import unittest

from src.textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter1(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL)
        ])
