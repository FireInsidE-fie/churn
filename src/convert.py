from nodes.htmlnode import HTMLNode
from nodes.textnode import text_node_to_html_node
from parsing.blocks import markdown_to_blocks, block_to_block_type, BlockType
from src.parsing.parsing import text_to_textnodes


def block_to_paragraph(str):
    return HTMLNode("p", None, list(map(text_node_to_html_node, text_to_textnodes(str))))

def block_to_heading(str):
    header_level = 0
    for c in str:
        if c == '#':
            header_level += 1
    return HTMLNode(f"h{header_level}", str, list(map(text_node_to_html_node, text_to_textnodes(str))))

def block_to_code(str):
    return HTMLNode("code", str.strip('`'))

def block_to_quote(str):
    lines = str.split('\n')
    new_str = ""
    for line in lines:
        new_str = new_str + line[2:]
    return HTMLNode("q", new_str, list(map(text_node_to_html_node, text_to_textnodes(str))))

def block_to_unordered(str):
    lines = str.split('\n')
    new_str = ""
    for line in lines:
        new_str = new_str + line[2:]
    return HTMLNode("ul", new_str, list(map(text_node_to_html_node, text_to_textnodes(str)))) # Need child nodes for each list element

def block_to_ordered(str):
    lines = str.split('\n')
    new_str = ""
    for line in lines:
        new_str = new_str + line[2:]
    return HTMLNode("ol", new_str, list(map(text_node_to_html_node, text_to_textnodes(str)))) # Need child nodes for each list element

def markdown_to_html_node(md_str):
    blocks = markdown_to_blocks(md_str)
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        print(f"\nblock_type: {block_type}\n")
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
    print(parent_node)
    return parent_node
