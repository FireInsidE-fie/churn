from nodes.htmlnode import HTMLNode
from parsing.blocks import markdown_to_blocks, block_to_block_type, BlockType

def markdown_to_html_node(md_str):
    blocks = markdown_to_blocks(md_str)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                html_node = HTMLNode("p", md_str)
            case BlockType.HEADING:
                pass
            case BlockType.CODE:
                pass
            case BlockType.QUOTE:
                pass
            case BlockType.UNORDERED_LIST:
                pass
            case BlockType.ORDERED_LIST:
                pass
