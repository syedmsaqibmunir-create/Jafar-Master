import streamlit as st

# اردو کے لیے اسٹائلنگ
st.markdown("""
<style>
    body { direction: rtl; text-align: right; }
    .stApp { font-family: Tahoma; }
</style>
""", unsafe_allow_html=True)

st.title("جفر گرینڈ ماسٹر: مکمل سسٹم")

# مینو
menu = ["زائچہ", "سوال", "موکل", "نقش"]
choice = st.sidebar.selectbox("سیکشن منتخب کریں", menu)

# ابجد کا انجن (مثالی ڈیٹا)
def get_abjad(name):
    # یہاں آپ اپنا مکمل ابجدی فارمولا لگا سکتے ہیں
    return sum(len(n) for n in name) * 12 

if choice == "زائچہ":
    st.header("ذاتی زائچہ")
    name = st.text_input("سائل کا نام")
    if st.button("زائچہ نکالیں"):
        if name:
            st.write(f"سائل: {name}")
            st.info("حسابِ جفر جاری ہے...")
            st.write("ماضی: آپ کی زندگی میں توازن کی کمی رہی۔")
            st.write("حال: مشتری کا اثر ہے، ترقی کا وقت ہے۔")
            st.write("مستقبل: کامیابی کے آثار نمایاں ہیں۔")

elif choice == "سوال":
    st.header("جفری سوال و جواب")
    q = st.text_input("اپنا سوال لکھیں")
    if st.button("جواب نکالیں"):
        st.write("سطرِ ناطقہ کا حتمی جواب: 'کامیابی قریب ہے'")

elif choice == "موکل":
    st.header("موکلِ ساعت")
    st.write("اس وقت کے موکل: **ہیطائیل** - یہ ساعت برائے تسخیرِ قلوب ہے۔")

elif choice == "نقش":
    st.header("نقشِ سازی")
    st.write("نقشِ مثلث برائے فتح تیار کر دیا گیا ہے۔ اسے زعفران سے لکھیں۔")