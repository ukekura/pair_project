import json

def load_json_files():
    # JSONファイルの読み込み
    with open("input/invoices.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
    
    return invoices, plays

# outputフォルダに請求書のテキストファイルを出力する関数
def output_invoice(content):
    # 出力ディレクトリの作成（存在しない場合）
    import os
    os.makedirs("output", exist_ok=True)
    
    # ファイルに出力
    with open("output/invoice.txt", "w", encoding="utf-8") as f:
        f.write(content)
    return print("請求書が正常に出力されました。")
