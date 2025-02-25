class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              # which tag (<h1>)
        self.value = value          # value contained in tag
        self.children = children    # child elements (list)
        self.props = props          # properties (dict)

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return self.props
        final_string = ""
        for prop in self.props:
            final_string = final_string + f" {prop}={self.props[prop]} "
        return final_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
