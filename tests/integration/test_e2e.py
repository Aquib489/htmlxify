"""
Integration tests for end-to-end compilation
"""

import pytest
from pathlib import Path
import tempfile
import shutil
from htmlxify.parser.ast_builder import ASTBuilder
from htmlxify.parser.indent_processor import IndentationProcessor
from htmlxify.validator.semantic import SemanticValidator
from htmlxify.generators.html_gen import HTMLGenerator
from htmlxify.generators.css_gen import CSSGenerator
from htmlxify.generators.js_gen import JSGenerator


class TestEndToEndCompilation:
    """Test full compilation pipeline"""
    
    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for test outputs"""
        temp = tempfile.mkdtemp()
        yield temp
        shutil.rmtree(temp)
    
    def compile_file(self, source_code: str, filename: str):
        """Helper method to compile source code through full pipeline"""
        # Parse
        builder = ASTBuilder(source_code, filename)
        ast = builder.parse()
        
        # Process indentation
        processor = IndentationProcessor()
        ast = processor.process(ast)
        
        # Validate
        validator = SemanticValidator(ast, filename)
        if not validator.validate():
            raise ValueError("Validation failed")
        
        # Generate HTML
        html_gen = HTMLGenerator(ast, filename)
        html, source_map = html_gen.generate()
        
        # Generate CSS
        css_gen = CSSGenerator(ast)
        css = css_gen.generate()
        
        # Generate JS
        js_gen = JSGenerator(ast)
        js = js_gen.generate()
        
        return html, css, js, source_map
    
    def test_simple_page_compilation(self):
        """Test compiling a simple page"""
        source = 'div { Hello World }'
        
        html, css, js, source_map = self.compile_file(source, 'test.htmlxify')
        
        assert '<!DOCTYPE html>' in html
        assert '<div>' in html
        assert 'Hello World' in html
        assert isinstance(css, str)
        assert isinstance(js, str)
    
    def test_nested_structure_compilation(self):
        """Test compiling nested structures"""
        source = '''
div.container {
  header { h1 { Title } }
  main { p { Content } }
  footer { p { Footer } }
}
        '''
        
        html, css, js, source_map = self.compile_file(source, 'test.htmlxify')
        
        assert '<header>' in html
        assert '<main>' in html
        assert '<footer>' in html
        assert 'Title' in html
        assert 'Content' in html
        assert 'Footer' in html
    
    def test_api_integration_compilation(self):
        """Test compiling with API integration"""
        source = 'div(⚡-call: "getData") { Loading... }'
        
        html, css, js, source_map = self.compile_file(source, 'test.htmlxify')
        
        assert 'data-api-call="getData"' in html
        assert 'apiHandlers' in js
        assert 'getData' in js
    
    def test_data_binding_compilation(self):
        """Test compiling with data binding"""
        source = 'span(⚡-data: "username") { Guest }'
        
        html, css, js, source_map = self.compile_file(source, 'test.htmlxify')
        
        assert 'data-dynamic="username"' in html
        assert 'dataBindings' in js
        assert 'username' in js
    
    def test_animation_compilation(self):
        """Test compiling with animations"""
        source = 'div(animate: "fade 2s") { Animated }'
        
        html, css, js, source_map = self.compile_file(source, 'test.htmlxify')
        
        assert 'animation' in css.lower()
        assert '@keyframes' in css.lower()
        assert 'fade' in css.lower()
    
    def test_xss_prevention_compilation(self):
        """Test XSS prevention in compilation"""
        source = 'div { <script>alert("XSS")</script> }'
        
        html, css, js, source_map = self.compile_file(source, 'test.htmlxify')
        
        assert '<script>' not in html
        assert '&lt;script&gt;' in html
    
    def test_fixture_complete_page(self):
        """Test compiling complete page fixture"""
        fixture_path = Path(__file__).parent.parent / 'fixtures' / 'complete_page.htmlxify'
        
        if fixture_path.exists():
            source = fixture_path.read_text(encoding='utf-8')
            
            html, css, js, source_map = self.compile_file(source, 'complete_page.htmlxify')
            
            # Check HTML structure
            assert '<!DOCTYPE html>' in html
            assert '<header' in html
            assert '<main' in html
            assert '<footer' in html
            
            # Check that content is present
            assert 'My Website' in html or 'website' in html.lower()
            
            # Check generated files are not empty
            assert len(html) > 100
            assert isinstance(css, str)
            assert isinstance(js, str)
    
    def test_multiple_files_compilation(self, temp_dir):
        """Test compiling multiple files"""
        files = {
            'page1.htmlxify': 'div { Page 1 }',
            'page2.htmlxify': 'div { Page 2 }',
            'page3.htmlxify': 'div { Page 3 }'
        }
        
        outputs = {}
        for filename, source in files.items():
            html, css, js, _ = self.compile_file(source, filename)
            outputs[filename] = {'html': html, 'css': css, 'js': js}
        
        # Verify all compiled successfully
        assert len(outputs) == 3
        assert 'Page 1' in outputs['page1.htmlxify']['html']
        assert 'Page 2' in outputs['page2.htmlxify']['html']
        assert 'Page 3' in outputs['page3.htmlxify']['html']


# Run tests: pytest tests/integration/test_e2e.py -v
