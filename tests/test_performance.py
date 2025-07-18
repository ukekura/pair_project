from src.main import Performance

class TestPrice:
    def test_comedy(self):
        perforamnce = Performance({"audience": 25, "name": "ukekura", "type": "comedy"})
        result = perforamnce.price()
        expected = 50000
        assert result == expected

    def test_tragic_comedy(self):
        perforamnce = Performance({"audience": 25, "name": "ukekura", "type": "tragic_comedy"})
        result = perforamnce.price()
        expected = 47500
        assert result == expected