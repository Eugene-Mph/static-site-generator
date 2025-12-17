from enum import Enum
from htmlnode import LeafNode
from collections.abc import Callable
import re

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
        
# create new inline TextNodes from composite TextNodes
        
def split_nodes_delimeter(old_nodes:list[TextNode], delimiter:str, text_type:TextType) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown syntax")

        for i, text in enumerate(sections):
            
            if text == "":
                continue

            if  i %2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes
            
    
def extract_markdown_images(text:str) -> list[tuple[str, str]]:
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    
    matches = re.findall(image_pattern, text)

    return matches

def extract_markdown_links(text:str) -> list[tuple[str, str]]:
    not_prefix = r"?<!"
    cap_text = r"[^\[\]]*"
    url = r"[^\(\)]*"

    link_pattern = fr"({not_prefix}!)\[({cap_text})\]\(({url})\)"

    matches = re.findall(link_pattern, text)

    return matches

    
def split_nodes(old_nodes:list[TextNode], extractor:Callable[[str], list[tuple[str, str]]], text_type:TextType) -> list[TextNode]:

    new_nodes:list[TextNode] = []


    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        

        links = (extractor(text))

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for _, link in enumerate(links):
            link_text, url = link

            delimiter = {
                TextType.LINK : f"[{link_text}]({url})",
                TextType.IMAGE : f"![{link_text}]({url})"
            }
            
            sections = text.split(delimiter[text_type], 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown link section not closed")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
    
            new_nodes.append(TextNode(link_text, text_type, url))

            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    
    return new_nodes