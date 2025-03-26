class HTMLNode:
    def _init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              # which tag (<h1>)
        self.value = value          # value contained in tag
        self.children = children    # child elements (list)
        self.props = props          # properties (dict)

    def to_html(self):
        if not self.tag:
            raise ValueError("HTMLNode must have a tag")
        children_html = ""
        if self.children:
            children_html = "".join(list(map(lambda elem: elem.to_html(), self.children)))
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        return f"<{self.tag}>{children_html}</{self.tag}>"

    def props_to_html(self):
        if not self.props:
            return self.props
        final_string = ""
        for prop in self.props:
            final_string = final_string + f" {prop}={self.props[prop]}"
        return final_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
