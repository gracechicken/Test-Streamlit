import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Streamlit Demo: Iris Dataset Explorer 🌸")

# Load example dataset
df = sns.load_dataset("iris")

# Show dataset
st.subheader("Raw Data")
st.write(df.head())

# Sidebar options
st.sidebar.header("Controls")
column = st.sidebar.selectbox("Choose a numeric column", df.select_dtypes(include="number").columns)
species = st.sidebar.multiselect("Filter by species", df["species"].unique(), default=df["species"].unique())

# Filter dataset
filtered_df = df[df["species"].isin(species)]

# Show filtered data
st.subheader("Filtered Data")
st.write(filtered_df)

# Plot histogram
st.subheader(f"Histogram of {column}")
fig, ax = plt.subplots()
ax.hist(filtered_df[column], bins=15, color="skyblue", edgecolor="black")
ax.set_xlabel(column)
ax.set_ylabel("Count")
ax.set_title(f"Distribution of {column}")
st.pyplot(fig)
