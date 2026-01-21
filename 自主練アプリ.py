import streamlit as st
import datetime
import pandas as pd
import os

st.title("自主練チェック")

# 日本時間
def jst_today():
    JST = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(JST).date()

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

today = jst_today()
st.write(f"📅 今日：{today}")

checks = {}
for m in menus:
    checks[m] = st.checkbox(m)

FILE = "training_log.csv"

# 保存
if st.button("保存"):
    rows = []
    for m, c in checks.items():
        rows.append([str(today), m, c])

    df_new = pd.DataFrame(rows, columns=["日付", "メニュー", "チェック"])

    if os.path.exists(FILE):
        df_old = pd.read_csv(FILE)
        df = pd.concat([df_old, df_new])
    else:
        df = df_new

    df.to_csv(FILE, index=False)
    st.success("保存しました！")

# 一覧表示
if os.path.exists(FILE):
    df = pd.read_csv(FILE)
    st.subheader("📊 記録一覧")
    st.dataframe(df)

    # ダウンロード
    st.download_button(
        label="⬇ CSVをダウンロード",
        data=df.to_csv(index=False),
        file_name="自主練記録.csv",
        mime="text/csv"
    )

# restart

