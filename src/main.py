import copy
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
    
    def add_price_point_to(INVOICES):

        for performance in INVOICES["performances"]:
            price = check_type_calc_price(performance)
            performance["price"] = price

        for performance in INVOICES["performances"]:
            performance["point"] = 0
            performance["point"] = check_type_calc_point(performance)

        return INVOICES["performances"]
    
    def amount_price(new_mid_data):
        total_price = 0
        for performance in new_mid_data:
            total_price += performance["price"]
        return total_price
        
    def amount_point(new_mid_data):
        total_point = 0
        for performance in new_mid_data:
            total_point += performance["point"]
        return total_point

    def create_invoice_content_from(invoice_data, total_price, total_point):
        invoice_content = "請求書\n"
        invoice_content += invoice_data["customer"] + "\n"
        for performance in new_mid_data:
            invoice_content = invoice_content + "・" + PLAYS[performance["playID"]]["name"] + "（観客数：" + str(performance["audience"]) + "人、金額：$"+ str(performance["price"]) + "）\n"
        invoice_content += "合計金額：$" + str(total_price) +  "\n"
        invoice_content += "獲得ポイント：" + str(total_point) + "pt"
        return invoice_content
    
    invoices, PLAYS = load_json()
    INVOICES = format_invoice_data(invoices)

    def deep_copy(arg):
        result = copy.deepcopy(arg)
        return result

    invoice_data = deep_copy(INVOICES)

    for performance in invoice_data["performances"]:
        price = check_type_calc_price(performance)
        performance["price"] = price

    for performance in invoice_data["performances"]:
        performance["point"] = 0
        performance["point"] = check_type_calc_point(performance)

    new_mid_data = invoice_data["performances"]

    total_price = 0
    for performance in invoice_data["performances"]:
        total_price += performance["price"]

    total_point = 0
    for performance in invoice_data["performances"]:
        total_point += performance["point"]
    
    invoice_content = create_invoice_content_from(invoice_data, total_price, total_point)
    
    output_text(invoice_content)

if __name__ == "__main__":
    main()