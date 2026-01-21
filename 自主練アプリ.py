import streamlit as st

st.title("自主練チェック")

# =====================
# 基本メニュー
# =====================
st.checkbox("① 一回転ジャンプ")

ball = st.checkbox("▼ ② ボールコーディネーション")

st.checkbox("③ ジンガ")
st.checkbox("④ 三角ドリブル")
st.checkbox("⑤ パンダ兄弟")
st.checkbox("⑥ ダブルタッチ")

# =====================
# ボールコーディネーション中身
# =====================
if ball:
    st.markdown("##### ボールコーディネーション メニュー")

    st.checkbox("① 軸足通し")
    st.checkbox("② 軸足通し（後ろ向き）")
    st.checkbox("③ アウトプッシュ")
    st.checkbox("④ アウトプッシュ（後ろ向き）")
    st.checkbox("⑤ プルプッシュ")
    st.checkbox("⑥ プルプッシュ（後ろ向き）")
    st.checkbox("⑦ 足裏シザース")
    st.checkbox("⑧ 足裏シザース（後ろ向き）")
    st.checkbox("⑨ インシザース")
    st.checkbox("⑩ インシザース（後ろ向き）")
    st.checkbox("⑪ インイン・アウト")
    st.checkbox("⑫ インイン・アウト（後ろ向き）")
    st.checkbox("⑬ インインロール")
    st.checkbox("⑭ インインロール（後ろ向き）")
    st.checkbox("⑮ 連続エラシコ")
    st.checkbox("⑯ 連続エラシコ（後ろ向き）")
    st.checkbox("⑰ アウト → クライフターン")
    st.checkbox("⑱ 足裏転がし合うターン")
    st.checkbox("⑲ ディープジンガ")
    st.checkbox("⑳ ディープジンガ（後ろ向き）")
    st.checkbox("㉑ 覗き込みドリブル")
    st.checkbox("㉒ ダブルタッチ空振り")

# =====================
# ストレッチ
# =====================
stretch = st.checkbox("▼ ⑦ ストレッチ")

if stretch:
    st.markdown("##### ストレッチ内容")

    st.checkbox("① もも（裏・表）")
    st.checkbox("② ふくらはぎ")
    st.checkbox("③ 開脚")
    st.checkbox("④ 開脚（左右）")
    st.checkbox("⑤ 長座前屈")
    st.checkbox("⑥ 前屈")

# =====================
# その他
# =====================
st.checkbox("⑧ 体幹")
st.checkbox("⑨ その他")
