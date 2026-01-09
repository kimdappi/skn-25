import streamlit as st 
import MySQLdb
import pandas as pd 

conn = MySQLdb.connect(host='myserver', user='play', passwd='123', db='encore')

df = pd.read_sql_query("select * from hotel_ratings", conn)

st.dataframe(df)
