import json
from src.utils import load_json_files


def generate_invoice_content():
    # JSONファイルの読み込み
    invoices, plays = load_json_files()

### 実装範囲ここから

    invoice_content = "請求書\n"

    # JSONの内容をそのまま文字列に変換
    invoice_content += "invoices.jsonの内容:\n"
    invoice_content += json.dumps(invoices, ensure_ascii=False, indent=2)
    invoice_content += "\n\nplays.jsonの内容:\n"
    invoice_content += json.dumps(plays, ensure_ascii=False, indent=2)

### 実装範囲ここまで
    return invoice_content