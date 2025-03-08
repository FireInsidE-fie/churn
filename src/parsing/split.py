from src.textnode import TextNode, TextType

from extract import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not old_nodes or not delimiter or not text_type:
        raise ValueError("split_nodes_delimiter needs valid values")
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.NORMAL:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Syntax contains unmatched delimiter!")
        slices = node.text.split(delimiter)
        for s in slices:
            if slices.index(s) % 2 == 0:
                new_nodes.append(TextNode(s, TextType.NORMAL))
            else:
                new_nodes.append(TextNode(s, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        text = node.text
        if not images:
            nodes.append(node)
            continue
        for image in images:
            image_pattern = f"![{image[0]}]({image[1]})"
            text_node = TextNode(text.split(image_pattern)[0], TextType.NORMAL)
            image_node = TextNode(image[0], TextType.IMAGE, image[1])
            if text_node.text:
                nodes.append(text_node)
            nodes.append(image_node)
            text = text.split(image_pattern)[1]
            # print(text_node)
            # print(image_node)
        if text:
            nodes.append(TextNode(text, TextType.NORMAL))
    return nodes

def split_nodes_link(old_nodes):
    pass
