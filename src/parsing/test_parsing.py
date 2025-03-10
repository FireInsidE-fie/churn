import unittest

from src.textnode import TextNode, TextType
from parsing import text_to_textnodes


class TestParsing(unittest.TestCase):
    def test_parsing1(self):
        input_text = ("This is **text** with an _italic_ word and a `code block`"
                      "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
                      "and a [link](https://boot.dev)")

        nodes = text_to_textnodes(input_text)

        self.assertListEqual(nodes, [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])
