from src.parsing.split import *

def text_to_textnodes(text):
    starting_node = TextNode(text, TextType.NORMAL)

    nodes = split_nodes_image([starting_node])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)

    return nodes