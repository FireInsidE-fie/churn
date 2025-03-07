import unittest

from links_images import extract_markdown_images, extract_markdown_links

class TestMarkdownImages(unittest.TestCase):
    def test_markdown_images1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) wowowowowo"
        images = extract_markdown_images(text)
        self.assertEqual(images[0], ("rick roll", "https://i.imgur.com/aKaOqIh.gif"))
        self.assertEqual(images[1], ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"))

    def test_markdown_images2(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        images = extract_markdown_images(text)
        self.assertEqual(images[0], ("image", "https://i.imgur.com/zjjcJKZ.png"))

    def test_markdown_images3(self):
        text = "This is text with no image ![]()"
        images = extract_markdown_links(text)
        self.assertEqual(images, None)

    def test_markdown_images4(self):
        text = "two ![images](wow.html)?? this is ![crazy!!!](wow2.html)"
        images = extract_markdown_links(text)
        self.assertEqual(images[0], ("images", "wow.html"))
        self.assertEqual(images[1], ("crazy!!!", "wow2.html"))

class TestMarkdownLinks(unittest.TestCase):
    def test_markdown_links1(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg) wowowowowo"
        links = extract_markdown_links(text)
        self.assertEqual(links[0], ("rick roll", "https://i.imgur.com/aKaOqIh.gif"))
        self.assertEqual(links[1], ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"))

    def test_markdown_links2(self):
        text = "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        links = extract_markdown_links(text)
        self.assertEqual(links[0], ("link", "https://i.imgur.com/zjjcJKZ.png"))

    def test_markdown_links3(self):
        text = "This is text with no link ![]()"
        links = extract_markdown_links(text)
        self.assertEqual(links, None)

    def test_markdown_links4(self):
        text = "two [links](wow.html)?? this is [crazy!!!](wow2.html)"
        links = extract_markdown_links(text)
        self.assertEqual(links[0], ("links", "wow.html"))
        self.assertEqual(links[1], ("crazy!!!", "wow2.html"))
