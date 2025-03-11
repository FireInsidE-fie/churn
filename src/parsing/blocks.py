def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    for block in blocks:
        index = blocks.index(block)
        blocks[index] = block.strip(' ').strip('\n')
        if not blocks[index]:
            del blocks[index]
    print(blocks)
    return blocks
