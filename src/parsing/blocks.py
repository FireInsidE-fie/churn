import re

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST = "ordered_list",

def is_heading(block_str):
    if re.fullmatch("^#+.*$", block_str, re.MULTILINE):
        return True
    return False

def is_code(block_str):
    if block_str[:3] == "```" and block_str[-3:] == "```":
        return True
    return False

def is_quote(block_str):
    if block_str[0] != '>':
        return False
    for c in block_str:
        if c == '\n' and c + 1 != '>':
            return False
    return True

def is_unordered_list(block_str):
    pass

def is_ordered_list(block_str):
    pass

def block_to_block_type(block_str):
    if is_heading(block_str):
        return BlockType.HEADING
    if is_code(block_str):
        return BlockType.CODE
    if is_quote(block_str):
        return BlockType.QUOTE
    if is_unordered_list(block_str):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block_str):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
        stripped_block = block.strip()
        if not stripped_block:
            continue
        filtered_blocks.append(stripped_block)
    # print(filtered_blocks)
    return filtered_blocks
