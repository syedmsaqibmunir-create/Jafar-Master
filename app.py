import streamlit as st

# سیٹ اپ: صاف ستھرا ڈیزائن
st.set_page_config(page_title="جفر گرینڈ ماسٹر", layout="centered")

st.markdown("""
<style>
    body { direction: rtl; text-align: right; }
    h1 { color: #004a99; text-align: center; }
    .stApp { background-color: #f9f9f9; }
</style>
""", unsafe_allow_html=True)

st.title("علمِ جفر گرینڈ ماسٹر")

# مینیو کے آپشنز
menu = ["زائچہ", "سوال", "موکل", "نقش"]
choice = st.sidebar.selectbox("مینو منتخب کریں", menu)

# ہر مینیو کے لیے الگ لاجک
if choice == "زائچہ":
    st.header("زائچہ سازی")
    name = st.text_input("سائل کا نام لکھیں")
    if st.button("زائچہ نکالیں"):
        st.write(f"سائل **{name}** کے لیے جفری حساب:")
        st.success("آپ کا زائچہ: ماضی میں سکون، حال میں ترقی، مستقبل میں کامیابی!")

elif choice == "سوال":
    st.header("سوال و جواب")
    q = st.text_input("اپنا سوال درج کریں")
    if st.button("جواب حاصل کریں"):
        st.write("سطرِ ناطقہ کا تجزیہ کیا جا رہا ہے...")
        st.info("حتمی جواب: آپ کا کام جلد تکمیل کو پہنچے گا، ان شاء اللہ۔")

elif choice == "موکل":
    st.header("موکلِ ساعت")
    st.write("موجودہ ساعت کے موکل:")
    st.warning("**ہیطائیل** - یہ ساعت برائے تسخیر اور کامیابی انتہائی موثر ہے۔")

elif choice == "نقش":
    st.header("نقش سازی")
    if st.button("نقش مثلث برائے فتح"):
        st.write("نقش تیار ہے:")
        st.code("۴  ۹  ۲\n۳  ۵  ۷\n۸  ۱  ۶")
        st.write("اس نقش کو زعفران سے لکھ کر اپنے پاس رکھیں۔")