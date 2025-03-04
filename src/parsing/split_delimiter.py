from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    slices = old_nodes.split(delimiter, text_type)
    new_nodes = [
        TextNode(slices[0], TextType.NORMAL),
        TextNode(slices[1], text_type),
        TextNode(slices[2], TextType.NORMAL)
    ]
    return new_nodes


