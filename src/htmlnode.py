from typing import Self

class HTMLNode():
    def __init__(self, tag:str | None=None,
                value:str | None=None,
                children:list[Self] | None=None,
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
            raise ValueError("value of leaf node missng")
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"