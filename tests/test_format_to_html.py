from src.main import format_to_html

class TestFormat:
    def test_format_case_1(self):
        invoice_material =  {'customer': 'BigCo', 'performances': [
            {'playID': 'hamlet', 'audience': 55, 'type': 'tragedy', 'name': 'Hamlet', 'price': 65000, 'point': 25}, 
            {'playID': 'as-like', 'audience': 35, 'type': 'comedy', 'name': 'As You Like It', 'price': 58000, 'point': 12}, 
            {'playID': 'othello', 'audience': 40, 'type': 'tragedy', 'name': 'Othello', 'price': 50000, 'point': 10}], 
            'total_price': 173000, 'total_point': 47}
        result = format_to_html(invoice_material)
        assert "<h2>" + invoice_material["customer"] + "</h2>" in result 

    def test_html_title(self):
        invoice_material =  {'customer': 'BigCo', 'performances': [
            {'playID': 'hamlet', 'audience': 55, 'type': 'tragedy', 'name': 'Hamlet', 'price': 65000, 'point': 25}, 
            {'playID': 'as-like', 'audience': 35, 'type': 'comedy', 'name': 'As You Like It', 'price': 58000, 'point': 12}, 
            {'playID': 'othello', 'audience': 40, 'type': 'tragedy', 'name': 'Othello', 'price': 50000, 'point': 10}], 
            'total_price': 173000, 'total_point': 47}
        result = format_to_html(invoice_material)
        assert "<h1>" + "請求書" + "</h1>" in result 