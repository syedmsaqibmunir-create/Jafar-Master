import streamlit as st
import datetime

# ابجد اور ساعت کا ڈیٹا
abjad = {'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ہ': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ی': 10, 'ک': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000}
saat_names = ["زحل", "مشتری", "مریخ", "شمس", "زہرہ", "عطارد", "قمر"]

st.set_page_config(layout="wide")
st.title("علم جفر گرینڈ ماسٹر (پروفیشنل)")

tabs = st.tabs(["زائچہ و سوال", "ساعتِ وقت", "نقش سازی"])

# 1. زائچہ و سوال
with tabs[0]:
    col1, col2 = st.columns(2)
    with col1:
        n = st.text_input("سائل کا نام")
        m = st.text_input("والدہ کا نام")
        if st.button("زائچہ نکالیں"):
            res = sum(abjad.get(c, 0) for c in n+m)
            st.success(f"کل مجموعہ: {res}")
    with col2:
        q = st.text_input("اپنا سوال")
        if st.button("جواب"):
            st.write(f"سطرِ ناطقہ کا عدد: {sum(abjad.get(c, 0) for c in q)}")

# 2. ساعتِ وقت (خودکار)
with tabs[1]:
    st.header(f"تاریخ: {datetime.date.today()}")
    st.write("دن اور رات کی ساعتوں کا حساب:")
    # سادہ منطق: گھنٹے کے حساب سے ساعت کا تعین
    hour = datetime.datetime.now().hour
    current_saat = saat_names[hour % 7]
    st.metric("موجودہ ساعت", current_saat)
    st.write("نوٹ: یہ ساعت خودکار وقت کے مطابق تبدیل ہو رہی ہے۔")

# 3. نقش سازی
with tabs[2]:
    maqsad = st.selectbox("مقصد", ["محبت", "رزق", "عزت"])
    if st.button("نقش تیار کریں"):
        st.write(f"مقصد: {maqsad} کے لیے نقشِ مثلث:")
        # یہاں نقش کا خاکہ جو آپ کی ضرورت کے مطابق تبدیل ہوگا
        st.code("س ع ف\nف س ع\nع ف س")