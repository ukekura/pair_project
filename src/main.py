import json
import os

def main():
    with open("input/invoices.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)

    invoice_content = "請求書\n"

    invoice_content += invoices[0]["customer"] + "\n"

    print(invoices[0]["performances"])
    print(invoices[0]["performances"][0]["playID"])

    for performance in invoices[0]["performances"][0].get("playID"):
        print("for-------------------", performance)

    for i in range(len(invoices[0]["performances"])):
        print(invoices[0]["performances"][i]["playID"])

    for perfomance in invoices[0]["performances"]:
        print(perfomance["playID"])

    total_price = "1000"
    total_point = "2000"

    invoice_content += "合計金額：$" + total_price +  "\n"
    invoice_content += "獲得ポイント：" + total_point + "pt"

    # 出力ディレクトリの作成（存在しない場合）
    os.makedirs("output", exist_ok=True)
    
    # ファイルに出力
    with open("output/invoice.txt", "w", encoding="utf-8") as f:
        f.write(invoice_content)
    
    print("請求書が正常に出力されました。")

if __name__ == "__main__":
    main()
