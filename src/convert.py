from nodes.htmlnode import HTMLNode
from parsing.blocks import markdown_to_blocks, block_to_block_type, BlockType

def block_to_paragraph(str):
    return HTMLNode("p", None)

def block_to_heading(str):
    header_level = 0
    for c in str:
        if c == '#':
            header_level += 1
    return HTMLNode(f"h{header_level}", str)

def block_to_code(str):
    return HTMLNode("code", str.strip('`'))

def block_to_quote(str):
    return HTMLNode("q", str[2:])

def block_to_unordered(str):
    pass

def block_to_ordered(str):
    pass

def markdown_to_html_node(md_str):
    blocks = markdown_to_blocks(md_str)
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                child_nodes.append(block_to_paragraph(block))
            case BlockType.HEADING:
                child_nodes.append(block_to_heading(block))
            case BlockType.CODE:
                child_nodes.append(block_to_code(block))
            case BlockType.QUOTE:
                child_nodes.append(block_to_quote(block))
            case BlockType.UNORDERED_LIST:
                child_nodes.append(block_to_unordered(block))
            case BlockType.ORDERED_LIST:
                child_nodes.append(block_to_ordered(block))

    parent_node = HTMLNode("div", None, child_nodes)
    return parent_node
