from src.textnode import TextNode, TextType

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


