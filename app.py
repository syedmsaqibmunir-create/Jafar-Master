with tabs[0]: # زائچہ
    n = st.text_input("سائل کا نام", key="name_in")
    m = st.text_input("والدہ کا نام", key="mother_in")
    
    if st.button("زائچہ نکالیں"):
        full_name = n + m
        # بسطِ حروف
        letters = [char for char in full_name if char in abjad]
        st.session_state.total_res = sum(abjad.get(c, 0) for c in letters)
        
        # 12 خانوں کا زائچہ (سادہ تکسیر)
        if len(letters) >= 3:
            st.write("آپ کا زائچہ (12 خانے):")
            # حروف کو 12 خانوں میں تقسیم کرنا
            zaicha_table = [letters[i % len(letters)] for i in range(12)]
            # 3x4 کا ٹیبل بنانا
            col_data = [zaicha_table[i:i+3] for i in range(0, 12, 3)]
            st.table(col_data)
        else:
            st.warning("نام مختصر ہے، پورا نام درج کریں۔")

    st.write(f"کل مجموعہ: {st.session_state.total_res}")