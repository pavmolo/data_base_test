import streamlit as st
import notion_df
import pandas as pd

notion_df.pandas()
url_bd = st.secrets["page_url"]
api_key = st.secrets["api_key"]
df = pd.read_notion(url_bd, api_key=api_key)
st.dataframe(data=df)

st.table(df)

if st.button('Say hello'):
  df.to_notion('1, 2, 3', api_key=api_key)
  st.table(df)
