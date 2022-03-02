import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

# This is the source code for Lab 3 app. The App contains vizualizations and the report.
# Link to streamlit app
# https://share.streamlit.io/rystew17/lab3/main/lab3.py

st.title("CSE 5544 Lab 3 - Ethics")
st.header("Ryan Stewart (.1756)")

data = pd.read_csv("https://raw.githubusercontent.com/CSE5544/data/main/ClimateData.csv")

countries = data['Country\\year']
df_data_country = data.iloc[:,2:]
df_data_country = df_data_country.apply(pd.to_numeric, errors='coerce')
country_stats = pd.DataFrame({'country': countries, 'mean': df_data_country.mean(axis=1), 'std': df_data_country.std(axis=1)})
chart_data = data.drop(columns=['Non-OECD Economies'])
chart_data = pd.melt(chart_data, id_vars=['Country\year'], var_name='year')
chart_data['value'] = chart_data['value'].apply(pd.to_numeric, errors='coerce')
chart_data.rename(columns={"Country\year": "country", "value":"emission"}, inplace = True)

heatmap1 = alt.Chart(chart_data).mark_rect().encode(
    x=alt.X('country:N', title = 'Country'),
    y=alt.Y('year:O', title = 'Year'),
    color=alt.Color('emission:Q', scale=alt.Scale(scheme='rainbow')),
    tooltip=['country', 'year', 'emission']
).properties(
    width = 1000,
    height = 1000
)

heatmap2 = alt.Chart(chart_data).mark_rect().encode(
    x=alt.X('country:N', title = 'Country'),
    y=alt.Y('year:O', title = 'Year'),
    color=alt.Color('emission:Q', scale=alt.Scale(scheme='greys')),
    tooltip=['country', 'year', 'emission']
).properties(
    width = 1000,
    height = 1000
)

st.markdown("<h4 style='text-align: center; color: black;'>Emmissions</h4>", unsafe_allow_html=True)
st.altair_chart(heatmap1)
st.markdown("<h4 style='text-align: center; color: black;'>Heatmap of Reported Emissions for each Country (1990-2019)</h4>", unsafe_allow_html=True)
st.altair_chart(heatmap2)

st.write('In my opinion, the second visualization is a better vizualization for contextualizing the Emissions data from the P1 perspective. The second vizualization uses the Luminance as the indicator of level of Emissions, this makes the vizualization easy to read and distinguish what countries have high levels of emissions and what countries have low levels of emissions. While the first visualization uses a diverging color scheme, with the rainbow. As the high level emission colors of blue and the low level emission colors of violet, are hard to distinguish from each other. This makes the heatmap very misleading, as most viewers would mistakingly think that the middle level emission countries are the highest level and would mistake the high level emissions as low level emissions, this is especially true for someone who is colorblind, as I am.')



