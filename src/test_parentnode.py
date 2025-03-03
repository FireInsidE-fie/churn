import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_basic_parentnode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_without_anything(self):
        parent_node = ParentNode(None, None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_without_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_without_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren2(self):
        grandchild_node = LeafNode("a", "grandchild", {"href": "aisling.codes"})
        child_node = ParentNode("span", [grandchild_node], {"id": "id1"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span id=id1><a href=aisling.codes>grandchild</a></span></div>",
        )

    def test_to_html_with_grandchildren3(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_grandchildren4(self):
        grandchild_node = LeafNode("a", "grandchild", {"href": "aisling.codes"})
        grandchild_node2 = LeafNode("strong", "grandchild2", {"class": "wow1"})
        grandchild_node3 = LeafNode("b", "grandchild3", {"class": "wow2"})
        child_node = ParentNode("span", [grandchild_node], {"id": "id1"})
        child_node2 = ParentNode("span", [grandchild_node2, grandchild_node3], {"id": "id2"})
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span id=id1><a href=aisling.codes>grandchild</a></span><span id=id2><strong class=wow1>grandchild2</strong><b class=wow2>grandchild3</b></span></div>",
        )
