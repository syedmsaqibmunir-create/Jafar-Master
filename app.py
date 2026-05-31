import streamlit as st
import datetime

# 1. ابجدِ قمری کی ڈکشنری
abjad_qamari = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ہ': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ی': 10,
    'ک': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100,
    'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
}

# 2. ساعت اور موکل کا ڈیٹا
saat_data = {
    0: {"ساعت": "زحل", "موکل": "کسفیائیل"}, 1: {"ساعت": "مشتری", "موکل": "صرفیائیل"},
    2: {"ساعت": "مریخ", "موکل": "سمسمائیل"}, 3: {"ساعت": "شمس", "موکل": "رقیائیل"},
    4: {"ساعت": "زہرہ", "موکل": "عنائیل"}, 5: {"ساعت": "عطارد", "موکل": "میخائیل"},
    6: {"ساعت": "قمر", "موکل": "جبرائیل"}
}

def calculate_abjad(text):
    return sum(abjad_qamari.get(char, 0) for char in text)

# انٹرفیس
st.title("علم جفر گرینڈ ماسٹر")
tabs = st.tabs(["زائچہ", "سوال و جواب", "موکل ساعت", "نقش سازی"])

# زائچہ ٹیب
with tabs[0]:
    st.header("زائچہ سازی")
    n = st.text_input("سائل کا نام")
    m = st.text_input("والدہ کا نام")
    if st.button("زائچہ نکالیں"):
        if n and m:
            st.success(f"سائل: {calculate_abjad(n)} | والدہ: {calculate_abjad(m)}")
            st.write(f"کل مجموعہ: {calculate_abjad(n) + calculate_abjad(m)}")
        else: st.warning("نام درج کریں")

# سوال و جواب ٹیب
with tabs[1]:
    st.header("سوال و جواب")
    q = st.text_input("اپنا سوال لکھیں")
    if st.button("جواب حاصل کریں"):
        if q: st.write(f"سوال کا عدد: {calculate_abjad(q)} | سطر ناطقہ کا جواب: حساب جاری ہے...")

# موکل ساعت ٹیب
with tabs[2]:
    st.header("موکل ساعت")
    st.write(f"وقت پاکستان: {datetime.datetime.now().strftime('%H:%M')}")
    if st.button("ساعت نکالیں"):
        info = saat_data[datetime.datetime.now().hour % 7]
        st.success(f"ساعت: {info['ساعت']} | موکل: {info['موکل']}")

# نقش سازی ٹیب
with tabs[3]:
    st.header("نقش سازی")
    maqsad = st.selectbox("مقصد منتخب کریں", ["محبت", "رزق", "حفاظت"])
    if st.button("نقش تیار کریں"):
        st.write(f"آپ کا مقصد: {maqsad}")
        st.table([["س", "ع", "ف"], ["ف", "س", "ع"], ["ع", "ف", "س"]])