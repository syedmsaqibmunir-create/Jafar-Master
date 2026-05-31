import streamlit as st
import datetime

# 1. سیشن سٹیٹ کا آغاز
if 'total_res' not in st.session_state: st.session_state.total_res = 0
if 'q_res' not in st.session_state: st.session_state.q_res = 0

# 2. ابجد اور ڈیٹا
abjad = {'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ہ': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ی': 10, 'ک': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000}
saat_names = ["زحل", "مشتری", "مریخ", "شمس", "زہرہ", "عطارد", "قمر"]
muwakil = ["کسفیائیل", "صرفیائیل", "سمسمائیل", "رقیائیل", "عنائیل", "میخائیل", "جبرائیل"]

st.title("علمِ جفر گرینڈ ماسٹر")

# 3. ٹیبز کا تعین
tabs = st.tabs(["زائچہ", "سوال", "ساعت", "نقش", "ابجد"])

# 4. زائچہ کا ٹیب
with tabs[0]:
    n = st.text_input("سائل کا نام", key="name_input")
    m = st.text_input("والدہ کا نام", key="mother_input")
    if st.button("زائچہ نکالیں"):
        st.session_state.total_res = sum(abjad.get(c, 0) for c in n+m)
    st.write(f"کل مجموعہ: {st.session_state.total_res}")

# 5. سوال کا ٹیب
with tabs[1]:
    q = st.text_input("اپنا سوال", key="q_input")
    if st.button("جواب"):
        st.session_state.q_res = sum(abjad.get(c, 0) for c in q)
    st.write(f"سطرِ ناطقہ کا عدد: {st.session_state.q_res}")

# 6. ساعت کا ٹیب
with tabs[2]:
    st.header("ساعت اور موکل")
    current_hour = datetime.datetime.now().hour
    idx = (current_hour + 6) % 7 
    st.metric("موجودہ ساعت", saat_names[idx])
    st.metric("موجودہ موکل", muwakil[idx])

# 7. نقش کا ٹیب
with tabs[3]:
    if st.button("نقش تیار کریں"):
        st.write("نقشِ مثلث کا خاکہ:")
        st.code("س ع ف\nف س ع\nع ف س")

# 8. ابجد کا ٹیب
with tabs[4]:
    st.table([{"حرف": k, "عدد": v} for k, v in abjad.items()])