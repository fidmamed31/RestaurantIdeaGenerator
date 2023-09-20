import streamlit as st

from LangChainHelper import generate_restaurant_name_menu_items


st.title("Restaurant idea generator ")
cuisine=st.sidebar.selectbox('select a cuisine',('algerian','frensh','arabic','persian','hindi'))


if cuisine:
    response=generate_restaurant_name_menu_items(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items=response["menu_items"].strip().split(",")

    st.write('**Menu items**')
    for item in menu_items:
        st.write("-",item)