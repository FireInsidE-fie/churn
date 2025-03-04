from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        slices = node.text.split(delimiter)
        new_nodes.append(TextNode(slices[0], TextType.NORMAL))
        new_nodes.append(TextNode(slices[1], text_type))
        new_nodes.append(TextNode(slices[2], TextType.NORMAL))
    print(new_nodes)
    return new_nodes


