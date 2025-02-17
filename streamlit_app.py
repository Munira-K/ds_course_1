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


with st.expander("Input features"):
  st.write('*Input penguin*')
  st.dataframe(input_df)
  st.write('*Comvcdghdghj*')
  st.dataframe(input_peng)

encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_peng, prefix = encode)
X = df_penguins[1:]
input_row = df_penguins[:1]
target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
  return target_mapper[val]
y = y_raw.apply(target_encode)

with st.expander('Data fhfh'):
  st.dataframe(input_row)
  st.write(y)

  
  
