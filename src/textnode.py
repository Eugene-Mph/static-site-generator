from enum import Enum

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