import webbrowser
from numpy.lib.function_base import select
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import base64
from bokeh.models.widgets import Div
from PIL import Image

st.set_page_config(page_title='compose.io', page_icon = Image.open('run.png'), layout = 'wide', initial_sidebar_state = 'auto')


st.header('Building a Customizable Virtual Environment for Studying Human Compositional Generalization')
st.markdown('#### MSc Dissertation in Informatics')

st.markdown("""
* **Researcher: ** [Ege Ersü](https://egeersu.github.io/)
* **Principal Investigator: ** [Christopher G. Lucas](https://homepages.inf.ed.ac.uk/clucas2/)
* **Dissertation: ** [PDF](https://egeersu.github.io/papers/dissertation.pdf)
""")

if st.button('Launch Environment'):
    js = "window.open('https://romantic-sinoussi-657706.netlify.app/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)


winners_df = pd.read_csv('data/winners.csv')
craft_df = pd.read_csv('data/crafting.csv')
craft_df = craft_df.dropna()
craft_df = craft_df.reset_index(drop=True)

winner_ids = list(winners_df['Winners'])
all_ids = craft_df['ID'].unique()
loser_ids = [elt for elt in all_ids if elt not in winner_ids]

winners = st.sidebar.header('Filter Data')
selected_groups = st.sidebar.multiselect('Group', [1,2], default=[1,2])
selected_days = st.sidebar.multiselect('Day', [1,2,3], default=[1,2,3])
selected_completion = st.sidebar.multiselect('Completion', ['Winners', 'Losers'], default=['Winners', 'Losers'])


def select_ids(selected_completions):
    selected_ids = []
    if 'Winners' in selected_completions:
        selected_ids.extend(winner_ids)
    if 'Losers' in selected_completions:
        selected_ids.extend(loser_ids)
    return selected_ids

print(len(select_ids(selected_completion)))


selected_df = craft_df[craft_df['Group'].isin(selected_groups) & craft_df['Day'].isin(selected_days) & craft_df['ID'].isin(select_ids(selected_completion))]

st.header('Explore Our Data')
st.write('Displaying ', selected_df.shape[0], 'attempts from ', len(selected_df['ID'].unique()), ' unique participants.')
selected_df.rename(columns={'ID':'PlayerID'}, inplace=True)
st.dataframe(selected_df)

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_data.csv">Download Filtered Data</a>'
    return href

st.markdown(filedownload(selected_df), unsafe_allow_html=True)