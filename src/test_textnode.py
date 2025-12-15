import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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




if __name__ == "__main__":
    unittest.main()