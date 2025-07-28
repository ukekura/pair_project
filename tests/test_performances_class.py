from src.main import Performances
import pytest

class TestCalcTotalPrice:
  def test_calc_total_price(self):
    performances = Performances([
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
    })
    total_price = performances.calc_total_price()
    assert total_price == 140000

    performances = Performances([
      {
        "playID" : "hamlet",
        "audience" : 31
      },
      {
        "playID" : "as-like",
        "audience" : 35
      }
    ],
    {
      "hamlet" : {"name": "Hamlet", "type": "tragedy"},
      "as-like" : {"name": "As You Like It", "type": "comedy"},
    })
    total_price = performances.calc_total_price()
    assert total_price == 99000


class TestCalcTotalPoint:
  def test_calc_total_point(self):
    performances = Performances([
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
    })
    total_point = performances.calc_total_point()
    assert total_point == 14

    performances = Performances([
      {
        "playID" : "hamlet",
        "audience" : 31
      },
      {
        "playID" : "as-like",
        "audience" : 35
      }
    ],
    {
      "hamlet" : {"name": "Hamlet", "type": "tragedy"},
      "as-like" : {"name": "As You Like It", "type": "comedy"},
    })
    total_point = performances.calc_total_point()
    assert total_point == 13

class TestCreatePerformance:
  def test_invalid_performance_type(self):
    test_performance = {"playID": "invaild-play", "audience": 31}
    test_plays = {"invaild-play": {"name": "Invaild Play", "type": "invaild-type"}}
    with pytest.raises(ValueError) as e:
      Performances([test_performance], test_plays)
    assert e.value.args == ("Invalid performance type:", "invaild-type")