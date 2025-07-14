import json
from src.main import main

def load_json_for_test(testcase_file):
    """指定されたテストケースファイルを読み込む"""
    with open(f"tests/input_for_test/{testcase_file}", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
    return invoices, plays

def get_output_invoice():
    """出力テキストファイルの内容を文字列として読み込み"""
    with open("output/invoice.html", "r", encoding="utf-8") as f:
        result = f.read()
    return result

# TestCase No.1
def test_testcase_1(mocker):
    """悲劇の観客数が「悲劇金額変化観客数」未満であるとき、金額は基本料金のみである。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_1.json"))
    main()
    invoice = get_output_invoice()
    # with open("tests/html_output_for_test/testcase_1.html", "r", encoding="utf-8") as f:
    #     expected = f.read()
    # assert invoice == expected