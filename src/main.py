import copy
import json
import os
import sys

class Performance:
    def __init__(self, data):
        self.__audience = data["audience"]
        self.__name = data["name"]
        self.__calculator = self.create_calculator(data["type"])

    def audience(self):
        return self.__audience
    
    def name(self):
        return self.__name

    def price(self):
        return self.__calculator.price()
    
    def point(self):
        return self.__calculator.point()
    
    def create_calculator(self, parf_type):
        if parf_type == "tragedy":
            return TragedyCalculator(self.audience())
        if parf_type == "comedy":
            return ComedyCalculator(self.audience())
        
class Calculator:
    def __init__(self, audience):
        self._audience = audience

    def price(self):
        raise '子の責務'
    
    def point(self):
        point = 0
        if self._audience  > 30:
            point +=  (self._audience - 30)
        return point
    
class TragedyCalculator(Calculator):
    def __init__(self, audience):
        self._audience = audience

    def price(self):
        price = 40000
        if self._audience > 30:
            price += (self._audience - 30) * 1000 
        return price

class ComedyCalculator(Calculator):
    def __init__(self, audience):
        self._audience = audience

    def price(self):
        price = 30000 + self._audience * 300
        if self._audience > 20:
            price += (self._audience - 20) * 500 + 10000
        return price
    
    def point(self):
        point = 0
        point += self._audience // 5
        if self._audience  > 30:
            point +=  (self._audience - 30)
        return point
    
class Performances:
    def __init__(self, performances, plays):
        self.__performances = self.__create_performances(performances, plays)

    def __create_performances(self, performances, plays):
        result = []
        for performance in performances:
            performance["type"] = plays[performance["playID"]]["type"]
            performance["name"] = plays[performance["playID"]]["name"]
            performance_instance = Performance(performance)
            result.append(performance_instance)
        return result

    def get_performances(self):
        return self.__performances

    def total_price(self):
        total_price = 0
        for performance in self.__performances:
            total_price += performance.price()
        return total_price

    def total_point(self):
        total_point = 0
        for performance in self.__performances:
            total_point += performance.point()
        return total_point

class Invoice:
    def __init__(self, invoice_data, plays):
        self.__customer = invoice_data["customer"]
        self.__performances = Performances(invoice_data["performances"], plays)

    def customer(self):
        return self.__customer
    
    def performances(self):
        return self.__performances
    
    def get_performances_iterator(self):
        return self.__performances.get_performances()
    
    def calc_performances_total_price(self):
        return self.__performances.total_price()
    
    def calc_performances_total_point(self):
        return self.__performances.total_point()
    
class InvoiceFormatter:
    def __init__(self, invoice):
        self.__invoice = invoice

    def to_text(self):
        invoice_content = "請求書\n"
        invoice_content += self.__invoice.customer() + "\n"
        invoice_content = self.__make_text_performance_area(invoice_content, self.__invoice.performances())
        
        return invoice_content
    
    def __make_text_performance_area(self, invoice_content, performances):
        for performance in performances.get_performances():
            invoice_content = invoice_content + "・" + performance.name() + "（観客数：" + str(performance.audience()) + "人、金額：$"+ str(performance.price()) + "）\n"
        invoice_content += "合計金額：$" + str(performances.total_price()) +  "\n"
        invoice_content += "獲得ポイント：" + str(performances.total_point()) + "pt"
        return invoice_content

    def to_html(self):
        invoice_content = "<h1>請求書</h1>"
        invoice_content += "<h2>" + self.__invoice.customer() + "</h2>"
        invoice_content += "<ul>"
        for performance in self.__invoice.get_performances_iterator():
            invoice_content = invoice_content + "<li>" + performance.name() + "（観客数：" + str(performance.audience()) + "人、金額：$"+ str(performance.price()) + "）</li>"
        invoice_content += "</ul>"
        invoice_content += "<p>" + "合計金額：$" + str(self.__invoice.calc_performances_total_price()) +  "</p>"
        invoice_content += "<p>" + "獲得ポイント：" + str(self.__invoice.calc_performances_total_point()) + "pt</p>"
        return invoice_content


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

def preperate_invoice_data(invoices):
    def format_invoices(invoices):
        invoices = invoices[0]
        return invoices
    
    def deep_copy(arg):
        result = copy.deepcopy(arg)
        return result
    
    invoices = format_invoices(invoices)
    invoice_data = deep_copy(invoices)
    return invoice_data

def main():
    args = sys.argv

    invoices, plays = load_json()
    invoice_data = preperate_invoice_data(invoices)

    invoice = Invoice(invoice_data, plays)
    
    if len(args) == 2:
        if args[1] == "text":
            print("請求書がテキストファイルで出力されました")
            with open("output/invoice.txt", "w", encoding="utf-8") as f:
                f.write(InvoiceFormatter(invoice).to_text())
        elif args[1] == "html":
            print("請求書がHTMLファイルで出力されました")
            with open("output/invoice.html", "w", encoding="utf-8") as f:
                f.write(InvoiceFormatter(invoice).to_html())
        else:
            print("引数はtextかhtmlを入力してください")
            print("現在の入力：", args[1])
    else:
        print("引数をひとつだけ入力してください")

    # tragedy_calculator = TragedyCalculator(30)
    # print("audience-------------", tragedy_calculator._audience)

    # for performance in performances.get_performances():
    #     print("performance.audience-----------------", performance.audience())

if __name__ == "__main__":
    main()
