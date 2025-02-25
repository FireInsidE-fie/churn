import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_basic_leafnode(self):
        node = LeafNode("h1", "miku")
        node2 = LeafNode("html", "empty", {"lang": "en"})
        node3 = LeafNode("p", "This is cool", {"id": "main", "class": "text"})
        node4 = LeafNode("body", "emptier")

        self.assertEqual(repr(node), "HTMLNode(h1, miku, None, None)")
        self.assertEqual(node.to_html(), "<h1>miku</h1>")
        self.assertEqual(node.props_to_html(), None)

        self.assertEqual(repr(node2), "HTMLNode(html, empty, None, {'lang': 'en'})")
        self.assertEqual(node2.to_html(), "<html lang=en>empty</html>")
        self.assertEqual(node2.props_to_html(), " lang=en")

        self.assertEqual(repr(node3), "HTMLNode(p, This is cool, None, {'id': 'main', 'class': 'text'})")
        self.assertEqual(node3.to_html(), "<p id=main class=text>This is cool</p>")
        self.assertEqual(node3.props_to_html(), " id=main class=text")

        self.assertEqual(repr(node4), "HTMLNode(body, emptier, None, None)")
        self.assertEqual(node4.to_html(), "<body>emptier</body>")
        self.assertEqual(node4.props_to_html(), None)

    def test_value_error_leafnode(self):
        node = LeafNode("p", None)

        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
