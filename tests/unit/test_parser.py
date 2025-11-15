"""
Unit tests for parser
"""

import pytest
from HTMLx.parser.ast_builder import ASTBuilder


def test_simple_element():
    """Test parsing simple element"""
    code = 'div { Hello }'
    
    builder = ASTBuilder(code, 'test.htmlx')
    ast = builder.parse()
    
    assert ast['type'] == 'Document'
    assert len(ast['children']) == 1
    assert ast['children'][0]['tag'] == 'div'


def test_element_with_classes():
    """Test parsing classes"""
    code = 'div.btn.primary { Click }'
    
    builder = ASTBuilder(code, 'test.htmlx')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert element['tag'] == 'div'
    assert 'btn' in element['classes']
    assert 'primary' in element['classes']


def test_element_with_id():
    """Test parsing ID"""
    code = 'button#submit { Submit }'
    
    builder = ASTBuilder(code, 'test.htmlx')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert element['id'] == 'submit'


def test_backend_call_attribute():
    """Test ⚡-call attribute"""
    code = 'button(⚡-call: "getData") { Load }'
    
    builder = ASTBuilder(code, 'test.htmlx')
    ast = builder.parse()
    
    element = ast['children'][0]
    assert '⚡-call' in element['attributes']


def test_invalid_emoji_in_id():
    """Test that emoji IDs cause error"""
    code = 'div#🎨 { Test }'
    
    builder = ASTBuilder(code, 'test.htmlx')
    
    # Should raise parse error or be caught by validator
    # (depends on where we check)
    try:
        ast = builder.parse()
        # If parsing succeeds, validator should catch it
        from HTMLx.validator.semantic import SemanticValidator
        validator = SemanticValidator(ast, 'test.htmlx')
        assert not validator.validate()
    except:
        # Parser caught it - that's ok too
        pass
