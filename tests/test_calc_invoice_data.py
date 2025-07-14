from src.main import calc_invoice_data

class TestPrice:
    def test_price_on_aslike_21(self):
        invoice_data = {
            'customer': 'BigCo', 
            'performances': [{
                'playID': 'as-like', 
                'audience': 21, 
                'type': 'comedy', 
                'name': 'As You Like It'
            }]}
        result = calc_invoice_data(invoice_data)
        assert result["performances"][0]["price"] == 46800

class TestPoint:
    def test_point_on_aslike_31(self):
        invoice_data = {
            'customer': 'BigCo', 
            'performances': [{
                'playID': 'as-like', 
                'audience': 31, 
                'type': 'comedy', 
                'name': 'As You Like It'
            }]}
        result = calc_invoice_data(invoice_data)
        assert result["performances"][0]["point"] == 7

class TestTotalPrice:
    def test_total_price_case_1(self):
        invoice_data = {'customer': 'BigCo', 'performances': [
            {'playID': 'hamlet', 'audience': 55, 'type': 'tragedy', 'name': 'Hamlet'}, 
            {'playID': 'as-like', 'audience': 35, 'type': 'comedy', 'name': 'As You Like It'}, 
            {'playID': 'othello', 'audience': 40, 'type': 'tragedy', 'name': 'Othello'}]}
        result = calc_invoice_data(invoice_data)
        assert result["total_price"] == 173000

class TestTotalPoint:
    def test_total_point_case_1(self):
        invoice_data = {'customer': 'BigCo', 'performances': [
            {'playID': 'hamlet', 'audience': 55, 'type': 'tragedy', 'name': 'Hamlet'}, 
            {'playID': 'as-like', 'audience': 35, 'type': 'comedy', 'name': 'As You Like It'}, 
            {'playID': 'othello', 'audience': 40, 'type': 'tragedy', 'name': 'Othello'}]}
        result = calc_invoice_data(invoice_data)
        assert result["total_point"] == 47