import streamlit as st
import datetime
import gspread
from google.oauth2.service_account import Credentials

st.title("自主練チェック")

# ===== 日本時間 =====
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

# ===== Google Sheets 接続 =====
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

gc = gspread.authorize(credentials)
sheet = gc.open("自主練記録").sheet1   # ← シート名

# ===== 今日の日付表示 =====
today = jst_today()
st.subheader(f"📅 今日：{today}")

# ===== チェック =====
checks = {}
for m in menus:
    checks[m] = st.checkbox(m)

# ===== 保存 =====
if st.button("保存"):
    for menu, checked in checks.items():
        sheet.append_row([str(today), menu, checked])

    st.success("保存しました！")

# ===== 一覧表示 =====
st.subheader("📊 記録一覧")

records = sheet.get_all_records()

if records:
    st.dataframe(records)
else:
    st.info("まだ記録がありません")
