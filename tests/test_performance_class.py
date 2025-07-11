from src.main import Performance

def test_calc_price():
  performance = Performance({
        "name": "Hamlet",
        "audience": 29,
        "type": "tragedy"
      })
  price = performance.calc_price()
  assert price == 40000