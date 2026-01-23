import streamlit as st
from datetime import date
import csv
import os
import pandas as pd

st.set_page_config(page_title="自主練チェック", layout="wide")
st.title("自主練チェック")

FILENAME = "自主練記録.csv"

# =====================
# セッション初期化
# =====================
def init(key, value=False):
    if key not in st.session_state:
        st.session_state[key] = value

init("delete_mode", False)
init("confirm_all_delete", False)

# =====================
# メニュー定義
# =====================
ball_items = [
    "軸足通し","軸足通し（後ろ向き）",
    "アウトプッシュ","アウトプッシュ（後ろ向き）",
    "プルプッシュ","プルプッシュ（後ろ向き）",
    "足裏シザース","足裏シザース（後ろ向き）",
    "インシザース","インシザース（後ろ向き）",
    "インイン・アウト","インイン・アウト（後ろ向き）",
    "インインロール","インインロール（後ろ向き）",
    "連続エラシコ","連続エラシコ（後ろ向き）",
    "アウト→クライフターン",
    "足裏転がし合うターン",
    "ディープジンガ","ディープジンガ（後ろ向き）",
    "覗き込みドリブル",
    "ダブルタッチ空振り"
]

stretch_items = [
    "もも（裏・表）",
    "ふくらはぎ",
    "開脚",
    "開脚（左右）",
    "長座前屈",
    "前屈"
]

for i in ball_items:
    init("ball_" + i)
for s in stretch_items:
    init("stretch_" + s)

checked = []

# =====================
# チェック入力
# =====================
if st.checkbox("① 一回転ジャンプ"):
    checked.append("一回転ジャンプ")

# ---- ② ボールコーディネーション
ball_all = st.checkbox("② ボールコーディネーション（全部やった）")
if ball_all:
    for i in ball_items:
        st.session_state["ball_" + i] = True

with st.expander("▼ ボールコーディネーション"):
    for i in ball_items:
        if st.checkbox(i, key="ball_" + i):
            checked.append(i)

# ---- ③〜⑥
for m in ["③ ジンガ", "④ 三角ドリブル", "⑤ パンダ兄弟", "⑥ ダブルタッチ"]:
    if st.checkbox(m):
        checked.append(m)

# ---- ⑦ 左足
if st.checkbox("⑦ 左足"):
    checked.append("左足")

# ---- ⑧ ストレッチ
stretch_all = st.checkbox("⑧ ストレッチ（全部やった）")
if stretch_all:
    for s in stretch_items:
        st.session_state["stretch_" + s] = True

with st.expander("▼ ストレッチ"):
    for s in stretch_items:
        if st.checkbox(s, key="stretch_" + s):
            checked.append(s)

# ---- ⑨⑩
if st.checkbox("⑨ 体幹"):
    checked.append("体幹")
if st.checkbox("⑩ その他"):
    checked.append("その他")

# =====================
# 保存
# =====================
st.divider()
memo = st.text_input("メモ（任意）")

if st.button("💾 今日の自主練を保存"):
    if checked:
        file_exists = os.path.exists(FILENAME)
        with open(FILENAME, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["日付", "内容", "メモ"])
            writer.writerow([
                date.today().strftime("%Y-%m-%d"),
                " / ".join(checked),
                memo
            ])
        st.success("保存しました（消えません）")
    else:
        st.warning("チェックがありません")

# =====================
# 記録表示（EmptyDataError対策済）
# =====================
st.divider()
st.subheader("📊 自主練記録（Excel形式）")

df = None
if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
    try:
        df = pd.read_csv(FILENAME)
    except pd.errors.EmptyDataError:
        df = None

if df is not None and not df.empty:
    # 削除チェック初期化
    for i in range(len(df)):
        init(f"del_{i}")

    # チェック表示
    for i, row in df.iterrows():
        st.checkbox(
            f"{row['日付']}｜{row['内容']}",
            key=f"del_{i}"
        )

    st.dataframe(df, use_container_width=True)

    # ---- 個別削除（二段階）
    if st.button("🗑 チェックした記録を削除"):
        if not st.session_state.delete_mode:
            st.session_state.delete_mode = True
            st.warning("もう一度押すと削除されます")
        else:
            new_df = df[[not st.session_state[f"del_{i}"] for i in range(len(df))]]
            new_df.to_csv(FILENAME, index=False)
            for i in range(len(df)):
                st.session_state[f"del_{i}"] = False
            st.session_state.delete_mode = False
            st.success("削除しました")
            st.experimental_rerun()

    # ---- 全消し（二段階・安全）
    if st.button("⚠️ 記録をすべて削除"):
        if not st.session_state.confirm_all_delete:
            st.session_state.confirm_all_delete = True
            st.warning("もう一度押すと【全削除】されます")
        else:
            if os.path.exists(FILENAME):
                os.remove(FILENAME)
            st.session_state.confirm_all_delete = False
            st.success("全記録を削除しました")
            st.experimental_rerun()
else:
    st.write("まだ記録はありません")
