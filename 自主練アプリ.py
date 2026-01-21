import streamlit as st
import datetime
import pandas as pd
import os

# =====================
# 日本時間の今日
# =====================
def jst_today():
    JST = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(JST).date()

# =====================
# 設定
# =====================
st.set_page_config(
    page_title="自主練チェック",
    page_icon="⚽",
    layout="centered"
)

st.markdown("## ⚽ 自主練チェック")
st.markdown("---")

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

# =====================
# チェック欄（2列）
# =====================
col1, col2 = st.columns(2)
checks = {}

for i, m in enumerate(menus):
    if i % 2 == 0:
        checks[m] = col1.checkbox(m)
    else:
        checks[m] = col2.checkbox(m)

# =====================
# 保存
# =====================
file = "records.csv"

if st.button("💾 保存する"):
    done = [k for k, v in checks.items() if v]
    count = len(done)

    row = {
        "日付": today,
        "実施数": count,
        "内容": "、".join(done)
    }

    if os.path.exists(file):
        df = pd.read_csv(file)
        df = pd.concat([pd.DataFrame([row]), df], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_csv(file, index=False)
    st.success("保存しました！")

st.markdown("---")

# =====================
# 記録一覧
# =====================
st.subheader("📋 記録一覧")

if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df, use_container_width=True)
else:
    st.write("まだ記録がありません")
