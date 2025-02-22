import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("miku", TextType.ITALIC, "miku.com")
        node = TextNode("teto", TextType.BOLD, "tetopear.com")
        self.assertEqual(repr(node), "TextNode(teto, bold, tetopear.com)")

if __name__ == "__main__":
    unittest.main()
