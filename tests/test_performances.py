from src.main import Performances

class TestTotalPrice:
    def test_1(self):
        performances = [{"audience": 25, "playID": "ukekura"}]
        plays = {"ukekura":{"type": "comedy", "name": "ukekura_takuma"}}
        performances_instance = Performances(performances, plays)
        result = performances_instance.total_price()
        expected = 50000
        assert result == expected

    def test_2(self):
        performances = [{"audience": 25, "playID": "ukekura"}]
        plays = {"ukekura":{"type": "tragic_comedy", "name": "ukekura_takuma"}}
        performances_instance = Performances(performances, plays)
        result = performances_instance.total_price()
        expected = 47500
        assert result == expected

    def test_3(self):
        performances = [{"audience": 25, "playID": "ukekura"}]
        performances.append({"audience": 25, "playID": "ukekura_2"})
        plays = {"ukekura":{"type": "comedy", "name": "ukekura_takuma"}}
        plays["ukekura_2"] = {"type": "tragic_comedy", "name": "ukekura_takuma"}
        performances_instance = Performances(performances, plays)
        result = performances_instance.total_price()
        expected = 50000 + 47500
        assert result == expected