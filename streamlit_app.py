import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])

st.write('sample_usernameの値は: ' + st.secrets['sample_username'])
st.write('sample_passwordの値は: ' + st.secrets['sample_password'])