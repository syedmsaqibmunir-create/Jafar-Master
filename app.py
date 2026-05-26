import streamlit as st

st.set_page_config(page_title="جفر گرینڈ ماسٹر", layout="centered")

# اردو کے لیے سیدھی لکھائی
st.markdown("""
<style>
    body, .stApp { direction: rtl; text-align: right; font-family: sans-serif; }
    h1 { color: #facc15; }
</style>
""", unsafe_allow_html=True)

st.title("علمِ جفر گرینڈ ماسٹر")

# مینو (Tabs)
tab1, tab2, tab3, tab4 = st.tabs(["زائچہ", "سوال", "موکل", "نقش"])

with tab1:
    st.header("ذاتی زائچہ")
    name = st.text_input("سائل کا نام")
    if st.button("زائچہ نکالیں"):
        st.write("آپ کا زائچہ تیار ہو رہا ہے...")

with tab2:
    st.header("سوال و جواب")
    ques = st.text_input("اپنا سوال لکھیں")
    if st.button("جواب حاصل کریں"):
        st.write("جفری انجن کے مطابق جواب...")

# ... اسی طرح باقی ٹیبز ...