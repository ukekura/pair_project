import json
import os

class Performances:
    def __init__(self, data, plays):
        self.performances = [Performance(self._format_obj(performance, plays)) for performance in data[0]["performances"]]
    def get_performances(self):
        return self.performances
    def _format_obj(self, performance, plays):
        return {"playID":performance["playID"], "audience":performance["audience"], "name":plays[performance["playID"]]["name"], "type":plays[performance["playID"]]["type"]}
    
class Performance:
    def __init__(self, data):
        self.data = data
        self.name = data["name"]
        self.audience = data["audience"]
        self.type = data["type"]

    def get_performance(self):
        return self.data
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
        
        return price


def load_json():
   with open("input/invoices.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
   with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
   return invoices, plays

def main():
    invoices, plays = load_json()

    invoice_content = "請求書\n"

    invoice_content += invoices[0]["customer"] + "\n"

    total_point = 0


    performances = Performances(invoices, plays)

    for performance in performances.get_performances():
        invoice_content += "・" + performance.get_name() + "（観客数：" + str(performance.get_audience()) + "人、金額：$"+ str(performance.calc_price()) + "）\n"

    total_price = 0
    for performance in performances.get_performances():
        total_price += performance.calc_price()


    for performance in performances.get_performances():
        if performance.get_type() == "comedy":
            total_point += performance.get_audience() // 5

        if performance.get_audience() > 30:
            total_point += (performance.get_audience() - 30)



    invoice_content += "合計金額：$" + str(total_price) +  "\n"
    invoice_content += "獲得ポイント：" + str(total_point) + "pt"

    # 出力ディレクトリの作成（存在しない場合）
    os.makedirs("output", exist_ok=True)
    
    # ファイルに出力
    with open("output/invoice.txt", "w", encoding="utf-8") as f:
        f.write(invoice_content)
    
    print("請求書が正常に出力されました。")

if __name__ == "__main__":
    main()
