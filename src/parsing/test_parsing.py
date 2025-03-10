import unittest

from src.textnode import TextNode, TextType
from parsing import text_to_textnodes


class TestParsing(unittest.TestCase):
    def test_parsing1(self):
        input_text = ("This is **text** with an _italic_ word and a `code block`"
                      " and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
                      " and a [link](https://boot.dev)")

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

    def test_parsing2(self):
        input_text = ("The **missile** knows where _it_ is, because _it_ knows where it"
                      " [isn't.](not.a.place)")

        nodes = text_to_textnodes(input_text)

        self.assertListEqual(nodes, [
            TextNode("The ", TextType.NORMAL),
            TextNode("missile", TextType.BOLD),
            TextNode(" knows where ", TextType.NORMAL),
            TextNode("it", TextType.ITALIC),
            TextNode(" is, because ", TextType.NORMAL),
            TextNode("it", TextType.ITALIC),
            TextNode(" knows where it ", TextType.NORMAL),
            TextNode("isn't.", TextType.LINK, "not.a.place"),
        ])

    def test_parsing3(self):
        input_text = ("I'm **thinking** Miiiikuuu _Miiikuuu ooioo_,"
                      " hiding in your ![wifi](your.wifi), see **if** you can find [me]()")

        nodes = text_to_textnodes(input_text)

        self.assertListEqual(nodes,[
            TextNode("I'm ", TextType.NORMAL),
            TextNode("thinking", TextType.BOLD),
            TextNode(" Miiiikuuu ", TextType.NORMAL),
            TextNode("Miiikuuu ooioo", TextType.ITALIC),
            TextNode(", hiding in your ", TextType.NORMAL),
            TextNode("wifi", TextType.IMAGE, "your.wifi"),
            TextNode(", see ", TextType.NORMAL),
            TextNode("if", TextType.BOLD),
            TextNode(" you can find [me]()", TextType.NORMAL),
        ])

    def test_parsing4(self):
        input_text = ("*that sure ** is a lot of brok_en text![]")

        with self.assertRaises(Exception):
            text_to_textnodes(input_text)
