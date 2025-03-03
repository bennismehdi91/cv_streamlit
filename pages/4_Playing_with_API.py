import streamlit as st
import pandas as pd
import requests
import json

st.set_page_config(
    page_title="Playing with API",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

FR = "Français"
EN = "English"

if "local" not in st.session_state:
    st.session_state.local = FR  # Default local

# Sidebar Local Selection
with st.sidebar.expander("**Language**"):
    local = st.radio(
        "Select language / Sélectionnez la langue:",
        (FR, EN),
        index=0 if st.session_state.local == FR else 1,
    )

# Update session state when a new local is selected
if local != st.session_state.local:
    st.session_state.local = local


st.title("API Pokédex")

if local == EN:
    st.markdown(
        """
        The goal of this page is to play with the API Tyradex (https://tyradex.vercel.app/).
        We use the python **requests** library to do a GET call, to retreive a full JSON of their pokédex.
        We save the json in cache, avoiding unnecessary API requests.
        From the JSON, we'll be able to display Pokémon informations for the user :)
        """
    )
else:
    st.markdown(
        """
        Le but de cette page est de jouer avec l'API Tyradex (https://tyradex.vercel.app/).
        On utilise la librairie Python **requests** pour faire un appel GET, nous permettant de récupérer l'ensemble du pokédex en format JSON.
        Pour éviter des appels inutiles à l'API, nous sauvegardons ce JSON en cache. Enfin, ce JSON nous permet de montrer des fiches Pokémon aux utilisateurs :)
        """
    )


@st.cache_data
def API_call(url: str) -> json:
    """
    Function to call the API, return the json response of the call
    """
    headers = {
        "User-Agent": "Mehdi",
        "From": "bennismehdi91@gmail.com",
        "Content-type": "application/json",
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
    else:
        print("Request failed : ", response.status_code)

    return data


@st.cache_data
def list_fr_function(json: json) -> list[str]:
    """
    Function to create a list of french pokemon names + their index number
    """
    list_fr = list()
    for i in range(1, len(json)):
        name_fr = json[i]["name"]["fr"]
        index = json[i]["pokedex_id"]
        full = name_fr + ", " + str(index)
        list_fr.append(full)
    return list_fr


@st.cache_data
def list_en_function(json: json) -> list[str]:
    """
    Function to create a list of english pokemon names + their index number
    """
    list_en = list()
    for i in range(1, len(json)):
        name_fr = json[i]["name"]["en"]
        index = json[i]["pokedex_id"]
        full = name_fr + ", " + str(index)
        list_en.append(full)
    return list_en


@st.cache_data
def dataframe_index_names(json: json) -> pd.DataFrame:
    """
    Create a dataframe with pokemon index number, french name and english name.
    It'll allow to get the pokemon index number and therefore, get the right json info
    to display the right pokemon sheet
    """
    df_poke = pd.DataFrame()
    for poke in json:
        name_fr_index = poke["name"]["fr"] + ", " + str(poke["pokedex_id"])
        name_en_index = poke["name"]["en"] + ", " + str(poke["pokedex_id"])
        new_row = pd.DataFrame(
            {
                "pokedex_id": [poke["pokedex_id"]],
                "name_fr": [name_fr_index],
                "name_en": [name_en_index],
            }
        )
        df_poke = pd.concat([df_poke, new_row], ignore_index=True)
    return df_poke


pokedex = API_call("https://tyradex.app/api/v1/pokemon")
pokelist_fr = list_fr_function(pokedex)
pokelist_en = list_en_function(pokedex)
df_index_name = dataframe_index_names(pokedex)

if local == FR:
    QUERY = "Rechercher un nom de pokémon ou son n°"
    ERROR = "Aucun pokémon correspondant. Veuillez affiner votre recherche."
    PRECISION = "Préciser le pokémon :"
    NAME = "name_fr"
else:
    QUERY = "Search for a pokémon name or number"
    ERROR = "No matching pokémon. Please refine your search."
    PRECISION = "Specify pokémon:"
    NAME = "name_en"


query_input = st.text_input(QUERY)

if local == EN:
    if query_input:
        filtered_options = [
            option for option in pokelist_en if query_input.lower() in option.lower()
        ]
    else:
        filtered_options = [pokelist_en[0]]
else:
    if query_input:
        filtered_options = [
            option for option in pokelist_fr if query_input.lower() in option.lower()
        ]
    else:
        filtered_options = [pokelist_fr[0]]

if not filtered_options:
    st.error(ERROR)
    st.stop()

if len(filtered_options) > 1:
    selected_option = st.selectbox(PRECISION, filtered_options)
else:
    selected_option = filtered_options[0]

df_poke = df_index_name[df_index_name[NAME] == selected_option]
if df_poke.empty:
    st.error(ERROR)
    st.stop()

index_poke = df_poke["pokedex_id"].iloc[0]

name_fr = pokedex[index_poke]["name"]["fr"]
name_en = pokedex[index_poke]["name"]["en"]
name_jp = pokedex[index_poke]["name"]["jp"]
img = pokedex[index_poke]["sprites"]["regular"]
hp = pokedex[index_poke]["stats"]["hp"]
atk = pokedex[index_poke]["stats"]["atk"]
defence = pokedex[index_poke]["stats"]["def"]
spe_atk = pokedex[index_poke]["stats"]["spe_atk"]
vit = pokedex[index_poke]["stats"]["vit"]
spe_def = pokedex[index_poke]["stats"]["spe_def"]
height = pokedex[index_poke]["height"]
weight = pokedex[index_poke]["weight"]

if local == FR:
    html_carac = f"""
                        <span style="font-size: 20px; font-weight: bold">Mensurations</span><br>
                        Taille : {height}<br>
                        Poid : {weight}<br><br>

                        <span style="font-size: 20px; font-weight: bold">Stats</span><br>
                        Points de vie : {hp}<br>
                        Attaque : {atk}<br>
                        Défense : {defence}<br>
                        Attaque Spé : {spe_atk}<br>
                        Défense Spé : {spe_def}<br>
                        Vitesse : {vit}<br>
                        """
else:
    html_carac = f"""
                    <span style="font-size: 20px; font-weight: bold">Measurements</span><br>
                    Height : {height}<br>
                    Weight : {weight}<br>
                    <br>
                    <span style="font-size: 20px; font-weight: bold">Stats</span><br>
                    Hit points : {hp}<br>
                    Attack : {atk}<br>
                    Defense : {defence}<br>
                    Spe Attack : {spe_atk}<br>
                    Spe Defense : {spe_def}<br>
                    Speed : {vit}<br>
                    """

if pokedex[index_poke]["types"]:
    if len(pokedex[index_poke]["types"]) == 1:
        type1 = pokedex[index_poke]["types"][0]["image"]
    else:
        type1 = pokedex[index_poke]["types"][0]["image"]
        type2 = pokedex[index_poke]["types"][1]["image"]

col1, col2, col3 = st.columns([1, 1, 1], vertical_alignment="center")

with col1:
    st.header(name_fr)
with col2:
    st.header(name_en)
with col3:
    st.header(name_jp)

col1, col2 = st.columns([2, 1], vertical_alignment="center")

with col1:
    st.image(img)
with col2:
    st.markdown(
        """<span style="font-size: 20px; font-weight: bold">Type</span>""",
        unsafe_allow_html=True,
    )
    if pokedex[index_poke]["types"]:
        if len(pokedex[index_poke]["types"]) == 1:
            st.image(type1)
        else:
            st.image(type1)
            st.image(type2)
    st.markdown(html_carac, unsafe_allow_html=True)
