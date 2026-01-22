import streamlit as st
from datetime import date

st.title("自主練チェック")

# =====================
# セッション初期化
# =====================
if "records" not in st.session_state:
    st.session_state.records = []

def init_check(key):
    if key not in st.session_state:
        st.session_state[key] = False

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

# =====================
# チェック初期化
# =====================
for i in ball_items:
    init_check("ball_" + i)

for s in stretch_items:
    init_check("stretch_" + s)

checked = []

# =====================
# メニュー表示
# =====================
if st.checkbox("① 一回転ジャンプ"):
    checked.append("一回転ジャンプ")

# ---------- ボールコーディネーション ----------
ball_all = st.checkbox("② ボールコーディネーション ▼")

if ball_all:
    for i in ball_items:
        st.session_state["ball_" + i] = True
else:
    for i in ball_items:
        st.session_state["ball_" + i] = False

if ball_all:
    st.markdown("### ▼ ボールコーディネーション")
    for i in ball_items:
        if st.checkbox(i, key="ball_" + i):
            checked.append(i)

# ---------- 単独メニュー ----------
for m in ["③ ジンガ","④ 三角ドリブル","⑤ パンダ兄弟","⑥ ダブルタッチ"]:
    if st.checkbox(m):
        checked.append(m)

# ---------- ストレッチ ----------
stretch_all = st.checkbox("⑦ ストレッチ ▼")

if stretch_all:
    for s in stretch_items:
        st.session_state["stretch_" + s] = True
else:
    for s in stretch_items:
        st.session_state["stretch_" + s] = False

if stretch_all:
    st.markdown("### ▼ ストレッチ")
    for s in stretch_items:
        if st.checkbox(s, key="stretch_" + s):
            checked.append(s)

# ---------- 残り ----------
if st.checkbox("⑧ 体幹"):
    checked.append("体幹")

if st.checkbox("⑨ その他"):
    checked.append("その他")

# =====================
# 保存
# =====================
st.divider()
memo = st.text_input("メモ（任意）")

if st.button("今日の自主練を保存"):
    if checked:
        st.session_state.records.append({
            "日付": date.today().strftime("%Y-%m-%d"),
            "内容": checked.copy(),
            "メモ": memo
        })
        st.success("保存しました！")
    else:
        st.warning("何もチェックされていません")

# =====================
# 記録一覧
# =====================
st.divider()
st.subheader("📋 自主練の記録")

if st.session_state.records:
    for r in reversed(st.session_state.records):
        st.markdown(f"### {r['日付']}")
        st.write("・" + " / ".join(r["内容"]))
        if r["メモ"]:
            st.write("📝 " + r["メモ"])
else:
    st.write("まだ記録はありません")
