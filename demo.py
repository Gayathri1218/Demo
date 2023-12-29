import streamlit as st
st.set_page_config(page_title='cats')
st.markdown("## Types of cats")
col1,col2,col3=st.columns(3)
with col1:
  st.subheader("Persian cat")
  st.image("./pcat.jpg",caption="persian cat",use_column_width=True)
  st.write("persian cats are cute")
with col2:
  st.write("- white cat")
  st.image("./wcat.jpg", width=280,use_column_width=True)
with col3:
  st.write("- cat")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMtz__o1a8lG_sKQIu47iK0b1neWUBdwBNfg&usqp=CAU",use_column_width=True)
