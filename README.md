# 請求書出力システム

## 概要
このシステムは、JSONファイルから請求書データを読み込み、請求書を出力する機能を提供します。

## 開発ガイドライン
- src/invoice_generator.pyのみを編集してください。
- その他のディレクトリ構造やファイル名は変更しないでください

## プロジェクト構成
project/
├── input/
│ ├── input1.json # 請求書データ
│ └── input2.json # 設定データ
├── output/
│ └── invoice.txt # 生成された請求書ファイル
├── src/
│ └── invoice_generator.py # 請求書情報の生成
│ └── main.py # メイン処理
│ └── utils.py # データの入出力
└── tests/
└── test_output_invoice.py # テストコード

## 必要条件
- Python 3.11以上
- pytest

## セットアップ方法
1. リポジトリをクローン
```bash
git clone [リポジトリURL]
cd pair_project
```

2. 仮想環境の作成と有効化
```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化（Windows）
venv\Scripts\activate

# 仮想環境の有効化（Mac/Linux）
source venv/bin/activate
```

3. 必要なパッケージのインストール
```bash
pip install -e .
pip install pytest
```

## 使用方法
1. 入力JSONファイルを`input/`ディレクトリに配置
2. 以下のコマンドでプログラムを実行
```bash
python src/main.py
```
3. 生成された請求書は`output/invoice.txt`に出力されます

## テストの実行
```bash
pytest
```

## 入力JSONファイルの形式
### input1.json（請求書データ）
```json
{
    // 請求書データの形式を記載
}
```

### input2.json（設定データ）
```json
{
    // 設定データの形式を記載
}
```

## 注意事項
- 入力JSONファイルは必ず指定された形式に従ってください
- ファイル名は変更しないでください

## ライセンス
[ライセンス情報を記載]

## 作者
[作者情報を記載]

