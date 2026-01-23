import streamlit as st
import pandas as pd
import os
from datetime import datetime

FILENAME = "jishuren_data.csv"

# ===============================
# CSV 安全読み込み
# ===============================
def load_data():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        return pd.DataFrame(columns=["日付", "内容"])

    try:
        df = pd.read_csv(FILENAME)
        if "日付" not in df.columns or "内容" not in df.columns:
            return pd.DataFrame(columns=["日付", "内容"])
        return df
    except:
        return pd.DataFrame(columns=["日付", "内容"])

# ===============================
# データ保存
# ===============================
def save_data(df):
    df.to_csv(FILENAME, index=False)

# ===============================
# UI
# ===============================
st.set_page_config(page_title="自主練チェック", layout="centered")
st.title("⚽ 自主練チェックアプリ")

df = load_data()

st.subheader("📌 今日の自主練")

menu = {
    "① 一回転ジャンプ": False,
    "② ボールコーディネーション": False,
    "③ ジンガ": False,
    "④ 三角ドリブル": False,
    "⑤ パンダ兄弟": False,
    "⑥ ダブルタッチ": False,
    "⑦ 左足": False,
    "⑧ ストレッチ": False,
    "⑨ 体幹": False,
    "⑩ その他": False
}

checked = []

for k in menu:
    if st.checkbox(k):
        checked.append(k)

note = st.text_input("✏️ メモ（任意）")

# ===============================
# 保存
# ===============================
if st.button("💾 記録する"):
    if checked:
        text = " / ".join(checked)
        if note:
            text += f"｜{note}"

        new = pd.DataFrame([{
            "日付": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "内容": text
        }])

        df = pd.concat([df, new], ignore_index=True)
        save_data(df)
        st.success("保存完了！")
        st.experimental_rerun()
    else:
        st.warning("最低1つはチェックしてね")

# ===============================
# 記録表示
# ===============================
st.subheader("📒 記録一覧")

df = load_data()

delete_indexes = []

for i, row in df.iterrows():
    col1, col2 = st.columns([0.15, 0.85])
    with col1:
        if st.checkbox("削除", key=f"del_{i}"):
            delete_indexes.append(i)
    with col2:
        st.write(f"{row['日付']}｜{row['内容']}")

# ===============================
# 個別削除
# ===============================
if st.button("🗑️ チェックした記録を削除"):
    if delete_indexes:
        df = df.drop(delete_indexes).reset_index(drop=True)
        save_data(df)
        st.success("削除完了")
        st.experimental_rerun()
    else:
        st.info("削除チェックがありません")

# ===============================
# 全消去
# ===============================
st.divider()
if st.button("🔥 全消去（完全リセット）"):
    pd.DataFrame(columns=["日付", "内容"]).to_csv(FILENAME, index=False)
    st.success("全削除完了")
    st.experimental_rerun()
