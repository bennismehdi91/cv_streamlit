import streamlit as st
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account
import plotly.express as px
import plotly.graph_objects as go
import requests

from turfpy.measurement import bbox
from functools import reduce

FR = "Français"
EN = "English"

with st.sidebar.expander("**Language**"):
    local = st.radio("Select Language / Sélectionnez la langue:", (FR, EN))

if local == EN:
    st.sidebar.markdown(
        """
        ## Sections
    <ul>
        <li><a href="#france">France Overview</a></li>
        <li><a href="#dpt">Evolution per regions and departments</a></li>
        <li><a href="#om">Overseas departments</a></li>
    </ul>
    """,
        unsafe_allow_html=True,
    )
else:
    st.sidebar.markdown(
        """
        ## Sections
    <ul>
        <li><a href="#france">Vue d'ensemble - France</a></li>
        <li><a href="#dpt">Evolution par régions et départements</a></li>
        <li><a href="#om">Départements d'outre-mer</a></li>
    </ul>
    """,
        unsafe_allow_html=True,
    )


###### DATA

#### Load credentials from Streamlit secrets
# credentials_dict = dict(st.secrets["bigquery"])
# credentials = service_account.Credentials.from_service_account_info(credentials_dict)

#### SQL requests
# sql = """
# SELECT * FROM dbt_mbennis.mart_dpt_overseas
# """

# df = pandas_gbq.read_gbq(
#     sql, project_id="mimetic-surfer-402208", credentials=credentials
# )

france_df = pd.read_csv(
    "/home/mehdibennis/projects/cv_streamlit/files/data/PrixImmobilier/plotly/dbt_models_streamlit_cv_mart_mart_france.csv"
)

dpt_df = pd.read_csv(
    "/home/mehdibennis/projects/cv_streamlit/files/data/PrixImmobilier/plotly/dbt_models_cv_streamlit_mart_mart_dpt2.csv",
    dtype={"departement": str},
)

##### BODY
### INTRODUCTION

if local == EN:
    st.title("France Real Estate overview - January 2014 to July 2024")
else:
    st.title("Marché de l'immobilier en France - Janvier 2014 à Juillet 2024")

st.header("Introduction")

if local == EN:
    st.markdown(
        """
        Here's an analysis of french real estate transactions from 2014 to 2024. Data has been found here : https://www.kaggle.com/datasets/benoitfavier/immobilier-france/data
        
        The goal is to provide an end to end analysis. I explored the data with Python (Pandas), before uploading the right tables to my google bigquery project. All data transformation have been done with dbt (https://www.getdbt.com/).
        
        Once the right tables were aggreagated, I get the data using the google.oauth2 and pandas_bgq libraries, and I display them on this streamlit using plotly.

        Note: The dataset lacks data for Corsica and Mayotte.
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        Voici une analyse de l'évolution des prix de l'immobilier en France de 2014 à 2024. Les données ont été téléchargées sur kaggle : https://www.kaggle.com/datasets/benoitfavier/immobilier-france/data

        Le but de cette page est de proposer un projet d'analyse de données de A à Z : j'ai exploré les données en Python (Pandas), j'ai ensuite uploadé les tables brutes sur Google Bigquery, avant d'effectuer toutes les transformations de table via dbt (https://www.getdbt.com/).

        Une fois les données aggrégées, je récupère les tables finalisées sur ce streamlit via une connexion google.oauth2 et la librairie pandas_bgq. Les données sont ensuite présentées via des graphiques plotly.

        Note: Le dataset ne contient pas de données pour la Corse et Mayotte.
        """,
        unsafe_allow_html=True,
    )

### FRANCE OVERVIEW

if local == EN:
    st.header("Overview - France Real Estate Information", anchor="france")
else:
    st.header("Vue d'ensemble - Indicateurs en France", anchor="france")

# Fat dictionnary because I thought it was a good idea to have the streamlit in both french and english...
variable_dict = {
    FR: {
        "Nombre de ventes 🟥": "count_transaction",
        "Prix moyen de vente 🟩": "avg_price",
        "Prix moyen du m² (en €) 🟦": "avg_price_squaredmetters",
        "Taux d'intérêt 🟨": "avg_interest_rate",
        "var_choice": "Sélectionnez l'indicateur à afficher",
        "var_comparison": "Sélectionnez une variable de comparaison",
        "none": "Aucune",
        "dpt_reg": "Départements ou régions",
        "dpt": "Département",
        "reg": "Régions",
        "x_axis_month_year": "Mois & Année",
        "x_axis_year": "Année",
        "Département": {
            "code": "departement",
            "name": "dep_name",
            "geo": "https://france-geojson.gregoiredavid.fr/repo/departements.geojson",
        },
        "Régions": {
            "code": "code_region",
            "name": "region_name",
            "geo": "https://france-geojson.gregoiredavid.fr/repo/regions.geojson",
        },
    },
    EN: {
        "Count of sales 🟥": "count_transaction",
        "Average price 🟩": "avg_price",
        "Average price of m² (in €) 🟦": "avg_price_squaredmetters",
        "Interest rate 🟨": "avg_interest_rate",
        "var_choice": "Please select the indicator to display",
        "var_comparison": "Please select a comparison indicator",
        "none": "None",
        "dpt_reg": "Department or regions",
        "dpt": "Department",
        "reg": "Regions",
        "x_axis_month_year": "Month & Year",
        "x_axis_year": "Year",
        "Department": {
            "code": "departement",
            "name": "dep_name",
            "geo": "https://france-geojson.gregoiredavid.fr/repo/departements.geojson",
        },
        "Regions": {
            "code": "code_region",
            "name": "region_name",
            "geo": "https://france-geojson.gregoiredavid.fr/repo/regions.geojson",
        },
    },
}

variable_dict_keys = list(variable_dict[local].keys())

color_line = {
    "count_transaction": "red",
    "avg_price": "green",
    "avg_price_squaredmetters": "blue",
    "avg_interest_rate": "goldenrod",
}

color_sequence = {
    "count_transaction": "oranges",
    "avg_price": "greens",
    "avg_price_squaredmetters": "blues",
}

col1, col2 = st.columns([1, 1], vertical_alignment="top")
with col1:
    variable_fr = st.radio(
        variable_dict[local]["var_choice"],
        (
            variable_dict_keys[0],
            variable_dict_keys[1],
            variable_dict_keys[2],
            variable_dict_keys[3],
        ),
    )
with col2:
    variable_comp = st.radio(
        variable_dict[local]["var_comparison"],
        (
            variable_dict[local]["none"],
            variable_dict_keys[0],
            variable_dict_keys[1],
            variable_dict_keys[2],
            variable_dict_keys[3],
        ),
    )

fig1 = px.line(
    france_df,
    x="date_year_month",
    y=variable_dict[local][variable_fr],
)
fig1.update_traces(line=dict(color=color_line[variable_dict[local][variable_fr]]))

# If comparison variable selected, then display a new line on the chart.
if variable_comp != variable_dict[local]["none"]:
    fig1.add_trace(
        go.Scatter(
            x=france_df["date_year_month"],
            y=france_df[variable_dict[local][variable_comp]],
            name=variable_comp,
            line=dict(color=color_line[variable_dict[local][variable_comp]]),
            yaxis="y2",
            showlegend=False,
        )
    )

    fig1.update_layout(
        yaxis=dict(title=variable_fr),
        yaxis2=dict(
            title=variable_comp,
            overlaying="y",
            side="right",
            showgrid=False,
        ),
        xaxis_title=variable_dict[local]["x_axis_month_year"],
    )
else:
    fig1.update_layout(
        yaxis_title=variable_fr,
        xaxis_title=variable_dict[local]["x_axis_month_year"],
    )
st.plotly_chart(fig1)

### DEPARTMENT & REGIONS ZOOM

st.divider()

if local == EN:
    st.header("Evolution per regions and departments", anchor="dpt")
else:
    st.header("Evolution par régions et départements", anchor="dpt")


if local == EN:
    st.markdown(
        "<em>Note: The year 2024 is not complete, and stopes in July<br>Double click on the map to reset the view</em>",
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        "<em>Note : L'année 2024 est incomplète, et s'arrête en juillet<br>Double cliquez sur la carte pour réinitialiser la carte</em>",
        unsafe_allow_html=True,
    )

col1, col2 = st.columns([1, 1], vertical_alignment="top")

with col1:
    variable_geo_dpt_reg = st.radio(
        variable_dict[local]["dpt_reg"],
        (variable_dict[local]["dpt"], variable_dict[local]["reg"]),
    )
with col2:
    variable_dpt = st.radio(
        variable_dict[local]["var_choice"],
        (variable_dict_keys[0], variable_dict_keys[1], variable_dict_keys[2]),
    )


### Hack found on stack overflow to improve map view.
gj = requests.get(variable_dict[local][variable_geo_dpt_reg]["geo"]).json()


def compute_bbox(gj):
    gj_bbox_list = list(map(lambda f: bbox(f["geometry"]), gj["features"]))
    gj_bbox = reduce(
        lambda b1, b2: [
            min(b1[0], b2[0]),
            min(b1[1], b2[1]),
            max(b1[2], b2[2]),
            max(b1[3], b2[3]),
        ],
        gj_bbox_list,
    )
    return gj_bbox


gj_bbox = compute_bbox(gj)

### Plotly map
fig = px.choropleth(
    dpt_df,
    geojson=variable_dict[local][variable_geo_dpt_reg]["geo"],
    locations=variable_dict[local][variable_geo_dpt_reg]["code"],
    featureidkey="properties.code",
    color=variable_dict[local][variable_dpt],
    hover_name=variable_dict[local][variable_geo_dpt_reg]["name"],
    animation_frame="date_year",
    color_continuous_scale=color_sequence[variable_dict[local][variable_dpt]],
    labels={
        variable_dict[local][variable_dpt]: variable_dpt,
        "date_year": variable_dict[local]["x_axis_year"],
    },
)

fig.update_geos(
    fitbounds="locations",
    center_lon=(gj_bbox[0] + gj_bbox[2]) / 2,
    center_lat=(gj_bbox[1] + gj_bbox[3]) / 2,
    lonaxis_range=[gj_bbox[0], gj_bbox[2]],
    lataxis_range=[gj_bbox[1], gj_bbox[3]],
    visible=False,
)

color_axis_dict = {
    "count_transaction": {"min": 5000, "max": 25000},
    "avg_price": {"min": 50000, "max": 350000},
    "avg_price_squaredmetters": {"min": 1000, "max": 4000},
}

fig.update_layout(
    geo=dict(showcoastlines=False, showland=False, showframe=False),
    coloraxis=dict(
        cmin=color_axis_dict[variable_dict[local][variable_dpt]]["min"],
        cmax=color_axis_dict[variable_dict[local][variable_dpt]]["max"],
    ),
    margin=dict(l=0, r=0, b=0, t=0),
)

st.plotly_chart(fig)

st.divider()

### OVERSEAS

if local == EN:
    st.header("Overseas departments", anchor="om")
else:
    st.header("Départements d'outre-mer", anchor="om")

outre_mer = dpt_df[dpt_df["departement_int"] > 100]

variable_dict_om = {
    FR: {
        "Nombre de ventes": "count_transaction",
        "Prix moyen de vente": "avg_price",
        "Prix moyen du m² (en €)": "avg_price_squaredmetters",
        "Taux d'intérêt": "avg_interest_rate",
        "var_choice": "Sélectionnez l'indicateur à afficher",
        "dpt": "Département",
    },
    EN: {
        "Count of sales": "count_transaction",
        "Average price": "avg_price",
        "Average price of m² (in €)": "avg_price_squaredmetters",
        "Interest rate": "avg_interest_rate",
        "var_choice": "Please select the indicator to display",
        "dpt": "Department",
    },
}

variable_dict_keys_om = list(variable_dict_om[local].keys())


variable_om = st.radio(
    variable_dict_om[local]["var_choice"],
    (variable_dict_keys_om[0], variable_dict_keys_om[1], variable_dict_keys_om[2]),
    key="om",
)

fig2 = px.line(
    outre_mer,
    x="date_year",
    y=variable_dict_om[local][variable_om],
    color="dep_name",
)

fig2.update_layout(
    yaxis_title=variable_om,
    xaxis_title=variable_dict[local]["x_axis_year"],
    legend_title_text=variable_dict[local]["dpt"],
)

st.plotly_chart(fig2)
