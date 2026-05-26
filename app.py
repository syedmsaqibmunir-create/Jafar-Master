import streamlit as st
import datetime

# ڈیزائن کی سیٹنگ
st.set_page_config(page_title="جفر گرینڈ ماسٹر", layout="centered")
st.title("علمِ جفر گرینڈ ماسٹر: پروفیشنل سسٹم")

# ساعت کا خود کار حساب (سادہ فنکشن)
def get_current_saat():
    hour = datetime.datetime.now().hour
    # یہ ایک مثالی لاجک ہے، آپ اسے اپنے حساب سے تبدیل کر سکتے ہیں
    saat_list = ["زحل", "مشتری", "مریخ", "شمس", "زہرہ", "عطارد", "قمر"]
    return saat_list[hour % 7]

# مینو
choice = st.sidebar.selectbox("مینو", ["زائچہ", "سوال", "موکل", "نقش"])

if choice == "زائچہ":
    st.header("ذاتی زائچہ فارم")
    with st.form("zaircha_form"):
        name = st.text_input("سائل کا نام")
        mother_name = st.text_input("والدہ کا نام")
        submit = st.form_submit_button("زائچہ نکالیں")
        if submit:
            st.write(f"سائل: {name} بن/بنت {mother_name}")
            st.success("آپ کا زائچہ تیار ہو رہا ہے...")

elif choice == "سوال":
    st.header("سوالِ جفر")
    with st.form("question_form"):
        q = st.text_area("اپنا سوال درج کریں")
        submit = st.form_submit_button("جواب حاصل کریں")
        if submit:
            st.info(f"سوال: {q}")
            st.write("سطرِ ناطقہ کا تجزیہ جاری ہے...")

elif choice == "موکل":
    st.header("موکلِ ساعت")
    st.write(f"موجودہ وقت: {datetime.datetime.now().strftime('%H:%M')}")
    st.write(f"موجودہ ساعت: **{get_current_saat()}**")
    st.warning("اس ساعت کے موکلِ خاص کا عمل جاری ہے۔")

elif choice == "نقش":
    st.header("نقش سازی فارم")
    with st.form("naqsh_form"):
        maqsad = st.selectbox("مقصد منتخب کریں", ["محبت", "رزق", "فتح"])
        submit = st.form_submit_button("نقش تیار کریں")
        if submit:
            st.write(f"مقصد: {maqsad} کے لیے نقشِ مثلث تیار ہے۔")