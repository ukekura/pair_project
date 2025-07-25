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


  def test_comedy_twenty_or_under(self):
    performance = Performance({
          "name": "As You Like It",
          "audience": 20,
          "type": "comedy"
        })
    price = performance.calc_price()
    assert price == 36000

    performance = Performance({
          "name": "As You Like It",
          "audience": 10,
          "type": "comedy"
        })
    price = performance.calc_price()
    assert price == 33000


  def test_comedy_over_twenty(self):
    performance = Performance({
          "name": "As You Like It",
          "audience": 21,
          "type": "comedy"
        })
    price = performance.calc_price()
    assert price == 46800

    performance = Performance({
          "name": "As You Like It",
          "audience": 30,
          "type": "comedy"
        })
    price = performance.calc_price()
    assert price == 54000


  def test_tragic_comedy(self):
    performance = Performance({
          "name": "Romeo and Juliet",
          "audience": 30,
          "type": "tragic-comedy"
        })
    price = performance.calc_price()
    assert price == 50000

    performance = Performance({
          "name": "Romeo and Juliet",
          "audience": 21,
          "type": "tragic-comedy"
        })
    price = performance.calc_price()
    assert price == 45500


class TestCalcPoint:
  def test_comedy_thirty_or_under(self):
    performance = Performance({
          "name": "As You Like It",
          "audience": 30,
          "type": "comedy"
        })
    point = performance.calc_point()
    assert point == 6

    performance = Performance({
          "name": "As You Like It",
          "audience": 20,
          "type": "comedy"
        })
    point = performance.calc_point()
    assert point == 4


  def test_comedy_over_thirty(self):
    performance = Performance({
          "name": "As You Like It",
          "audience": 31,
          "type": "comedy"
        })
    point = performance.calc_point()
    assert point == 7

    performance = Performance({
          "name": "As You Like It",
          "audience": 40,
          "type": "comedy"
        })
    point = performance.calc_point()
    assert point == 18


  def test_exception_comedy_thirty_or_under(self):
    performance = Performance({
          "name": "Hamlet",
          "audience": 30,
          "type": "tragedy"
        })
    point = performance.calc_point()
    assert point == 0

    performance = Performance({
          "name": "Hamlet",
          "audience": 20,
          "type": "tragedy"
        })
    point = performance.calc_point()
    assert point == 0


  def test_exception_comedy_over_thirty(self):
    performance = Performance({
          "name": "Hamlet",
          "audience": 31,
          "type": "tragedy"
        })
    point = performance.calc_point()
    assert point == 1

    performance = Performance({
          "name": "Hamlet",
          "audience": 40,
          "type": "tragedy"
        })
    point = performance.calc_point()
    assert point == 10


  def test_tragic_comedy_over_twenty(self):
    performance = Performance({
          "name": "Romeo and Juliet",
          "audience": 21,
          "type": "tragic-comedy"
        })
    point = performance.calc_point()
    assert point == 1
    
    performance = Performance({
          "name": "Romeo and Juliet",
          "audience": 40,
          "type": "tragic-comedy"
        })
    point = performance.calc_point()
    assert point == 20


    def test_tragic_comedy_twenty_or_under(self):
      performance = Performance({
            "name": "Romeo and Juliet",
            "audience": 20,
            "type": "tragic-comedy"
          })
      point = performance.calc_point()
      assert point == 0

      performance = Performance({
            "name": "Romeo and Juliet",
            "audience": 10,
            "type": "tragic-comedy"
          })
      point = performance.calc_point()
      assert point == 0