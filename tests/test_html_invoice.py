import json
from src.main import main
import sys
import os

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

def cleanup_output_dir():
    """outputディレクトリ内のファイルをすべて削除"""
    output_dir = "output"
    for filename in os.listdir(output_dir):
        file_path = os.path.join(output_dir, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

# TestCase No.1
def test_testcase_1(mocker):
    """悲劇の観客数が「悲劇金額変化観客数」未満であるとき、金額は基本料金のみである。"""
    cleanup_output_dir()  # ここでクリーンアップ
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_1.json"))
    mocker.patch.object(sys, "argv", ["src/main.py", "html"])
    main()

    # outputディレクトリにinvoice.html以外のファイルがないことを確認
    output_files = os.listdir("output")
    assert output_files == ["invoice.html"], f"outputディレクトリの内容: {output_files}"
    
    invoice = get_output_invoice()
    with open("tests/html_output_for_test/testcase_1.html", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected