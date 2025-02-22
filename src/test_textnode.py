import unittest

from textnode import TextNode, TextType

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

if __name__ == "__main__":
    unittest.main()
