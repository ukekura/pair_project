import json
import os

def load_json():
   with open("input/INVOICES.json", "r", encoding="utf-8") as f:
        INVOICES = json.load(f)
   with open("input/PLAYS.json", "r", encoding="utf-8") as f:
        PLAYS = json.load(f)
   return INVOICES, PLAYS

def output_text(invoice_content):
    os.makedirs("output", exist_ok=True)
    with open("output/invoice.txt", "w", encoding="utf-8") as f:
        f.write(invoice_content)
    print("請求書が正常に出力されました。")

def main():
    def format_invoice_data(INVOICES):
        INVOICES = INVOICES[0]
        return INVOICES
    
    def initialize_invoice_content():
        invocie_content = "請求書\n"
        invocie_content += INVOICES["customer"] + "\n"
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
        if PLAYS[performance["playID"]].get("type") == "tragedy":
            price = clac_tragedy_price(performance)
        if PLAYS[performance["playID"]].get("type") == "comedy":
            price = clac_comedy_price(performance)
        return price
    
    def check_type_calc_point(performance):
        if PLAYS[performance["playID"]].get("type") == "comedy":
            point = performance["audience"] // 5
            performance["point"] += point
        if performance["audience"]  > 30:
            point = (performance["audience"] - 30)
            performance["point"] += point
        return performance["point"]
    
    def add_price_key_to(INVOICES):
        mid_data = INVOICES["performances"]
        for performance in mid_data:
            price = check_type_calc_price(performance)
            performance["price"] = price
        return mid_data
    
    def add_point_key_value_to(mid_data):
        new_mid_data = mid_data
        for performance in new_mid_data:
            performance["point"] = 0
            performance["point"] = check_type_calc_point(performance)
        return new_mid_data

    def create_trade_content(invocie_contenta, mid_data):
        for performance in mid_data:
            invocie_contenta = invocie_contenta + "・" + PLAYS[performance["playID"]]["name"] + "（観客数：" + str(performance["audience"]) + "人、金額：$"+ str(performance["price"]) + "）\n"
        return invocie_contenta
    
    def finish_invoice_content(invoice_content, total_price, total_point):
        invoice_content += "合計金額：$" + str(total_price) +  "\n"
        invoice_content += "獲得ポイント：" + str(total_point) + "pt"
        return invoice_content


    invoices, PLAYS = load_json()
    INVOICES = format_invoice_data(invoices)
        
    mid_data = add_price_key_to(INVOICES)
    new_mid_data = add_point_key_value_to(mid_data)

    def amoutn_price(mid_data):
        total_price = 0
        for performance in mid_data:
            price = check_type_calc_price(performance)
            total_price += price
        return total_price
        
        
        
    def amount_point(new_mid_data):
        total_point = 0
        for performance in new_mid_data:
            total_point += performance["point"]
        return total_point

    total_price = amoutn_price(mid_data)
    total_point = amount_point(new_mid_data)

    invoice_content = initialize_invoice_content()
    invoice_content = create_trade_content(invoice_content, mid_data)
    invoice_content = finish_invoice_content(invoice_content, total_price, total_point)

    output_text(invoice_content)

if __name__ == "__main__":
    main()