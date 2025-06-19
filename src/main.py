import json
import os

def main():
    with open("input/invoices.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)

    invoice_content = "請求書\n"

    # JSONの内容をそのまま文字列に変換
    invoice_content += "invoices.jsonの内容:\n"
    invoice_content += json.dumps(invoices, ensure_ascii=False, indent=2)
    invoice_content += "\n\nplays.jsonの内容:\n"
    invoice_content += json.dumps(plays, ensure_ascii=False, indent=2)

    # 出力ディレクトリの作成（存在しない場合）
    os.makedirs("output", exist_ok=True)
    
    # ファイルに出力
    with open("output/invoice.txt", "w", encoding="utf-8") as f:
        f.write(invoice_content)
    
    print("請求書が正常に出力されました。")

if __name__ == "__main__":
    main()
