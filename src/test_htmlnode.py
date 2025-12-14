import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    

    def test_props_to_html(self):

        attributes = {"href":"https://example.com", "target":"_blank"}

        node = HTMLNode("a", "example link", None, attributes)
        out = f" href={attributes['href']} target={attributes['target']}"
        self.assertEqual(node.props_to_html(), out)

    def test_values(self):

        node = HTMLNode("h1", "This is the main title")

        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "This is the main title")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        children = [HTMLNode("li", f"item{i}") for i in range(3)]
        node = HTMLNode(
            "ul",
            None,
            children,
            None
        )

        out_ul = f"HTMLNode(ul, None, children:{children}, None)"
        out_li = f"HTMLNode(li, item0, children:None, None)"

        self.assertEqual(repr(children[0]), out_li)
        self.assertEqual(repr(node), out_ul)

