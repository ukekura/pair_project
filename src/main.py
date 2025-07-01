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
    def format_invoice_data(invoices):
        invoices = invoices[0]
        return invoices
    
    def initialize_invoice_content():
        invocie_content = "請求書\n"
        invocie_content += invoices["customer"] + "\n"
        return invocie_content
    
    def clac_tragedy_price(performance):
        price = 40000
        if performance["audience"] > 30:
            price += (performance["audience"] - 30) * 1000 
        return price
    
    def clac_comedy_price(performance):
        price = 30000 + performance["audience"] * 300
        if performance["audience"] > 20:
            price += (performance["audience"] - 20) * 500 + 10000
        return price
    
    def check_type_calc_price(performance):
        if plays[performance["playID"]].get("type") == "tragedy":
                price = clac_tragedy_price(performance)
        if plays[performance["playID"]].get("type") == "comedy":
            price = clac_comedy_price(performance)
        return price
    
    def calc_total_price_point(invoices, total_price, total_point):
        for performance in invoices["performances"]:
            price = check_type_calc_price(performance)
            total_price += price
            if plays[performance["playID"]].get("type") == "comedy":
                total_point += performance["audience"] // 5
            if performance["audience"]  > 30:
                total_point += (performance["audience"] - 30)
        return total_price, total_point
    
    def create_trade_content(invocie_contenta):
        for performance in invoices["performances"]:
            if plays[performance["playID"]].get("type") == "tragedy":
                price = clac_tragedy_price(performance)
            if plays[performance["playID"]].get("type") == "comedy":
                price = clac_comedy_price(performance)
            invocie_contenta = invocie_contenta + "・" + plays[performance["playID"]]["name"] + "（観客数：" + str(performance["audience"]) + "人、金額：$"+ str(price) + "）\n"
        return invocie_contenta
    
    def finish_invoice_content(invoice_content, total_price, total_point):
        invoice_content += "合計金額：$" + str(total_price) +  "\n"
        invoice_content += "獲得ポイント：" + str(total_point) + "pt"
        return invoice_content


    invoices, plays = load_json()
    invoices = format_invoice_data(invoices)

    total_price = 0
    total_point = 0

    invoice_content = initialize_invoice_content()

    invoice_content = create_trade_content(invoice_content)
    total_price, total_point = calc_total_price_point(invoices, total_price, total_point)
    
    invoice_content = finish_invoice_content(invoice_content, total_price, total_point)

    output_text(invoice_content)

if __name__ == "__main__":
    main()