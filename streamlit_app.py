import streamlit as st

# タイトルを表示
st.title('st.experimental_get_query_params')

# URLパラメータを取得して表示
params = st.experimental_get_query_params()
if params is None:
    st.write('get_query_params(): None')
else:
    st.write('get_query_params(): not None')
if isinstance(params, dict):
    st.write('get_query_params(): dict')
    l = len(params)
    st.write('get_query_params(): len == {}'.format(l))
else:
    st.write('get_query_params(): not dict')
st.write(params)
