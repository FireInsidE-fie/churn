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
