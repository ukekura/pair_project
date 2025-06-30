import json
import os

def load_json():
   with open("input/invoices.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
   with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
   return invoices, plays

def output_text(invoice_content):
    os.makedirs("output", exist_ok=True)
    with open("output/invoice.txt", "w", encoding="utf-8") as f:
        f.write(invoice_content)
    print("請求書が正常に出力されました。")

def main():
    def calc_price_point(invoices, plays):
        total_price = 0
        total_point = 0

        for performance in invoices["performances"]:

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

            total_price += price

        invocie_contenta = "請求書\n"
        invocie_contenta += invoices["customer"] + "\n"

        for performance in invoices["performances"]:

            if plays[performance["playID"]].get("type") == "tragedy":
                price = 40000
                if performance["audience"] > 30:
                    price += (performance["audience"] - 30) * 1000 

            if plays[performance["playID"]].get("type") == "comedy":
                price = 30000 + performance["audience"] * 300
                if performance["audience"] > 20:
                    price += (performance["audience"] - 20) * 500 + 10000

            invocie_contenta = invocie_contenta + "・" + plays[performance["playID"]]["name"] + "（観客数：" + str(performance["audience"]) + "人、金額：$"+ str(price) + "）\n"
        
        return invocie_contenta, total_price, total_point

    def add_total_price_point(invoice_content):
        invoice_content += "合計金額：$" + str(total_price) +  "\n"
        invoice_content += "獲得ポイント：" + str(total_point) + "pt"
        return invoice_content

    def format_invoice_data(invoices):
        invoices = invoices[0]
        return invoices
    
    invoices, plays = load_json()
    invoices = format_invoice_data(invoices)
    invoice_content, total_price, total_point = calc_price_point(invoices, plays)
    invoice_content = add_total_price_point(invoice_content)
    output_text(invoice_content)

if __name__ == "__main__":
    main()
