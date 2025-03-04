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

    def test_split_delimiter2(self):
        node = TextNode("This is text with a *strong* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("strong", TextType.BOLD),
            TextNode(" word", TextType.NORMAL)
        ])

    def test_split_delimiter3(self):
        node = TextNode("This is text with *a `strong` word*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.NORMAL),
            TextNode("a `strong` word", TextType.BOLD),
            TextNode("", TextType.NORMAL)
        ])

    def test_split_delimiter4(self):
        node = TextNode("This is text with a /italic/ word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "/", TextType.ITALIC)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL)
        ])

    def test_split_delimiter_empty(self):
        node = TextNode("This is text with *a `strong` word*", TextType.NORMAL)
        with self.assertRaises(AttributeError):
            split_nodes_delimiter(node, "*", TextType.WOW)
        with self.assertRaises(ValueError):
            new_nodes1 = split_nodes_delimiter(None, "*", TextType.BOLD)
            new_nodes2 = split_nodes_delimiter(node, "", TextType.BOLD)
            new_nodes3 = split_nodes_delimiter(node, "*", None)
