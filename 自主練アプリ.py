import streamlit as st
import datetime
import csv
import os

st.title("自主練チェック")

# ===== メニュー =====
menus = [
    "一回転ジャンプ",
    "ボールコーディネーション",
    "ジンガ",
    "三角ドリブル",
    "パンダ兄弟",
    "ダブルタッチ",
    "ストレッチ",
    "体幹",
    "その他"
]

st.write("今日の自主練をチェックしよう")

# チェックボックス保存用
checks = {}

for m in menus:
    checks[m] = st.checkbox(m)

# ===== 保存ボタン =====
if st.button("保存"):
    today = datetime.date.today()  # ← ★ここで今日の日付を取る

    file_name = "training_log.csv"
    file_exists = os.path.exists(file_name)

    with open(file_name, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # 初回だけヘッダーを書く
        if not file_exists:
            writer.writerow(["日付", "メニュー", "チェック"])

        for menu, checked in checks.items():
            writer.writerow([today, menu, checked])

    st.success(f"{today} の記録を保存しました！")
