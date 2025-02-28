import streamlit as st

st.set_page_config(
    page_title=None,
    page_icon=None,
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items=None,
)

FR = "Français"
EN = "English"

with st.sidebar.expander("**Language**"):
    local = st.radio("Select Language / Sélectionnez la langue:", (FR, EN))

st.markdown(
    """<em>To swith to english, select English on dropdown menu "language" on the side panel.</em>""",
    unsafe_allow_html=True,
)

if local == FR:
    st.write(
        """
        # Portfolio - Mehdi Bennis

        ### Bienvenue sur mon Portfolio

        <span style="font-size: 20px;"> Après plus de 10 ans à travailler en tant que Customer Success Manager dans des entreprises de SaaS (Vision Critical, Alida, EasyPicky), j'ai décidé de me réorienter en Data Analyse. J'ai pour cela effectué le <a href="https://www.lewagon.com/fr/data-analytics-course" target="_blank">Bootcamp Data Analytics du Wagon </a> et je recherche actuellement un nouveau poste !</span>
        
        <span style="font-size: 20px;">Cette formation m'a permis de confirmer et développer des compétences techniques en lien avec la data analyse : transformation de données, automatisation et requêtes API, exploration en Python et SQL, machine learning, et data visualisation (Apache Superset, Looker, PowerBI).</span>

        <span style="font-size: 20px;">Enfin, j'ai décidé de mettre en ligne mon CV et quelques projets de data analyse en ligne, pour vous donner une idée de mes compétences. <b>Vous pouvez accéder aux différentes pages sur l'onglet à gauche de la page.</b></span>

        <span style="font-size: 20px;">L'ensemble du code pour ce projet est accessible sur GitHub : https://github.com/bennismehdi91/cv_streamlit
        Si vous avez des retours, n'hésitez pas à m'en faire part directement par email : bennismehdi91@gmail.com</span>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        # Portfolio - Mehdi Bennis

        ### Welcome to My Portfolio!

        <span style="font-size: 20px;"> After more than 10 years working as a Customer Success Manager in SaaS companies (Vision Critical, Alida, EasyPicky), I decided to transition into Data Analytics. To achieve this, I completed the <a href="https://www.lewagon.com/data-analytics-course" target="_blank">Le Wagon Data Analytics Bootcamp</a>, and I am currently looking for a new opportunity!</span>

        <span style="font-size: 20px;">This training allowed me to confirm and develop technical skills related to data analysis, including data transformation, automation and API queries, exploration in Python and SQL, machine learning, and data visualization (Apache Superset, Looker, PowerBI).</span>

        <span style="font-size: 20px;">Finally, I decided to put my resume and some data analysis projects online to give you an idea of my skills. You can access the different pages from the tab on the left side of the page.</span>

        <span style="font-size: 20px;">The full code for this project is available on GitHub: https://github.com/bennismehdi91/cv_streamlit.
        If you have any feedback, feel free to reach out to me directly via email: bennismehdi91@gmail.com</span>
        """,
        unsafe_allow_html=True,
    )
