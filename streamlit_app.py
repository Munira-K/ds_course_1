import streamlit as st
import pandas as pd
import plotly.express as px

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
  gender = st.selectbox("Gender", ('female', 'male'))



import plotly.express as px

st.subheader('Data Visualization')
fig = px.scatter(
    df,
    x='bill_length_mm',
    y='bill_depth_mm',
    color='island',
    title='Bill Length vs. Bill Depth by Island'
)
st.plotly_chart(fig)

fig2 = px.histogram(
    df, 
    x='body_mass_g', 
    nbins=30, 
    title='Distribution of Body Mass'
)
st.plotly_chart(fig2)

data = {
    'island': island,
    'bill_length_mm': bill_length_mm,
    'bill_depth_mm': bill_depth,
    'flipper_length_mm': flipper_length,
    'body_mass_g': body_mass,
    'sex': gender
}
input_df = pd.DataFrame(data, index=[0])
input_penguins = pd.concat([input_df, X_row], axis=0)

  
  
