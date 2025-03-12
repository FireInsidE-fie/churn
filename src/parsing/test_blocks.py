import unittest

from blocks import markdown_to_blocks

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks2(self):
        md = """
The **missile**
knows where it is

because
- it
- knows

- where
- it
- isn't



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "The **missile**\nknows where it is",
                "because\n- it\n- knows",
                "- where\n- it\n- isn't"
            ],
        )

    def test_markdown_to_blocks3(self):
        md = """
I'm thinking

Miiiikuuuu



Miiikuuu

ou


i


ou
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "I'm thinking",
                "Miiiikuuuu",
                "Miiikuuu",
                "ou",
                "i",
                "ou",
            ],
        )

    def test_markdown_to_blocks4(self):
        md = """
        
        
        
        
        
        
        
        
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            []
        )
