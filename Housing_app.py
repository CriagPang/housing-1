import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data(1990) by Pang Qige')
df = pd.read_csv('housing.csv')

# set the slider
median_house_price_filter = st.slider('Median House Price', 0, 500001, 200000)

# set the sidebar of multiselect
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique())

# set the sidebar of a radio button
income_level_filter = st.sidebar.radio('Choose income level:',pd.DataFrame(['Low', 'Medium', 'High']))

# filter data by median house price
df = df[df.median_house_value <= median_house_price_filter]

# filter databy location
df = df[df.ocean_proximity.isin(location_filter)] 

# filter data by income
st.subheader('See more filters in the sidebar:')
if income_level_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_level_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income <= 4.5)]
elif income_level_filter == 'High':
    df = df[df.median_income > 4.5]

# draw the map
st.map(df)

# draw the graph
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots()
df.median_house_value.hist(ax = ax, bins = 30)
st.pyplot(fig)