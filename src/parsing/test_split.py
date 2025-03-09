import unittest

from src.textnode import TextNode, TextType
from split import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter1(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL)
        ])

    def test_split_delimiter2(self):
        node = TextNode("This is text with a *strong* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("strong", TextType.BOLD),
            TextNode(" word", TextType.NORMAL)
        ])

    def test_split_delimiter3(self):
        node = TextNode("This is text with *a `strong` word*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.NORMAL),
            TextNode("a `strong` word", TextType.BOLD),
            TextNode("", TextType.NORMAL)
        ])

    def test_split_delimiter4(self):
        node = TextNode("This is text with a /italic/ word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "/", TextType.ITALIC)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.NORMAL)
        ])

    def test_split_delimiter5(self):
        node = TextNode("This is nothing but /italic/", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "/", TextType.ITALIC)

        self.assertEqual(new_nodes, [
            TextNode("This is nothing but /italic/", TextType.ITALIC),
        ])

    def test_split_delimiter6(self):
        node = TextNode("This is broken text with a /italic word", TextType.NORMAL)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "/", TextType.ITALIC)

    def test_split_delimiter7(self):
        node = TextNode("This is text with two !code! !words!", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "!", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is text with two ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" ", TextType.NORMAL),
            TextNode("words", TextType.CODE),
            TextNode("", TextType.NORMAL)
        ])

    def test_split_delimiter_empty(self):
        node = TextNode("This is text with *a `strong` word*", TextType.NORMAL)
        with self.assertRaises(AttributeError):
            split_nodes_delimiter(node, "*", TextType.WOW)
        with self.assertRaises(ValueError):
            split_nodes_delimiter(None, "*", TextType.BOLD)
            split_nodes_delimiter(node, "", TextType.BOLD)
            split_nodes_delimiter(node, "*", None)

class TestSplitImages(unittest.TestCase):
    def test_split_images1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images2(self):
        node = TextNode(
            "This is text with just one ![image](https://i.imgur.com/zjjcJKZ.png) and some text afterwards...",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with just one ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text afterwards...", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_split_images3(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        node2 = TextNode(
            "![image2](https://i.imgur.com/zjjcJKZ2.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node, node2])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("image2", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ2.png"),
            ],
            new_nodes,
        )

    def test_split_images4(self):
        node = TextNode(
            "This is text with just no images...",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with just no images...", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_split_images5(self):
        node = TextNode(
            "wowowowowowow ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        node2 = TextNode(
            "![image2](https://i.imgur.com/zjjcJKZ2.png) wowowowowoowow",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node, node2])
        self.assertListEqual(
            [
                TextNode("wowowowowowow ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("image2", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ2.png"),
                TextNode(" wowowowowoowow", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_split_images6(self):
        node = TextNode(
            "This is text with an ![image followed by](https://i.imgur.com/zjjcJKZ.png)![a second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        node2 = TextNode(
            "![image followed by](https://i.imgur.com/zjjcJKZ.png)![a second image](https://i.imgur.com/3elNhQu.png)![and a third](i.love.you)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node, node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image followed by", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "a second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(
                    "image followed by", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"
                ),
                TextNode(
                    "a second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(
                    "and a third", TextType.IMAGE, "i.love.you"
                ),
            ],
            new_nodes,
        )

    def test_split_images7(self):
        node = TextNode(
            "wowowowowowow ![broken ]ima(ge](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        node2 = TextNode(
            "![](https://i.imgur.com/zjjcJKZ2.png) wowowowowoowow",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node, node2])
        self.assertListEqual(
            [
                TextNode("wowowowowowow ![broken ]ima(ge](https://i.imgur.com/zjjcJKZ.png)", TextType.NORMAL),
                TextNode("![](https://i.imgur.com/zjjcJKZ2.png) wowowowowoowow", TextType.NORMAL),
            ],
            new_nodes,
        )

class TestSplitLinks(unittest.TestCase):
    def test_split_links1(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links2(self):
        node = TextNode(
            "This is text with just one [link](https://i.imgur.com/zjjcJKZ.png) and some text afterwards...",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with just one ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text afterwards...", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_split_links3(self):
        node = TextNode(
            "[link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        node2 = TextNode(
            "[link2](https://i.imgur.com/zjjcJKZ2.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node, node2])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("link2", TextType.LINK, "https://i.imgur.com/zjjcJKZ2.png"),
            ],
            new_nodes,
        )

    def test_split_links4(self):
        node = TextNode(
            "This is text with just no links...",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with just no links...", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_split_links5(self):
        node = TextNode(
            "wowowowowowow [link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        node2 = TextNode(
            "[link2](https://i.imgur.com/zjjcJKZ2.png) wowowowowoowow",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node, node2])
        self.assertListEqual(
            [
                TextNode("wowowowowowow ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("link2", TextType.LINK, "https://i.imgur.com/zjjcJKZ2.png"),
                TextNode(" wowowowowoowow", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_split_links6(self):
        node = TextNode(
            "This is text with a [link followed by](https://i.imgur.com/zjjcJKZ.png)[a second link](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        node2 = TextNode(
            "[link followed by](https://i.imgur.com/zjjcJKZ.png)[a second link](https://i.imgur.com/3elNhQu.png)[and a third](i.love.you)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node, node2])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("link followed by", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "a second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(
                    "link followed by", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"
                ),
                TextNode(
                    "a second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(
                   "and a third", TextType.LINK, "i.love.you"
                ),
            ],
            new_nodes,
        )

    def test_split_links7(self):
        node = TextNode(
            "wowowowowowow ![broken ]lin(k](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL,
        )
        node2 = TextNode(
            "![](https://i.imgur.com/zjjcJKZ2.png) wowowowowoowow",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node, node2])
        self.assertListEqual(
            [
                TextNode("wowowowowowow ![broken ]lin(k](https://i.imgur.com/zjjcJKZ.png)", TextType.NORMAL),
                TextNode("![](https://i.imgur.com/zjjcJKZ2.png) wowowowowoowow", TextType.NORMAL),
            ],
            new_nodes,
        )
