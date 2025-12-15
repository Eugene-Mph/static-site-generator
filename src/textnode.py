from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text:str, text_type: TextType, url:str | None=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, obj:object) -> bool: 

        if not isinstance(obj, TextNode):
            return False
        
        return (
            self.text == obj.text
            and self.text_type.value == obj.text_type.value
            and self.url == obj.url
        )
    

    def __repr__(self) -> str:

        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node : TextNode) -> LeafNode:
    value = text_node.text
    url = text_node.url

    match text_node.text_type.value:

        case "text":
            return LeafNode(None, value)
        
        case "bold":
            return LeafNode("b", value)
        
        case "italic":
            return LeafNode("i", value)
        
        case "code":
            return LeafNode("code", value)
        
        case "link":

            if url is None:
                raise ValueError("Invalid link: no url")
            
            return LeafNode("a", value, {"href": url})
        
        case "image":

            if url is None:
                raise ValueError("Invalid image: no url")

            return LeafNode("img", "", {"src": url, "alt":value})
        
    

