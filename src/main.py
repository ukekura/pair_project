import json
import os

def main():
    with open("input/invoices.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)


    invoice_content = "請求書\n"

    invoice_content += invoices[0]["customer"] + "\n"

    total_price = 0
    total_point = 0

    for performance in invoices[0]["performances"]:

        if plays[performance["playID"]].get("type") == "tragedy":
            price = 40000
            if performance["audience"] > 30:
                price += (performance["audience"] - 30) * 1000 
        
        if plays[performance["playID"]].get("type") == "comedy":
            price = 30000 + performance["audience"] * 300
            if performance["audience"] > 20:
                price += (performance["audience"] - 20) * 500 + 10000             
            total_point += performance["audience"] // 5

        if performance["audience"]  > 30:
            total_point += (performance["audience"] - 30)

        invoice_content += "・" + plays[performance["playID"]]["name"] + "（観客数：" + str(performance["audience"]) + "人、金額：$"+ str(price) + "）\n"

        total_price += price

    invoice_content += "合計金額：$" + str(total_price) +  "\n"
    invoice_content += "獲得ポイント：" + str(total_point) + "pt"

    # 出力ディレクトリの作成（存在しない場合）
    os.makedirs("output", exist_ok=True)
    
    # ファイルに出力
    with open("output/invoice.txt", "w", encoding="utf-8") as f:
        f.write(invoice_content)
    
    print("請求書が正常に出力されました。")

if __name__ == "__main__":
    main()
