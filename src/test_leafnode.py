import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_repr_props(self):
        node = LeafNode("h1", "miku")
        node2 = LeafNode("html", None, {"lang":"en"})
        node3 = LeafNode("p", "This is cool")
        node4 = LeafNode("body", None)
        self.assertEqual(repr(node), "HTMLNode(h1, miku, None, None)")
        self.assertEqual(node.to_html(), "<h1>miku<\h1>")
        self.assertEqual(node.props_to_html(), None)

if __name__ == "__main__":
    unittest.main()
