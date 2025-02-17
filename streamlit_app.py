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

with st.sidebar:
  st.header("введите признак:   ")
  island = st.selectbox("Island", ("Torgersen", "Dream", "Biscoe"))
  bill_length_mm = st.slider("Bill length", 32.1, 59.6 ,44.5)
  bill_depth = st.slider("Bill depth", 13.1, 21.5, 17.3)
  flipper_length = st.slider('Flipper length', 32.1, 59.6 , 44.5)
  body_mass = st.slider("Body mass", 32.1 , 59.6, 44.5)
  gender = st.slider("Gender", ('female', 'male'))
  
