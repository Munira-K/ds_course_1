import streamlit as st
import pandas as pd

st.title("🎈 Munira's attempts to be smart...")

st.write('So sad...')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

with st.expander("Data"):
  st.write("X")
  X_row = df.drop("species", axis = 1)
  st.dataframe(X_row)

  st.write("y")
  y_row = df.species
  st.dataframe(y_row)
