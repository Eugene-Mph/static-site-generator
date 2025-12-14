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

    def to_html(self) -> NotImplementedError:
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        
        if self.props == None:
            return ""
        return "".join([f" {key}={value}" for key, value in self.props.items()])
    
    def __repr__(self) -> str:
        return f"({self.tag}, {self.value}, children:{self.children}, {self.props})"