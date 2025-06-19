import json
import os

def main():
    with open("input/invoices.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)

    invoice_content = "請求書\n"

    invoice_content += invoices[0]["customer"] + "\n"

    for performance in invoices[0]["performances"]:
        invoice_content += "・" + performance["playID"] + "（観客数：" + str(performance["audience"]) + "人）\n"

        print("plays:", plays[performance["playID"]].get("type"))
        if plays[performance["playID"]].get("type") == "tragedy":
            print("ifが実行された")
            price = 40000
            if performance["audience"] > 30:
                price += (performance["audience"] - 30) * 1000 

    print("price:", price)
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
