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
    
    invoices, PLAYS = load_json()
    INVOICES = format_invoice_data(invoices)

    def deep_copy(arg):
        result = copy.deepcopy(arg)
        return result

    invoice_data = deep_copy(INVOICES)
    
    for performance in invoice_data["performances"]:
        performance["type"] = PLAYS[performance["playID"]].get("type")
        performance["name"] = PLAYS[performance["playID"]]["name"]
    
    def create_invoice_content(invoice_data):

        for performance in invoice_data["performances"]:
            if performance["type"] == "tragedy":
                price = clac_tragedy_price(performance)
            if performance["type"] == "comedy":
                price = clac_comedy_price(performance)
            performance["price"] = price

        for performance in invoice_data["performances"]:
            performance["point"] = 0
            if performance["type"] == "comedy":
                point = performance["audience"] // 5
                performance["point"] += point
            if performance["audience"]  > 30:
                point = (performance["audience"] - 30)
                performance["point"] += point

        total_price = 0
        for performance in invoice_data["performances"]:
            total_price += performance["price"]
        invoice_data["total_price"] = total_price

        total_point = 0
        for performance in invoice_data["performances"]:
            total_point += performance["point"]
        invoice_data["total_point"] = total_point

        invoice_content = "請求書\n"
        invoice_content += invoice_data["customer"] + "\n"
        for performance in invoice_data["performances"]:
            invoice_content = invoice_content + "・" + performance["name"] + "（観客数：" + str(performance["audience"]) + "人、金額：$"+ str(performance["price"]) + "）\n"
        invoice_content += "合計金額：$" + str(invoice_data["total_price"]) +  "\n"
        invoice_content += "獲得ポイント：" + str(invoice_data["total_point"]) + "pt"
    
        return invoice_content

    invoice_content = create_invoice_content(invoice_data)
    output_text(invoice_content)

if __name__ == "__main__":
    main()