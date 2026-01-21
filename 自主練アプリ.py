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
# ページ設定（PC / スマホ対応）
# =====================
st.set_page_config(
    page_title="自主練チェック",
    page_icon="⚽",
    layout="centered"
)

# =====================
# スマホ向けスタイル
# =====================
st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    height: 3em;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# =====================
# タイトル
# =====================
st.markdown("## ⚽ 自主練チェック")
st.markdown("---")

# =====================
# メニュー
# =====================
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
# 表示モード管理（トグル）
# =====================
if "mobile" not in st.session_state:
    st.session_state["mobile"] = False

if st.session_state["mobile"]:
    if st.button("💻 パソコン表示に切り替え"):
        st.session_state["mobile"] = False
else:
    if st.button("📱 スマホ表示に切り替え"):
        st.session_state["mobile"] = True

st.markdown("---")

# =====================
# チェック欄
# =====================
checks = {}

if st.session_state["mobile"]:
    # スマホ：1列
    for m in menus:
        checks[m] = st.checkbox(m)
else:
    # パソコン：2列
    col1, col2 = st.columns(2)
    for i, m in enumerate(menus):
        if i % 2 == 0:
            checks[m] = col1.checkbox(m)
        else:
            checks[m] = col2.checkbox(m)

# =====================
# 保存処理
# =====================
file = "records.csv"

st.markdown("###")
if st.button("💾 保存する"):
    done = [k for k, v in checks.items() if v]

    row = {
        "日付": today,
        "実施数": len(done),
        "内容": "、".join(done)
    }

    if os.path.exists(file):
        df = pd.read_csv(file)
        df = pd.concat([pd.DataFrame([row]), df], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_csv(file, index=False)
    st.success("保存しました！")

# =====================
# 記録一覧
# =====================
st.markdown("---")
st.subheader("📋 記録一覧")

if os.path.exists(file):
    df = pd.read_csv(file)
    st.dataframe(df, use_container_width=True)
else:
    st.write("まだ記録がありません")

# =====================
# 削除（安全・確認つき）
# =====================
st.markdown("---")
st.subheader("🗑 記録の整理")

if os.path.exists(file):
    if st.checkbox("記録を削除したい（確認）"):
        if st.button("⚠ 全記録を削除する"):
            os.remove(file)
            st.success("記録をすべて削除しました")
