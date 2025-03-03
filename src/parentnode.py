from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        children_html = "".join(list(map(lambda elem: elem.to_html(), self.children)))
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        return f"<{self.tag}>{children_html}</{self.tag}>"
