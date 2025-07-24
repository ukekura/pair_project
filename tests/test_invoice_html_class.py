from src.main import Invoice, Performances
import re

class TestOutputHtmlInvoiceContent:
  def test_correct_layout(self):
    invoice = Invoice({
      "performances": Performances([
        {
          "playID" : "hamlet",
          "audience" : 31
        },
        {
          "playID" : "as-like",
          "audience" : 35
        },
        {
          "playID" : "othello",
          "audience" : 31
        }
        ],
        {
          "hamlet" : {"name": "Hamlet", "type": "tragedy"},
          "as-like" : {"name": "As You Like It", "type": "comedy"},
          "othello" : {"name": "Othello", "type": "tragedy"}
        }),
      "customer": "BigCo"
    })
    output = invoice.output_html_invoice_content()
    customer = re.findall("<h2>BigCo</h2>", output)

    assert customer == ["<h2>BigCo</h2>"]
    assert re.findall("<h1>請求書</h1>", output) == ["<h1>請求書</h1>"]
    assert re.findall("<ul>", output) == ["<ul>"]
    assert re.findall("</ul>", output) == ["</ul>"]
    assert re.findall("<li>", output) == ["<li>", "<li>", "<li>"]
    assert re.findall("</li>", output) == ["</li>", "</li>", "</li>"]
    assert re.findall("合計金額：", output) == ["合計金額："]


    invoice = Invoice({
      "performances": Performances([
        {
          "playID" : "hamlet",
          "audience" : 31
        },
        {
          "playID" : "as-like",
          "audience" : 35
        },
        {
          "playID" : "othello",
          "audience" : 31
        }
        ],
        {
          "hamlet" : {"name": "Hamlet", "type": "tragedy"},
          "as-like" : {"name": "As You Like It", "type": "comedy"},
          "othello" : {"name": "Othello", "type": "tragedy"}
        }),
      "customer": "SmallCo"
    })
    output = invoice.output_html_invoice_content()
    customer = re.findall("<h2>SmallCo</h2>", output)
    assert customer == ["<h2>SmallCo</h2>"]