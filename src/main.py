import copy
import json
import os

def load_json():
   with open("input/INVOICES.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
   with open("input/PLAYS.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
   return invoices, plays

def output_text(invoice_content):
    os.makedirs("output", exist_ok=True)
    with open("output/invoice.txt", "w", encoding="utf-8") as f:
        f.write(invoice_content)
    print("請求書が正常に出力されました。")

def main():
    def preperate_invoice_data(invoices, plays):
        def format_invoice_data(invoices):
            invoices = invoices[0]
            return invoices
        
        def deep_copy(arg):
            result = copy.deepcopy(arg)
            return result
        
        def integrate(invoice_data, plays):
            for performance in invoice_data["performances"]:
                performance["type"] = plays[performance["playID"]].get("type")
                performance["name"] = plays[performance["playID"]]["name"]
            return invoice_data
        
        invoices = format_invoice_data(invoices)
        invoice_data = deep_copy(invoices)
        integrated_invoice_data = integrate(invoice_data, plays)

        return integrated_invoice_data
    
    
    def create_invoice_content(invoice_data):
        def calc_invoice_data(invoice_data):
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

            return invoice_data

        def format_invoice_content(invoice_material):
            invoice_content = "請求書\n"
            invoice_content += invoice_data["customer"] + "\n"
            for performance in invoice_data["performances"]:
                invoice_content = invoice_content + "・" + performance["name"] + "（観客数：" + str(performance["audience"]) + "人、金額：$"+ str(performance["price"]) + "）\n"
            invoice_content += "合計金額：$" + str(invoice_data["total_price"]) +  "\n"
            invoice_content += "獲得ポイント：" + str(invoice_data["total_point"]) + "pt"

            return invoice_content
        
        invoice_material = calc_invoice_data(invoice_data)
        invoice_content = format_invoice_content(invoice_material)

        return invoice_content

    invoices, plays = load_json()
    invoice_data = preperate_invoice_data(invoices, plays)
    invoice_content = create_invoice_content(invoice_data)
    output_text(invoice_content)

if __name__ == "__main__":
    main()