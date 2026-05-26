import streamlit as st
from datetime import datetime, timedelta

# ڈیزائن سیٹنگ
st.set_page_config(page_title="جفر گرینڈ ماسٹر", layout="centered")

# پاکستان کے وقت کے لیے آفسیٹ (UTC+5)
def get_pk_time():
    return datetime.utcnow() + timedelta(hours=5)

# ساعت کا حساب (پاکستان کے وقت کے مطابق)
def get_current_saat():
    hour = get_pk_time().hour
    # ساعتوں کی ترتیب (طلوعِ آفتاب سے شروع)
    saat_list = ["زحل", "مشتری", "مریخ", "شمس", "زہرہ", "عطارد", "قمر"]
    return saat_list[hour % 7]

st.title("علمِ جفر گرینڈ ماسٹر")

# مینو
choice = st.sidebar.selectbox("مینو", ["زائچہ", "سوال", "موکل", "نقش"])

if choice == "موکل":
    st.header("موکلِ ساعت")
    pk_now = get_pk_time()
    st.write(f"موجودہ وقتِ پاکستان: {pk_now.strftime('%H:%M')}")
    st.write(f"موجودہ ساعت: **{get_current_saat()}**")
    st.warning("یہ ساعت جفری عملیات کے لیے فعال ہے۔")

# بقیہ حصے اسی طرح رہیں گے...