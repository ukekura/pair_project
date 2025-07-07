import json
import os

class Performances:
    def __init__(self, data, plays):
        self.data = data
        self.performances = [Performance(performance, plays) for performance in self.data[0]["performances"]]
    def get_performances(self):
        return self.performances
    def set_performances(self, arg):
        self.data[0]["performances"] = arg
    
class Performance:
    def __init__(self, data, plays):
        self.data = data
        self.play_id = data["playID"]
        self.name = plays[self.get_play_id()]["name"]
        self.audience = data["audience"]
        self.type = plays[self.get_play_id()]["type"]

    def get_performance(self):
        return self.data
    def get_play_id(self):
        return self.play_id
    def get_name(self):
        return self.name
    def get_audience(self):
        return self.audience
    def get_type(self):
        return self.type

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

    total_price = 0
    total_point = 0

    def calc_price(performance):
        if plays[performance["playID"]].get("type") == "tragedy":
            price = 40000
            if performance["audience"] > 30:
                price += (performance["audience"] - 30) * 1000 
        
        if plays[performance["playID"]].get("type") == "comedy":
            price = 30000 + performance["audience"] * 300
            if performance["audience"] > 20:
                price += (performance["audience"] - 20) * 500 + 10000
        
        return price


    performances = Performances(invoices, plays)

    for performance in performances.get_performances():
        price = calc_price(performance.get_performance())
        invoice_content += "・" + performance.get_name() + "（観客数：" + str(performance.get_audience()) + "人、金額：$"+ str(price) + "）\n"

    for performance in performances.get_performances():
        price = calc_price(performance.get_performance())
        total_price += price


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
