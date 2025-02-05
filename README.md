# 悪用厳禁
本体
```
iris.py
```
# ダウンロード方法
1. 緑色「<> Code ∇」
2. 「Download ZIP」
# 環境構築
pipの仮想化
```
python3 -m venv .v
```
仮想環境起動
```
. ./.v/bin/activate
```
パッケージインストール
```
python3 -m pip install -r requirements.txt
```
# 結果
1. seto - vers 線形分離可能
2. seto - vrig 線形分離可能
3. vers - vrig 線形分離不可能

学習係数、重みを固定値で初期化しても結果は同じ

2024.07.04
2025.02.05 README.md 編集
