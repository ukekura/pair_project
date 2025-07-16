import copy
import json
import os
import sys

class Performance:
    def __init__(self, data):
        self.data = data
        self.type = data["type"]
        self.audience = data["audience"]

    def get_performance(self):
        return self.data
    
    def get_type(self):
        return self.type

    def get_audience(self):
        return self.audience
    
    def get_name(self):
        return self.data["name"]

    def tragedy_price(self):
        price = 40000
        if self.audience > 30:
            price += (self.audience - 30) * 1000 
        return price
    
    def comedy_price(self):
        price = 30000 + self.audience * 300
        if self.audience > 20:
            price += (self.audience - 20) * 500 + 10000
        return price
    
    def comedy_point(self):
        point = self.audience // 5
        return point

    def common_point(self):
        point = (self.audience - 30)
        return point
    
    def price(self):
        if self.get_type() == "tragedy":
            price = self.tragedy_price()
        if self.get_type() == "comedy":
            price = self.comedy_price()
        return price
    
    def point(self):
        point = 0
        if self.get_type() == "comedy":
            point += self.comedy_point()
        if self.get_audience()  > 30:
            point += self.common_point()
        return point

class Performances:
    def __init__(self, invoice_data):
        self.performances = invoice_data["performances"]

    def get_performances(self):
        result = []
        for performance in self.performances:
            performance_instance = Performance(performance)
            result.append(performance_instance)
        return result
    
    def integrate(self, plays):
        for performance in self.performances:
            performance["type"] = plays[performance["playID"]]["type"]
            performance["name"] = plays[performance["playID"]]["name"]

    def total_price(self):
        total_price = 0
        for performance in self.get_performances():
            total_price += performance.price()
        return total_price

    def total_point(self):
        total_point = 0
        for performance in self.get_performances():
            total_point += performance.point()
        return total_point

class Invoice:
    def __init__(self, customer, performances):
        self.__customer = customer
        self.__performances = performances

    def customrer(self):
        return self.__customer
    
    def performances(self):
        return self.__performances

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
    
    invoices = format_invoices(invoices)
    invoice_data = deep_copy(invoices)
    return invoice_data

# Invoiceクラスがあってもよさそう
# そしてら以下２つの関数はInvoiceクラスの責務としてメソッドであるべき？
def format_invoice_content(customer, performances, invoice):
    invoice_content = "請求書\n"
    invoice_content += customer + "\n"
    for performance in performances.get_performances():
        invoice_content = invoice_content + "・" + performance.get_name() + "（観客数：" + str(performance.get_audience()) + "人、金額：$"+ str(performance.price()) + "）\n"
    invoice_content += "合計金額：$" + str(performances.total_price()) +  "\n"
    invoice_content += "獲得ポイント：" + str(performances.total_point()) + "pt"
    return invoice_content

def format_to_html(invoice_data, performances):
    invoice_content = "<h1>請求書</h1>"
    invoice_content += "<h2>" + invoice_data["customer"] + "</h2>"
    invoice_content += "<ul>"
    for performance in performances.get_performances():
        invoice_content = invoice_content + "<li>" + performance.get_name() + "（観客数：" + str(performance.get_audience()) + "人、金額：$"+ str(performance.price()) + "）</li>"
    invoice_content += "</ul>"
    invoice_content += "<p>" + "合計金額：$" + str(performances.total_price()) +  "</p>"
    invoice_content += "<p>" + "獲得ポイント：" + str(performances.total_point()) + "pt</p>"
    return invoice_content

def main():
    args = sys.argv

    invoices, plays = load_json()
    invoice_data = preperate_invoice_data(invoices, plays)

    performances = Performances(invoice_data)
    performances.integrate(plays)
    
    invoice = Invoice(invoice_data["customer"], performances)

    invoice_content = format_invoice_content(invoice_data["customer"], performances, invoice)
    html_invoice_content = format_to_html(invoice_data, performances)

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
