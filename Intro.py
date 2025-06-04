"""
test to add something to main
"""

import streamlit as st

st.set_page_config(
    page_title="Introduction",
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

st.markdown(
    """<em>To switch to english, select English on dropdown menu "language" on the side panel.</em>""",
    unsafe_allow_html=True,
)

if local == FR:
    st.write(
        """
        # Portfolio - Mehdi Bennis

        ### Bienvenue sur mon Portfolio

        <span style="font-size: 20px;"> Après plus de 10 ans à travailler en tant que Customer Success Manager dans des entreprises de SaaS spécialisées en Etudes de Marché et IA (Vision Critical, Alida, EasyPicky), j'ai décidé d'approfondir mes compétences techniques. J'ai pour cela effectué le <a href="https://www.lewagon.com/fr/data-analytics-course" target="_blank">Bootcamp Data Analytics du Wagon </a> et je recherche actuellement un nouveau poste !</span>
        
        <span style="font-size: 20px;">Cette formation m'a permis de confirmer et développer des compétences techniques en lien avec la data analyse et le web : transformation de données, automatisation et requêtes API, exploration en Python et SQL, machine learning, et data visualisation (Apache Superset, Looker, PowerBI).</span>

        <span style="font-size: 20px;">Enfin, pour vous donner une idée de mes compétences, j'ai décidé de mettre en ligne mon CV et quelques projets. <b>Vous pouvez accéder aux différentes pages sur l'onglet à gauche de la page.</b></span>

        <span style="font-size: 20px;">L'ensemble du code de ce projet est accessible sur GitHub : https://github.com/bennismehdi91/cv_streamlit
        Si vous avez des retours, n'hésitez pas à m'en faire part directement par email : bennismehdi91@gmail.com</span>

        <span style="font-size: 14px;"><em>Si vous êtes sur mobile, cliquez sur la flêche en haut à gauche de la page pour ouvrir le menu.</em></span>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        # Portfolio - Mehdi Bennis

        ### Welcome to My Portfolio!

        <span style="font-size: 20px;"> After more than 10 years working as a Customer Success Manager in SaaS companies specialized in Market Research and AI (Vision Critical, Alida, EasyPicky), I decided to deepen my technical skills. To achieve this, I completed the <a href="https://www.lewagon.com/data-analytics-course" target="_blank">Le Wagon Data Analytics Bootcamp</a>, and I am currently looking for a new opportunity!</span>

        <span style="font-size: 20px;">This training allowed me to confirm and develop technical skills related to data analysis and web, including data transformation, automation and API queries, exploration in Python and SQL, machine learning, and data visualization (Apache Superset, Looker, PowerBI).</span>

        <span style="font-size: 20px;">Finally, to give you an idea of my skills, I decided to put my resume and some projects. You can access the different pages from the tab on the left side of the page.</span>

        <span style="font-size: 20px;">The full code for this project is available on GitHub: https://github.com/bennismehdi91/cv_streamlit.
        If you have any feedback, feel free to reach out to me directly via email: bennismehdi91@gmail.com</span>

        <span style="font-size: 14px;"><em>If you are on mobile, click on the arrow at the top left of the page to open the menu.</em></span>
        """,
        unsafe_allow_html=True,
    )
