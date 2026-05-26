import streamlit as st

# سیٹ اپ: اردو اور لے آؤٹ
st.set_page_config(page_title="جفر گرینڈ ماسٹر", layout="wide")
st.markdown("""
<style>
    body { direction: rtl; text-align: right; font-family: Tahoma; }
    .stApp { background-color: #0f172a; color: white; }
    h1 { color: #fbbf24; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("علمِ جفر گرینڈ ماسٹر: مکمل ڈیش بورڈ")

# سائیڈ بار مینو
menu = ["زائچہ", "سوال", "موکل", "نقش"]
choice = st.sidebar.selectbox("مرکزی مینو", menu)

# لاجک
if choice == "زائچہ":
    st.header("ذاتی زائچہ")
    name = st.text_input("سائل کا نام درج کریں")
    if st.button("زائچہ نکالیں"):
        st.success(f"{name} کا زائچہ تیار ہے...")
        st.write("ماضی: توازن اور محنت۔")
        st.write("حال: کامیابی کے قریب۔")
        st.write("مستقبل: روشن امکانات۔")

elif choice == "سوال":
    st.header("سوال و جواب")
    q = st.text_input("اپنا سوال یہاں لکھیں")
    if st.button("جواب حاصل کریں"):
        st.info("سطرِ ناطقہ کا تجزیہ: کام جلد تکمیل پذیر ہوگا۔")

elif choice == "موکل":
    st.header("موکلِ ساعت")
    st.write("اس وقت کے موکل: **ہیطائیل**")
    st.warning("یہ ساعت تسخیر کے لیے انتہائی طاقتور ہے۔")

elif choice == "نقش":
    st.header("نقشِ سازی")
    st.write("اپنی مرضی کا نقش منتخب کریں:")
    if st.button("نقشِ مثلث تیار کریں"):
        st.image("https://upload.wikimedia.org/wikipedia/commons/e/e9/Magic_square.svg", width=200)
        st.write("نقشِ مثلث فتحِ مبین کے لیے تیار ہے۔")