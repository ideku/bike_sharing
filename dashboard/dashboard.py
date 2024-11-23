import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

day_df = pd.read_csv("dashboard/day_clean.csv")
hour_df = pd.read_csv("dashboard/hour_clean.csv")
monthly_bs_df = pd.read_csv("dashboard/monthly_bs_df_clean.csv")

st.set_page_config(
    page_title="Bike Sharing Project",
    #layout="wide"
)

with st.sidebar:
    st.title("Bike Sharing Dashboard")
    
    year_list = list(day_df.year.unique())[::-1]
    selected_year = st.selectbox("Select a year", year_list, index=len(year_list)-1)
    df_selected_year = day_df[day_df.year == selected_year]
    df_selected_year_sorted = df_selected_year.sort_values(by="year", ascending=False)

#Melengkapi Dashboard dengan Berbagai Visualisasi Data
st.header('Bike Sharing :sparkles:')

st.subheader('Jumlah Penyewaan Sepeda')
col1, col2, col3 = st.columns(3)
 
with col1:
    total_orders = day_df.query("year == @selected_year").count_bs.sum()
    st.metric("Total Sharing Bike", value=total_orders)

with col2:
    total_sum = day_df.query("year == @selected_year & workingday == 'Yes'").count_bs.sum()
    st.metric("Working Day", value=total_sum)

with col3:
    total_sum = day_df.query("year == @selected_year & workingday == 'No'").count_bs.sum()
    st.metric("Not Working Day", value=total_sum)

st.subheader("Musim penyewaan sepeda paling banyak, dan musim penyewaan sepeda paling sedikit")

colors = ["#D3D3D3", "#D3D3D3", "#90CAF9", "#3037CF"]
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
        y="count_bs",
        x="season",
        data=day_df.sort_values(by="season", ascending=False),
        palette=colors,
        ax=ax,
        hue="season"
    )

#ax.set_title("Penyewaan sepeda per musim", loc="center", fontsize=25)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)

st.pyplot(fig)


st.subheader("Perbandingan persentase penyewaan sepeda pada hari kerja (workingday=Yes) dengan pada hari libur (workingday=No)")

workingday_yes = day_df[day_df.workingday == "Yes"].count_bs.sum()
workingday_no = day_df[day_df.workingday == "No"].count_bs.sum()

labels = ['Working Day', 'Not Working Day']
sizes = [workingday_yes, workingday_no]
explode = (0, 0) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',colors=["#D3D3D3", "#90CAF9"],
        shadow=False, startangle=90)
ax1.axis('equal')  

st.pyplot(fig1)


st.subheader("Waktu penyewaan sepeda paling banyak, dan waktu penyewaan sepeda paling sedikit")

colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3",
          "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3",
          "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#3037CF",
          "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

fig, ax = plt.subplots(figsize=(15, 8))

sns.barplot(
        y="count_bs",
        x="hour",
        data=hour_df.sort_values(by="hour", ascending=False),
        palette=colors,
        ax=ax,
        hue="hour",
        legend=False
    )

#ax.set_title("Penyewaan sepeda terbanyak dan sedikit berdasarkan jam", loc="center", fontsize=25)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)

st.pyplot(fig)


st.subheader("Kinerja penyewaan sepeda selama tahun 2011 hingga tahun 2012")

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(monthly_bs_df["date"], monthly_bs_df["bike sharing"], marker='o', linewidth=2, color="#72BCD4")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
plt.xticks(rotation=45)
st.pyplot(fig)
