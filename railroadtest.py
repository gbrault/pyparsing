from pyparsing.diagram import to_railroad, railroad_to_html
import pprint


def make_diagram(expr, output_html="output.html"):
    with open(output_html, "w", encoding="utf-8") as fp:
        railroad = to_railroad(expr)
        fp.write(railroad_to_html(railroad))


from ebnftest import ebnf_parser as imported_expr

pprint.pprint(imported_expr)

make_diagram(imported_expr)