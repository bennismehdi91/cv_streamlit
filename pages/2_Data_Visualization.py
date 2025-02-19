import streamlit as st
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account

FR = "Français"
EN = "English"

with st.sidebar.expander("**Language**"):
    local = st.radio("Select Language / Sélectionnez la langue:", (FR, EN))

st.title("Data Visualization")

if local == EN:
    st.markdown(
        """
        Here's an analysis of french real estate transactions from 2014 to 2024. Data has been found here : https://www.kaggle.com/datasets/benoitfavier/immobilier-france/data<br><br>
        The goal is to provide an end to end analysis. I explored the data with Python, before uploading the right tables to my google bigquery project. All data transformation have been done with dbt (https://www.getdbt.com/).<br><br>
        Once the right tables were aggreagated, I get the data using the google.oauth2 and pandas_bgq libraries, and I display them on this streamlit using plotly. Lastly, I provide a powerpoint export of the data using python-pptx package.
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        Le but de cette page est de jouer avec l'API Tyradex (https://tyradex.vercel.app/).
        On utilise la librairie Python **requests** pour faire un appel GET, nous permettant de récupérer l'ensemble du pokédex en format JSON.
        Pour éviter des appels inutiles à l'API, nous sauvegardons ce JSON en cache. Enfin, ce JSON nous permet de montrer des fiches Pokémon aux utilisateurs :)
        """
    )


# Load credentials from Streamlit secrets
credentials_dict = dict(st.secrets["bigquery"])
credentials = service_account.Credentials.from_service_account_info(credentials_dict)

# Define SQL query
sql = """
SELECT * FROM dbt_mbennis.mart_dpt_overseas
"""

# Fetch data using pandas_gbq

# df = pandas_gbq.read_gbq(
#     sql, project_id="mimetic-surfer-402208", credentials=credentials
# )

st.dataframe(df)
