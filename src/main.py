from src.textnode import *
from src.leafnode import *
from src.htmlnode import *
from src.parentnode import *

def main():
    test = TextNode("Hewwo", TextType.NORMAL, "boot.dev")
    print(test)

main()
