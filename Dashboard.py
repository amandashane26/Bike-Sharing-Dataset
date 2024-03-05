import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

pwd = os.getcwd()

def byseason(df):
    season_rent = df.groupby('season')['cnt'].sum()
    return season_rent

def bytemp(df):
    temp_rent = df.groupby('temp')['cnt'].sum()
    return temp_rent

# import dataframe
day_df = pd.read_csv('C:\\Users\\USER\\OneDrive\\Attachments\\Documents\\Submission\\Dashboard\\day_data.csv')
hour_df = pd.read_csv('C:\\Users\\USER\\OneDrive\\Attachments\\Documents\\Submission\\Dashboard\\hour_data.csv')

# Menyiapkan dataframe yang dikelompokkan
byseason_df = byseason(day_df)
bytemp_df = bytemp(hour_df)

st.header('Bike Sharing Dashboard')
st.markdown("""
<div style="text-align: justify">
  Pada dashboard ini akan disajikan jumlah pengguna sepeda pada musim, bulan, dan temperatur tertentu.
</div>
""", unsafe_allow_html=True)

st.markdown("\n")

st.subheader('Bar Chart Jumlah Pengguna Sepeda pada Musim Tertentu')

st.markdown("\n")

# Menampilkan plot
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=day_df['season'], y=day_df['casual'], ax=ax)
plt.xlabel('Season')
plt.ylabel('Casual')
plt.title('Casual Bikers Rentals by Season')
st.pyplot(fig)

st.markdown("\n")

st.markdown("\n")

fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=day_df['season'], y=day_df['registered'], ax=ax)
plt.xlabel('Season')
plt.ylabel('Registered')
plt.title('Registered Bikers Rentals by Season')
st.pyplot(fig)

st.markdown("\n")

st.markdown("\n")

st.subheader('Bar Chart Jumlah Pengguna Sepeda pada Bulan dan Temperatur Tertentu')

st.markdown("\n")

st.markdown("\n")

# Menampilkan plot
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=hour_df['mnth'], y=hour_df['temp'], ax=ax)
plt.xlabel('Month')
plt.ylabel('Temp')
plt.title('The temperature of every month for the bikers')
st.pyplot(fig)

st.markdown("\n")

st.markdown("\n")

fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x=hour_df['mnth'], y=hour_df['casual'], ax=ax)
plt.xlabel('Month')
plt.ylabel('Casual')
plt.title('The most popular Month for the bikers')
st.pyplot(fig)


st.caption('Copyright (c) Amanda Shane Gracia Siahaan 2024')