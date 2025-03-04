from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not old_nodes or not delimiter or not text_type:
        raise ValueError("split_nodes_delimiter needs valid values")
    new_nodes = []
    for node in old_nodes:
        slices = node.text.split(delimiter)
        new_nodes.append(TextNode(slices[0], TextType.NORMAL))
        new_nodes.append(TextNode(slices[1], text_type))
        new_nodes.append(TextNode(slices[2], TextType.NORMAL))
    return new_nodes


