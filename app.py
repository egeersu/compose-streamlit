import webbrowser
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


st.header('Studying Human Compositional Generalization in Virtual Environments')
st.markdown('#### MSc Dissertation in Informatics')

st.markdown("""
* **Researcher: ** [Ege Ersü](https://egeersu.github.io/)
* **Principal Investigator: ** [Christopher G. Lucas](https://homepages.inf.ed.ac.uk/clucas2/)
* **Dissertation: ** [PDF](https://egeersu.github.io/papers/dissertation.pdf)
""")

if st.button('LAUNCH ENVIRONMENT'):
    webbrowser.open_new_tab('https://romantic-sinoussi-657706.netlify.app/')
