from typing import  Any

class HTMLNode():
    def __init__(self, tag:str | None=None,
                value:str | None=None,
                children:list[Any] | None=None,
                props:dict[str, str] | None=None ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        
        if self.props == None:
            return ""
        return "".join([f" {key}={value}" for key, value in self.props.items()])
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children:{self.children}, {self.props})"
    

class LeafNode(HTMLNode):

    def __init__(self, tag: str | None=None, 
                value: str | None=None,
                props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):

        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag: str | None = None,
                children: list[HTMLNode] | None = None,
                props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        
        
        html_children = "".join([child.to_html() for child in self.children])
        

        return f"<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>"
    

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        
