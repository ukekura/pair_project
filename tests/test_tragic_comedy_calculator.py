from src.main import TragicComedyCalculator

class TestPrice:
    def test_1(self):
        tragic_comedy_calculator = TragicComedyCalculator(25)
        result = tragic_comedy_calculator.price()
        expected = 47500
        assert result == expected

class TestPoint:
    def test_1(self):
        tragic_comedy_calculator = TragicComedyCalculator(25)
        result = tragic_comedy_calculator.point()
        expected = 5
        assert result == expected

    def test_2(self):
        tragic_comedy_calculator = TragicComedyCalculator(50)
        result = tragic_comedy_calculator.point()
        expected = 30
        assert result == expected

    def test_3(self):
        tragic_comedy_calculator = TragicComedyCalculator(5)
        result = tragic_comedy_calculator.point()
        expected = 0
        assert result == expected