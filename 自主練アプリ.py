import streamlit as st
import datetime
import csv
import os

st.title("自主練チェック（日本時間）")

# ===== 日本時間を取得する関数 =====
def jst_today():
    JST = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(JST).date()

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

st.write(f"今日の日付：{jst_today()}")

# チェックボックス
checks = {}
for m in menus:
    checks[m] = st.checkbox(m)

# ===== 保存 =====
if st.button("保存"):
    today = jst_today()  # ← ★必ずここで取得（日本時間）

    file_name = "training_log.csv"
    file_exists = os.path.exists(file_name)

    with open(file_name, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["日付", "メニュー", "チェック"])

        for menu, checked in checks.items():
            writer.writerow([today, menu, checked])

    st.success(f"{today} の記録を保存しました！")
