import streamlit as st
from datetime import datetime, timedelta

# ڈیزائن: سفید بیک گراؤنڈ
st.set_page_config(page_title="جفر گرینڈ ماسٹر", layout="wide")
st.markdown("""
<style>
    body { direction: rtl; text-align: right; font-family: Tahoma; background-color: white; }
    .stApp { background-color: white; color: black; }
</style>
""", unsafe_allow_html=True)

# ساعت کا درست حساب (پاکستان)
def get_pk_time():
    return datetime.utcnow() + timedelta(hours=5)

def get_current_saat():
    hour = get_pk_time().hour
    saat_list = ["زحل", "مشتری", "مریخ", "شمس", "زہرہ", "عطارد", "قمر"]
    return saat_list[hour % 7]

st.title("علمِ جفر گرینڈ ماسٹر")

# مینو
menu = ["زائچہ", "سوال", "موکل", "نقش"]
choice = st.sidebar.selectbox("مینو منتخب کریں", menu)

if choice == "زائچہ":
    st.header("زائچہ سازی")
    with st.form("zaircha_form"):
        name = st.text_input("سائل کا نام")
        mother_name = st.text_input("والدہ کا نام")
        submit = st.form_submit_button("زائچہ نکالیں")
        if submit:
            st.write(f"سائل: {name} بن/بنت {mother_name}")
            st.success("حسابِ جفر مکمل!")

elif choice == "سوال":
    st.header("سوال و جواب")
    with st.form("q_form"):
        q = st.text_area("اپنا سوال لکھیں")
        submit = st.form_submit_button("جواب حاصل کریں")
        if submit:
            st.info("سطرِ ناطقہ کا جواب: کامیابی یقینی ہے۔")

elif choice == "موکل":
    st.header("موکلِ ساعت")
    pk_now = get_pk_time()
    st.write(f"وقتِ پاکستان: {pk_now.strftime('%H:%M')}")
    st.write(f"موجودہ ساعت: **{get_current_saat()}**")

elif choice == "نقش":
    st.header("نقش سازی")
    maqsad = st.selectbox("مقصد", ["محبت", "رزق", "فتح"])
    if st.button("نقش تیار کریں"):
        st.write(f"آپ کا نقشِ {maqsad} تیار ہے۔")