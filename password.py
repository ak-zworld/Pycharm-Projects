import streamlit as st
name=st.text_input("NAME")
phno=st.number_input('PHNO',min_value=0)
email=st.text_input('EMAIL')
password=st.text_input('PASSWORD')
create=st.button('CREATE',type='primary')
if create:
    u_count = 0
    l_count = 0
    n_count = 0
    sp_count = 0
    if len(password) >= 8:
        for i in password:
            if i.isupper():
                u_count += 1
            elif i.islower():
                l_count += 1
            elif i.isdigit():
                n_count += 1
            else:
                sp_count += 1

        if u_count > 0 and l_count > 0 and sp_count > 0 and n_count > 0:
            st.success('ACCOUNT CREATED ')
            st.balloons()
        else:
            st.error('ACCOUNT NOT CREATED')

    else:
        st.warning('invalid length')
