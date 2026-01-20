import streamlit as st
import datetime
import csv

st.set_page_config(page_title="自主練チェック")

st.title("⚽ 自主練チェック")

today = datetime.date.today().strftime("%Y/%m/%d")
st.write(f"📅 {today} の記録")

menu = [
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

checked = 0

for item in menu:
    if st.checkbox(item):
        checked += 1

if st.button("記録する"):
    total = len(menu)
    percent = int((checked / total) * 100)

    st.success(f"達成：{checked}/{total}　達成率：{percent}%")

    with open("training_log.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([today, checked, total, f"{percent}%"])

    st.info("保存しました！")
