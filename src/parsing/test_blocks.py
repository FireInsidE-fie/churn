import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType

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

class TestBlockType(unittest.TestCase):
    def test_blocks_to_block_type_heading(self):
        test_str1 = "# miku"
        test_str2 = "### miku"
        test_str3 = "##### miku"
        test_str4 = "########## miku"

        self.assertEqual(block_to_block_type(test_str1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(test_str2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(test_str3), BlockType.HEADING)
        self.assertEqual(block_to_block_type(test_str4), BlockType.PARAGRAPH)

    def test_blocks_to_block_type_code(self):
        test_str1 = "```miku```"
        test_str2 = ("```"
                     "jfdlakfjsd wowowowowowowowo this is great oh and miku"
                     "```")
        test_str3 = "``````"
        test_str4 = "``miku```"
        test_str5 = "```miku``"
        test_str6 = "``````miku```"

        self.assertEqual(block_to_block_type(test_str1), BlockType.CODE)
        self.assertEqual(block_to_block_type(test_str2), BlockType.CODE)
        self.assertEqual(block_to_block_type(test_str3), BlockType.CODE)
        self.assertEqual(block_to_block_type(test_str4), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(test_str5), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(test_str6), BlockType.CODE)

    def test_blocks_to_block_type_quote(self):
        test_str1 = "> miku"
        test_str2 = ">"
        test_str3 = ("> wowowowowo"
                     "> zazzzz"
                     ">thisshould work too>jadklfj"
                     "> and also this!!")
        test_str4 = ("this should nOT work"
                     "> wowowowow"
                     "> oowoow")

        self.assertEqual(block_to_block_type(test_str1), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(test_str2), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(test_str3), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(test_str4), BlockType.PARAGRAPH)

    def test_blocks_to_block_type_unordered_list(self):
        test_str1 = "- miku"
        test_str2 = "- ## miku"
        test_str3 = ("- ----miku"
                     "- wow"
                     "- wow2-"
                     "- still works")
        test_str4 = "-miku"

        self.assertEqual(block_to_block_type(test_str1), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(test_str2), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(test_str3), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(test_str4), BlockType.PARAGRAPH)

    def test_blocks_to_block_type_ordered_list(self):
        test_str1 = "1. miku"
        test_str2 = "44. "
        test_str3 = ("1. ----miku"
                     "2. wow"
                     "4. wow2-"
                     "5. still works")
        test_str4 = "6.miku"

        self.assertEqual(block_to_block_type(test_str1), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(test_str2), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(test_str3), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(test_str4), BlockType.PARAGRAPH)
