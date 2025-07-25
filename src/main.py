import json
import os
import sys

class Performances:
    def __init__(self, data, plays):
        self.performances = [self.__create_performance(performance, plays) for performance in data]

    def __create_performance(self, performance, plays):
        perf_type = plays[performance["playID"]]["type"]
        data = self._format_obj(performance, plays)
        if perf_type == "comedy":
            return Comedy(data)
        elif perf_type == "tragedy":
            return Tragedy(data)
        elif perf_type == "tragic-comedy":
            return TragicComedy(data)
        else:
            return Performance(data)

    def get_performances(self):
        return self.performances
    def _format_obj(self, performance, plays):
        return {"playID":performance["playID"], "audience":performance["audience"], "name":plays[performance["playID"]]["name"], "type":plays[performance["playID"]]["type"]}

    def calc_total_price(self):
        total_price = 0
        for performance in self.get_performances():
            total_price += performance.calc_price()
        return total_price
    
    def calc_total_point(self):
        total_point = 0
        for performance in self.get_performances():
            total_point += performance.calc_point()
        return total_point
    



class Performance:
    def __init__(self, data):
        self.name = data["name"]
        self.audience = data["audience"]
        self.type = data["type"]

    def get_name(self):
        return self.name
    def get_audience(self):
        return self.audience
    def get_type(self):
        return self.type
    
    def calc_price(self):
        if self.get_type() == "tragedy":
            price = 40000
            if self.get_audience() > 30:
                price += (self.get_audience() - 30) * 1000 
        
        if self.get_type() == "comedy":
            price = 30000 + self.get_audience() * 300
            if self.get_audience() > 20:
                price += (self.get_audience() - 20) * 500 + 10000
        
        if self.get_type() == "tragic-comedy":
            price = 35000 + self.get_audience() * 500
        
        return price
    
    def calc_point(self):
        point = 0
        if self.get_type() == "comedy":
            point = self.get_audience() // 5

        if self.get_type() == "tragic-comedy":
            if self.get_audience() > 20:
                point += min((self.get_audience() - 20), 10)
            
        if self.get_audience() > 30:
            point += (self.get_audience() - 30)
        return point


class Comedy(Performance):
    pass

class Tragedy(Performance):
    pass

class TragicComedy(Performance):
    pass

class Invoice:
    def __init__(self, data):
        self.performances = data["performances"]
        self.customer = data["customer"]
    def get_performances(self):
        return self.performances
    def get_customer(self):
        return self.customer
    
    def output_invoice_content(self):
        invoice_content = "請求書\n"
        invoice_content += self.get_customer() + "\n"
        
        for performance in self.get_performances().get_performances():
            invoice_content += "・" + performance.get_name() + "（観客数：" + str(performance.get_audience()) + "人、金額：$"+ str(performance.calc_price()) + "）\n"

        invoice_content += "合計金額：$" + str(self.get_performances().calc_total_price()) +  "\n"
        invoice_content += "獲得ポイント：" + str(self.get_performances().calc_total_point()) + "pt"

        return invoice_content
    
    def output_html_invoice_content(self):
        invoice_content = "<h1>請求書</h1>"
        invoice_content += "<h2>" + self.get_customer() + "</h2>"
        invoice_content += "<ul>"
        
        for performance in self.get_performances().get_performances():
            invoice_content += "<li>" + performance.get_name() + "（観客数：" + str(performance.get_audience()) + "人、金額：$"+ str(performance.calc_price()) + "）</li>"

        invoice_content += "</ul>"
        invoice_content += "<p>合計金額：$" + str(self.get_performances().calc_total_price()) +  "</p>"
        invoice_content += "<p>獲得ポイント：" + str(self.get_performances().calc_total_point()) + "pt</p>"

        return invoice_content


def load_json():
   with open("input/invoices.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
   with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
   return invoices, plays

def main():
    invoices, plays = load_json()

    invoice = Invoice({
        "performances": Performances(invoices[0]["performances"], plays),
        "customer": invoices[0]["customer"]
    })
    
    
    # 出力ディレクトリの作成（存在しない場合）
    os.makedirs("output", exist_ok=True)
    
    args = sys.argv

    # ファイルに出力
    if len(args) == 2:
        if args[1] == "text":
            invoice_content = invoice.output_invoice_content()

            with open("output/invoice.txt", "w", encoding="utf-8") as f:
                f.write(invoice_content)
            print("請求書が.txtで出力されました。")
    
        elif args[1] == "html":
            invoice_content = invoice.output_html_invoice_content()

            with open("output/invoice.html", "w", encoding="utf-8") as f:
                f.write(invoice_content)
            print("請求書が.htmlで出力されました。")
        else:
            print("textかhtmlを入力してください。")
    else:
        print("引数をひとつだけ入力してください。")

    
if __name__ == "__main__":
    main()
