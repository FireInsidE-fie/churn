from src.nodes.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if self.props:
            return f"<{self.tag} {self.props_to_html().strip(' ')}>{self.value}</{self.tag}>"
        if self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"{self.value}"
