import unittest

from src.nodes.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr_props(self):
        node = HTMLNode("h1", "miku")
        node2 = HTMLNode("html", None, ["test-head", "test-body"], {"lang": "en"})
        node3 = HTMLNode("p", "This is cool", [HTMLNode("strong", "right?")])
        node4 = HTMLNode("body", None, [HTMLNode("p", "wow"), HTMLNode("p", "wow2")])

        self.assertEqual(repr(node), "HTMLNode(h1, miku, None, None)")
        self.assertEqual(node.props_to_html(), None)

        self.assertEqual(repr(node2), "HTMLNode(html, None, ['test-head', 'test-body'], {'lang': 'en'})")
        self.assertEqual(node2.props_to_html(), " lang=en")
        self.assertEqual(repr(node3), "HTMLNode(p, This is cool, [HTMLNode(strong, right?, None, None)], None)")

        self.assertEqual(node3.props_to_html(), None)
        self.assertEqual(repr(node4),
                         "HTMLNode(body, None, [HTMLNode(p, wow, None, None), HTMLNode(p, wow2, None, None)], None)")
        self.assertEqual(node4.props_to_html(), None)


if __name__ == "__main__":
    unittest.main()
