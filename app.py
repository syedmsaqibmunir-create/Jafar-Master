import streamlit as st
import datetime

# ابجدِ قمری کی ڈکشنری
abjad_qamari = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ہ': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ی': 10,
    'ک': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100,
    'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
}

def calculate_abjad(text):
    total = 0
    for char in text:
        total += abjad_qamari.get(char, 0)
    return total

# انٹرفیس کی سیٹنگز
st.title("علم جفر گرینڈ ماسٹر")
tabs = st.tabs(["زائچہ", "سوال و جواب", "موکل ساعت", "نقش سازی"])

# 1. زائچہ ٹیب
with tabs[0]:
    st.header("زائچہ سازی")
    name = st.text_input("سائل کا نام (اردو میں)")
    mother_name = st.text_input("والدہ کا نام (اردو میں)")
    if st.button("زائچہ نکالیں"):
        if name and mother_name:
            val_name = calculate_abjad(name)
            val_mother = calculate_abjad(mother_name)
            total = val_name + val_mother
            st.success("حساب جفر مکمل!")
            st.write(f"سائل کا عدد: {val_name} | والدہ کا عدد: {val_mother}")
            st.write(f"کل مجموعی عدد: **{total}**")
        else:
            st.warning("برائے مہربانی نام درج کریں۔")

# 2. سوال و جواب ٹیب
with tabs[1]:
    st.header("سوال و جواب")
    question = st.text_input("اپنا سوال لکھیں")
    if st.button("جواب حاصل کریں"):
        if question:
            q_val = calculate_abjad(question)
            st.write(f"آپ کے سوال کا عددی مان: {q_val}")
            st.write("سطر ناطقہ کا جواب: حساب جاری ہے...")
        else:
            st.error("سوال لکھنا ضروری ہے۔")

# 3. موکل ساعت ٹیب
with tabs[2]:
    st.header("موکل ساعت")
    # ایک سادہ ٹائم لاجک
    hour = datetime.datetime.now().hour
    st.write(f"موجودہ وقت: {datetime.datetime.now().strftime('%H:%M')}")
    st.write(f"موجودہ ساعت کا علم جفر کے مطابق اطلاق: یہاں آپ کا ساعت والا ڈیٹا آئے گا۔")

# 4. نقش سازی ٹیب
with tabs[3]:
    st.header("نقش سازی")
    purpose = st.selectbox("مقصد", ["محبت", "رزق", "حفاظت"])
    if st.button("نقش تیار کریں"):
        st.write(f"آپ کا مقصد: {purpose}")
        st.write("نقش کی ترتیب: [یہاں نقش کا خاکہ بنے گا]")