from textnode import TextNode, TextType


def main() -> None:
    print("with url link")
    print(TextNode("anchor text", TextType.TEXT, "https://www.example.com"), "\n")

    print("No url link")
    print(TextNode("plain text", TextType.TEXT))
   


main()