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

def preperate_invoice_data(invoices, plays):
    def format_invoices(invoices):
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
    
    invoices = format_invoices(invoices)
    invoice_data = deep_copy(invoices)
    integrated_invoice_data = integrate(invoice_data, plays)
    return integrated_invoice_data

def calc_invoice_data(invoice_data):
    def calc_price(invoice_data):
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
        return invoice_data
    
    def calc_point(invoice_data):
        for performance in invoice_data["performances"]:
            performance["point"] = 0
            if performance["type"] == "comedy":
                point = performance["audience"] // 5
                performance["point"] += point
            if performance["audience"]  > 30:
                point = (performance["audience"] - 30)
                performance["point"] += point
        return invoice_data
    
    def calc_total_price_point(invoice_data):
        def calc_total_price(invoice_data):
            total_price = 0
            for performance in invoice_data["performances"]:
                total_price += performance["price"]
            invoice_data["total_price"] = total_price
            return invoice_data
            
        def calc_total_point(invoice_data):
            total_point = 0
            for performance in invoice_data["performances"]:
                total_point += performance["point"]
            invoice_data["total_point"] = total_point
            return invoice_data
        
        invoice_data = calc_total_price(invoice_data)
        invoice_data = calc_total_point(invoice_data)
        
        return invoice_data
    
    invoice_data = calc_price(invoice_data)
    invoice_data = calc_point(invoice_data)
    invoice_data = calc_total_price_point(invoice_data)
    return invoice_data

def format_invoice_content(invoice_data):
    invoice_content = "請求書\n"
    invoice_content += invoice_data["customer"] + "\n"
    for performance in invoice_data["performances"]:
        invoice_content = invoice_content + "・" + performance["name"] + "（観客数：" + str(performance["audience"]) + "人、金額：$"+ str(performance["price"]) + "）\n"
    invoice_content += "合計金額：$" + str(invoice_data["total_price"]) +  "\n"
    invoice_content += "獲得ポイント：" + str(invoice_data["total_point"]) + "pt"
    return invoice_content

def format_to_html(invoice_data):
    invoice_content = "<h1>請求書</h1>"
    invoice_content += "<h2>" + invoice_data["customer"] + "</h2>"
    for performance in invoice_data["performances"]:
        invoice_content = invoice_content + "・" + performance["name"] + "（観客数：" + str(performance["audience"]) + "人、金額：$"+ str(performance["price"]) + "）\n"
    invoice_content += "合計金額：$" + str(invoice_data["total_price"]) +  "\n"
    invoice_content += "獲得ポイント：" + str(invoice_data["total_point"]) + "pt"
    return invoice_content

def main():

    

    invoices, plays = load_json()
    invoice_data = preperate_invoice_data(invoices, plays)
    print("========== invoice_data ==========\n", invoice_data, "\n")

    invoice_material = calc_invoice_data(invoice_data)
    print("========== invoice_material ==========\n", invoice_material)
    
    invoice_content = format_invoice_content(invoice_material)
    invoice_html_content = format_to_html(invoice_material)
    output_text(invoice_content)

    # ファイルに出力
    if len(args) == 2:
        if args[1] == "text":
            print("請求書がテキストファイルで出力されました")
            with open("output/invoice.txt", "w", encoding="utf-8") as f:
                f.write(invoice_content)
        elif args[1] == "html":
            print("請求書がHTMLファイルで出力されました")
            with open("output/invoice.html", "w", encoding="utf-8") as f:
                f.write(html_invoice_content)
        else:
            print("引数はtextかhtmlを入力してください")
            print("現在の入力：", args[1])
    else:
        print("引数をひとつだけ入力してください")

if __name__ == "__main__":
    main()