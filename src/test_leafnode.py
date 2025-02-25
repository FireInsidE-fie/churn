import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_repr_props(self):
        node = LeafNode("h1", "miku")
        node2 = LeafNode("html", "empty", {"lang": "en"})
        node3 = LeafNode("p", "This is cool")
        node4 = LeafNode("body", "emptier")
        node5 = LeafNode("p", None)

        self.assertEqual(repr(node), "HTMLNode(h1, miku, None, None)")
        self.assertEqual(node.to_html(), "<h1>miku</h1>")
        self.assertEqual(node.props_to_html(), None)

        self.assertEqual(repr(node2), "HTMLNode(html, empty, None, {'lang': 'en'})")
        self.assertEqual(node2.to_html(), "<html lang=en >empty</html>")
        self.assertEqual(node2.props_to_html(), " lang=en ")

        self.assertEqual(repr(node3), "HTMLNode(p, This is cool, None, None)")
        self.assertEqual(node3.to_html(), "<p>This is cool</p>")
        self.assertEqual(node3.props_to_html(), None)

        self.assertEqual(repr(node4), "HTMLNode(body, emptier, None, None)")
        self.assertEqual(node4.to_html(), "<body>emptier</body>")
        self.assertEqual(node4.props_to_html(), None)

if __name__ == "__main__":
    unittest.main()
