import unittest

from textnode import (
    TextNode,
    TextType,
    text_node_to_html_node,
    split_nodes_delimeter,
    extract_markdown_images,
    extract_markdown_links
)



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false_text(self):
        node1 = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_eq_false_text_type(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_eq_true_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self. assertEqual(
            "TextNode(This is a text node, text, None)", repr(node)
        )

    def test_text_to_html(self):
        text_node = TextNode("raw text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "raw text")

    def test_bold_text_to_html(self):
        bold_text_node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(bold_text_node)

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")

    def test_link_to_html(self):
        link_text_node = TextNode("click me", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(link_text_node)

        self.assertEqual(html_node.tag, "a")

        if html_node.props is None:
            self.assertNotEqual(html_node.props, None)
        else:
            self.assertEqual(html_node.props["href"], "https://example.com")


    def test_split_nodes_delimiter_at_start(self):
        old_node = TextNode("**bold** at start", TextType.TEXT)
        new_nodes = split_nodes_delimeter([old_node], "**", TextType.BOLD)

        out = [
            TextNode("bold", TextType.BOLD),
            TextNode(" at start", TextType.TEXT)
        ]

        self.assertListEqual(new_nodes, out)

    def test_split_nodes_delimiter_many(self):
        old_nodes = [
            TextNode("This is **bold1** and **bold2**", TextType.TEXT),
            TextNode("This is **bold3** and _italic1_", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimeter(old_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimeter(new_nodes, "_", TextType.ITALIC)

        out = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold1", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold2", TextType.BOLD),
            TextNode("This is ", TextType.TEXT),
            TextNode("bold3", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic1", TextType.ITALIC),
        ]

        self.assertListEqual(new_nodes, out)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)

        out = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]

        self.assertListEqual(matches, out)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) ![alt text for image](url/of/image.jpg)"
        
        matches = extract_markdown_links(text)

        out = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]

        self.assertListEqual(matches, out)




if __name__ == "__main__":
    unittest.main()