import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is another text node", TextType.CODE, "google.com")
        node4 = TextNode("This is another text node", TextType.CODE, "google.com")
        node5 = TextNode("This is a final text node", TextType.CODE)
        node6 = TextNode("This is a final text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertNotEqual(node5, node6)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node4)

    def test_repr(self):
        node = TextNode("miku", TextType.ITALIC, "miku.com")
        node2 = TextNode("teto", TextType.BOLD, "tetopear.ch")
        node3 = TextNode("not rin", TextType.CODE)
        self.assertEqual(repr(node), "TextNode(miku, italic, miku.com)")
        self.assertEqual(repr(node2), "TextNode(teto, bold, tetopear.ch)")
        self.assertEqual(repr(node3), "TextNode(not rin, code, None)")

    def test_text_to_html1(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html3(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html4(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html5(self):
        node = TextNode("This is a text node", TextType.LINK, "aisling.codes")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "aisling.codes"})

    def test_text_to_html6(self):
        node = TextNode("This is a text node", TextType.IMAGE, "cuteimage.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"href": "cuteimage.png"})

    def test_text_to_html7(self):
        node = TextNode("This is a text node", "MIKU", "cuteimage.png")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
