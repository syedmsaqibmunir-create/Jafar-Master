import streamlit as st
import datetime

# سیشن سٹیٹ کا استعمال تاکہ ڈیٹا غائب نہ ہو
if 'total_sum' not in st.session_state: st.session_state.total_sum = 0
if 'q_sum' not in st.session_state: st.session_state.q_sum = 0

abjad = {'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ہ': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ی': 10, 'ک': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000}
saat_names = ["زحل", "مشتری", "مریخ", "شمس", "زہرہ", "عطارد", "قمر"]

st.title("علم جفر گرینڈ ماسٹر (پروفیشنل)")
tabs = st.tabs(["زائچہ و سوال", "ساعتِ وقت", "نقش سازی"])

with tabs[0]:
    col1, col2 = st.columns(2)
    with col1:
        n = st.text_input("سائل کا نام")
        m = st.text_input("والدہ کا نام")
        if st.button("زائچہ نکالیں"):
            st.session_state.total_sum = sum(abjad.get(c, 0) for c in n+m)
        st.success(f"کل مجموعہ: {st.session_state.total_sum}")
    with col2:
        q = st.text_input("اپنا سوال")
        if st.button("جواب"):
            st.session_state.q_sum = sum(abjad.get(c, 0) for c in q)
        st.write(f"سطرِ ناطقہ کا عدد: {st.session_state.q_sum}")

with tabs[1]:
    st.header("ساعتِ وقت کا مکمل چارٹ")
    # دن کی تمام 12 ساعتیں دکھانے کا ٹیبل
    data = [[i+1, saat_names[i % 7]] for i in range(12)]
    st.table(data)
    hour = datetime.datetime.now().hour
    st.metric("موجودہ ساعت", saat_names[hour % 7])

with tabs[2]:
    maqsad = st.selectbox("مقصد", ["محبت", "رزق", "عزت"])
    if st.button("نقش تیار کریں"):
        st.write(f"مقصد: {maqsad} کے لیے نقش کا خاکہ:")
        st.code("س ع ف\nف س ع\nع ف س")