import unittest

from src.textnode import TextNode, TextType
from split import split_nodes_delimiter, split_nodes_image, split_nodes_link

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

    def test_split_delimiter5(self):
        node = TextNode("This is nothing but /italic/", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "/", TextType.ITALIC)

        self.assertEqual(new_nodes, [
            TextNode("This is nothing but /italic/", TextType.ITALIC),
        ])

    def test_split_delimiter6(self):
        node = TextNode("This is broken text with a /italic word", TextType.NORMAL)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "/", TextType.ITALIC)

    def test_split_delimiter7(self):
        node = TextNode("This is text with two !code! !words!", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "!", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is text with two ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" ", TextType.NORMAL),
            TextNode("words", TextType.CODE),
            TextNode("", TextType.NORMAL)
        ])

    def test_split_delimiter_empty(self):
        node = TextNode("This is text with *a `strong` word*", TextType.NORMAL)
        with self.assertRaises(AttributeError):
            split_nodes_delimiter(node, "*", TextType.WOW)
        with self.assertRaises(ValueError):
            split_nodes_delimiter(None, "*", TextType.BOLD)
            split_nodes_delimiter(node, "", TextType.BOLD)
            split_nodes_delimiter(node, "*", None)

class TestSplitImages(unittest.TestCase):
    def test_split_images1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images2(self):
        node = TextNode(
            "This is text with just one ![image](https://i.imgur.com/zjjcJKZ.png) and some text afterwards...",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with just one ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text afterwards...", TextType.NORMAL),
            ],
            new_nodes,
        )
