"""
Comprehensive unit tests for htmlxify compiler
"""

import pytest
from pathlib import Path
from htmlxify.parser.ast_builder import ASTBuilder
from htmlxify.parser.indent_processor import IndentationProcessor
from htmlxify.validator.semantic import SemanticValidator
from htmlxify.generators.html_gen import HTMLGenerator
from htmlxify.generators.css_gen import CSSGenerator
from htmlxify.generators.js_gen import JSGenerator


# ==================== PARSER TESTS ====================

def test_simple_element():
    """Test parsing simple element"""
    code = 'div { Hello }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    assert ast['type'] == 'Document'
    assert len(ast['children']) == 1
    assert ast['children'][0]['tag'] == 'div'


def test_element_with_single_class():
    """Test parsing single class"""
    code = 'div.container { Content }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert element['tag'] == 'div'
    assert 'container' in element['classes']


def test_element_with_multiple_classes():
    """Test parsing multiple classes"""
    code = 'div.btn.primary.large { Click }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert element['tag'] == 'div'
    assert 'btn' in element['classes']
    assert 'primary' in element['classes']
    assert 'large' in element['classes']
    assert len(element['classes']) == 3


def test_element_with_id():
    """Test parsing ID"""
    code = 'button#submit { Submit }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert element['tag'] == 'button'
    assert element['id'] == 'submit'


def test_element_with_class_and_id():
    """Test parsing class and ID together"""
    code = 'div.container#main { Content }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert element['tag'] == 'div'
    assert 'container' in element['classes']
    assert element['id'] == 'main'


def test_nested_elements():
    """Test parsing nested elements"""
    code = 'div { p { Hello } }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    div = ast['children'][0]
    assert div['tag'] == 'div'
    assert len(div['children']) == 1
    
    p = div['children'][0]
    assert p['tag'] == 'p'


def test_multiple_siblings():
    """Test parsing multiple sibling elements"""
    code = 'div { First } span { Second }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    assert len(ast['children']) == 2
    assert ast['children'][0]['tag'] == 'div'
    assert ast['children'][1]['tag'] == 'span'


def test_empty_element():
    """Test parsing empty element"""
    code = 'div {}'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert element['tag'] == 'div'
    assert element['children'] == []


# ==================== ATTRIBUTE TESTS ====================

def test_single_attribute():
    """Test parsing single attribute"""
    code = 'a(href: "/about") { About }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert element['tag'] == 'a'
    assert 'href' in element['attributes']
    assert element['attributes']['href'] == '/about'


def test_multiple_attributes():
    """Test parsing multiple attributes"""
    code = 'input(type: "text", placeholder: "Enter name")'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert element['tag'] == 'input'
    assert element['attributes']['type'] == 'text'
    assert element['attributes']['placeholder'] == 'Enter name'


def test_backend_call_attribute():
    """Test ⚡-call attribute"""
    code = 'button(⚡-call: "getData") { Load }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert '⚡-call' in element['attributes']


def test_dynamic_data_attribute():
    """Test ⚡-data attribute"""
    code = 'span(⚡-data: "username") { Guest }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert '⚡-data' in element['attributes']


# ==================== VALIDATOR TESTS ====================

def test_valid_identifier():
    """Test valid identifier passes validation"""
    code = 'div#valid-id.valid-class { Content }'
    
    builder = ASTBuilder(code, 'test.htmlxify')
    ast = builder.parse()
    
    validator = SemanticValidator(ast, 'test.htmlxify')
    assert validator.validate() == True


def test_invalid_emoji_in_id():
    """Test that emoji IDs cause error"""
    test_ast = {
        'type': 'Document',
        'children': [
            {
                'type': 'Element',
                'tag': 'div',
                'id': '🎨',
                'classes': [],
                'attributes': {},
                'children': [],
                'meta': {}
            }
        ]
    }
    
    validator = SemanticValidator(test_ast, 'test.htmlxify')
    assert validator.validate() == False
    assert len(validator.errors) > 0


def test_performance_warning():
    """Test performance warnings"""
    test_ast = {
        'type': 'Document',
        'children': [
            {
                'type': 'Element',
                'tag': 'div',
                'id': None,
                'classes': [],
                'attributes': {
                    'animate': 'fade 1s'
                },
                'children': [],
                'meta': {}
            }
        ]
    }
    
    validator = SemanticValidator(test_ast, 'test.htmlxify')
    validator.validate()
    assert len(validator.warnings) > 0


# ==================== HTML GENERATOR TESTS ====================

def test_html_generation_simple():
    """Test basic HTML generation"""
    test_ast = {
        'type': 'Document',
        'children': [
            {
                'type': 'Element',
                'tag': 'div',
                'id': None,
                'classes': [],
                'attributes': {},
                'children': [
                    {
                        'type': 'Text',
                        'value': 'Hello World'
                    }
                ]
            }
        ]
    }
    
    gen = HTMLGenerator(test_ast, 'test.htmlxify')
    html, _ = gen.generate()
    
    assert '<!DOCTYPE html>' in html
    assert '<div>' in html
    assert 'Hello World' in html
    assert '</div>' in html


def test_html_xss_prevention():
    """Test XSS prevention in HTML generation"""
    test_ast = {
        'type': 'Document',
        'children': [
            {
                'type': 'Element',
                'tag': 'div',
                'id': None,
                'classes': [],
                'attributes': {},
                'children': [
                    {
                        'type': 'Text',
                        'value': '<script>alert("XSS")</script>'
                    }
                ]
            }
        ]
    }
    
    gen = HTMLGenerator(test_ast, 'test.htmlxify')
    html, _ = gen.generate()
    
    assert '<script>' not in html
    assert '&lt;script&gt;' in html
    assert '&lt;/script&gt;' in html


def test_html_with_classes_and_id():
    """Test HTML generation with classes and ID"""
    test_ast = {
        'type': 'Document',
        'children': [
            {
                'type': 'Element',
                'tag': 'div',
                'id': 'main',
                'classes': ['container', 'large'],
                'attributes': {},
                'children': []
            }
        ]
    }
    
    gen = HTMLGenerator(test_ast, 'test.htmlxify')
    html, _ = gen.generate()
    
    assert 'id="main"' in html
    assert 'class="container large"' in html


# ==================== CSS GENERATOR TESTS ====================

def test_css_generation():
    """Test CSS generation"""
    test_ast = {
        'type': 'Document',
        'children': [
            {
                'type': 'Element',
                'tag': 'div',
                'id': 'hero',
                'classes': [],
                'attributes': {
                    'style': {'background': '#FF0000'}
                },
                'children': []
            }
        ]
    }
    
    gen = CSSGenerator(test_ast)
    css = gen.generate()
    
    assert isinstance(css, str)


def test_css_animation_generation():
    """Test CSS animation generation"""
    test_ast = {
        'type': 'Document',
        'children': [
            {
                'type': 'Element',
                'tag': 'div',
                'id': 'animated',
                'classes': [],
                'attributes': {
                    'animate': 'fade 2s'
                },
                'children': []
            }
        ]
    }
    
    gen = CSSGenerator(test_ast)
    css = gen.generate()
    
    assert 'animation' in css.lower()
    assert '@keyframes' in css.lower()


# ==================== JAVASCRIPT GENERATOR TESTS ====================

def test_js_api_handler_generation():
    """Test JavaScript API handler generation"""
    test_ast = {
        'type': 'Document',
        'children': [
            {
                'type': 'Element',
                'tag': 'div',
                'id': None,
                'classes': [],
                'attributes': {
                    '⚡-call': {'type': 'backend_call', 'endpoint': 'getData'}
                },
                'children': []
            }
        ]
    }
    
    gen = JSGenerator(test_ast)
    js = gen.generate()
    
    assert 'apiHandlers' in js
    assert 'getData' in js


def test_js_data_binding_generation():
    """Test JavaScript data binding generation"""
    test_ast = {
        'type': 'Document',
        'children': [
            {
                'type': 'Element',
                'tag': 'span',
                'id': None,
                'classes': [],
                'attributes': {
                    '⚡-data': {'type': 'dynamic_data', 'key': 'username'}
                },
                'children': []
            }
        ]
    }
    
    gen = JSGenerator(test_ast)
    js = gen.generate()
    
    assert 'dataBindings' in js
    assert 'username' in js


# ==================== FIXTURE-BASED TESTS ====================

def test_fixture_simple():
    """Test compilation of simple fixture"""
    fixture_path = Path(__file__).parent.parent / 'fixtures' / 'simple.htmlxify'
    
    if fixture_path.exists():
        code = fixture_path.read_text(encoding='utf-8')
        builder = ASTBuilder(code, 'simple.htmlxify')
        ast = builder.parse()
        
        assert ast['type'] == 'Document'
        assert len(ast['children']) > 0


def test_fixture_with_classes():
    """Test compilation of fixture with classes"""
    fixture_path = Path(__file__).parent.parent / 'fixtures' / 'with_classes.htmlxify'
    
    if fixture_path.exists():
        code = fixture_path.read_text(encoding='utf-8')
        builder = ASTBuilder(code, 'with_classes.htmlxify')
        ast = builder.parse()
        
        has_classes = False
        for child in ast['children']:
            if child.get('classes'):
                has_classes = True
                break
        
        assert has_classes


# Run tests: pytest tests/unit/test_parser.py -v
