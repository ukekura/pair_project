from src.main import Invoice, Performances
import re

class TestOutputInvoiceContent:
  def test_correct_customer(self):
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
    output = invoice.output_invoice_content()
    customer = re.findall("BigCo", output)
    assert customer == ["BigCo"]

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
    output = invoice.output_invoice_content()
    customer = re.findall("SmallCo", output)
    assert customer == ["SmallCo"]