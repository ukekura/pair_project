from src.main import Performance

class TestCalcPrice:
  def test_tragedy_thirty_or_under(self):
    performance = Performance({
          "name": "Hamlet",
          "audience": 30,
          "type": "tragedy"
        })
    price = performance.calc_price()
    assert price == 40000

    performance = Performance({
      "name": "Hamlet",
      "audience": 23,
      "type": "tragedy"
    })
    price = performance.calc_price()
    assert price == 40000

  def test_tragedy_over_thirty(self):
    performance = Performance({
          "name": "Hamlet",
          "audience": 31,
          "type": "tragedy"
        })
    price = performance.calc_price()
    assert price == 41000

    performance = Performance({
          "name": "Hamlet",
          "audience": 40,
          "type": "tragedy"
        })
    price = performance.calc_price()
    assert price == 50000


