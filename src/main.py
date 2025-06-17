# 仮の請求書内容
default_content = """請求書
株式会社ビッグカンパニー
・Hamlet（観客数：55人、金額：〇〇円）
・As You Like It（観客数：35人、金額：△△円）
・Othello（観客数：40人、金額：□□円）
合計金額：××円
獲得ポイント：～pt
"""

def generate_invoice_content():
# 実装範囲ここから

    invoice_content = default_content

# 実装範囲ここまで
    return invoice_content

# outputフォルダに請求書のテキストファイルを出力する関数
def output_invoice(content):
    # 出力ディレクトリの作成（存在しない場合）
    import os
    os.makedirs("output", exist_ok=True)
    # 請求書の内容を生成（仮の内容）
    
    # ファイルに出力
    with open("output/invoice.txt", "w", encoding="utf-8") as f:
        f.write(invoice_content)
    return print("請求書が正常に出力されました。")



if __name__ == "__main__":
    invoice_content = generate_invoice_content()
    output_invoice(invoice_content)
