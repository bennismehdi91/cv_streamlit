import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="CV",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

FR = "Français"
EN = "English"
IMG = Path("./files/images")

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

if local == EN:
    st.sidebar.markdown(
        """
        ## Sections
    <ul>
        <li><a href="#info">Orverall Informations</a></li>
        <li><a href="#pro">Professional Experience</a></li>
        <li><a href="#educ">Educational Background</a></li>
        <li><a href="#skill">Skills</a></li>
        <li><a href="#language">Languages</li>
        <li><a href="#hobbie">Hobbies</li>
    </ul>
    """,
        unsafe_allow_html=True,
    )
else:
    st.sidebar.markdown(
        """
        ## Sections
    <ul>
        <li><a href="#info">Informations générales</a></li>
        <li><a href="#pro">Expériences professionnelles</a></li>
        <li><a href="#educ">Education</a></li>
        <li><a href="#skill">Compétences</a></li>
        <li><a href="#language">Langues</li>
        <li><a href="#hobbie">Loisirs</li>
    </ul>
    """,
        unsafe_allow_html=True,
    )


st.title("Curriculum Vitae")

if local == EN:
    st.header(":information_source: Overall Information", anchor="info")
else:
    st.header(":information_source: Informations générales", anchor="info")

col1, col2 = st.columns([2, 5], vertical_alignment="center")

with col1:

    st.image(str(IMG.joinpath("photo_profil.jpg")), use_container_width=True)

with col2:
    if local == EN:
        st.markdown("**Name:** Mehdi Bennis")
        st.markdown("**Phone:** +33 (0)6 95 38 14 40")
        st.markdown("**Email:** bennismehdi91@gmail.com")
        st.markdown("**Address:** 4 rue Guillaume de Nogaret, 34070, Montpellier")
        st.markdown("**Nationality:** French")
        st.markdown("**LinkedIn:** www.linkedin.com/in/mehdibennis")
        st.markdown(
            "**Strong points:** Strong analytical focus, agile and flexible, creative and sociable."
        )
    else:
        st.markdown("**Nom :** Mehdi Bennis")
        st.markdown("**Téléphone :** +33 (0)6 95 38 14 40")
        st.markdown("**Email :** bennismehdi91@gmail.com")
        st.markdown("**Adresse :** 4 rue Guillaume de Nogaret, 34070, Montpellier")
        st.markdown("**Nationalité :** Française")
        st.markdown("**LinkedIn :** www.linkedin.com/in/mehdibennis")
        st.markdown(
            "**Points forts :** Analytique, agile, flexible, créatif et sociable."
        )

st.divider()


with open("./files/cv_pdf/CV_MehdiBennis_2025.pdf", "rb") as file:
    pdf_data = file.read()

if local == EN:
    download_txt_button = "Download English CV"
else:
    download_txt_button = "Télécharger le CV en anglais"

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    pass
with col2:
    st.download_button(
        label=download_txt_button,
        data=pdf_data,
        file_name="CV_MehdiBennis_2025.pdf",
        mime="application/pdf",
    )
with col3:
    pass
#### ACTIVITE PRO

st.divider()
if local == EN:
    st.header(":briefcase: Professional Experience", anchor="pro")
else:
    st.header(":briefcase: Expériences professionnelles", anchor="pro")

######### Recherche

st.divider()

col1, col2 = st.columns([10, 4], vertical_alignment="center")
with col1:
    if local == EN:
        st.markdown(
            "<span style='font-size:25px; font-weight:bold'>Research Engineering</span>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<span style='font-size:25px; font-weight:bold'>Ingénierie de recherche</span>",
            unsafe_allow_html=True,
        )
with col2:
    st.markdown(
        "<div style='text-align: right; width:100%;'><span style='font-size:25px; font-weight:bold;'>Freelance</span></div>",
        unsafe_allow_html=True,
    )

if local == EN:
    date = "Montpellier, since february 2025"
else:
    date = "Montpellier, depuis Février 2025"

st.markdown(date)

if local == EN:
    st.markdown(
        """
    - Research engineering in collaboration with a political science university researcher
    - **Creation and processing of databases** based on election results. **Implementation of ad hoc solutions** to meet the researcher's needs
    """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
    - Ingénierie de recherche en collaboration avec une maîtresse de conférence en sciences politiques
    - **Création et traitement de bases de données** basées sur les résultats électoraux. **Mise en place de solutions ad hoc** pour répondre aux besoins de la chercheuse
    """,
        unsafe_allow_html=True,
    )

######### EASYPICKY

st.divider()

col1, col2 = st.columns([10, 4], vertical_alignment="center")
with col1:
    st.markdown(
        "<span style='font-size:25px; font-weight:bold'>Customer Success Manager</span>",
        unsafe_allow_html=True,
    )
with col2:
    st.image(str(IMG.joinpath("EP_logo_png.png")), use_container_width=True)

st.markdown("Montpellier, 2023-02 / 2024-09")

if local == EN:
    st.markdown(
        """
    - Responsible for managing EasyPicky customer accounts. **Introduced Customer Success best practices to the company**: quarterly account reviews,
    satisfaction surveys, user roundtables
    - **Drafted new KPIs to track account success** based on users’ data, from data gathering to analysis
    - **Worked closely with developers** to improve EasyPicky’s solution based on customer and
    users’ feedback
    """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
    - Responsable de la gestion des comptes clients d'EasyPicky. **Mise en place de meilleures pratiques Customer Success** : bilans trimestriels des comptes, enquêtes de satisfaction, tables rondes avec les utilisateurs
    - **Création de nouveaux KPI pour suivre le succès des comptes** en se basant sur les données des utilisateurs : de la compilation des données brutes à l'analyse des résultats
    - **Collaboration étroite avec les développeurs** pour améliorer la solution EasyPicky en se basant sur les retours clients et utilisateurs
"""
    )

#### ALIDA - SOLUTION ENGINEERING

st.divider()
col1, col2 = st.columns([10, 4], vertical_alignment="center")
with col1:
    st.markdown(
        "<span style='font-size:25px; font-weight:bold'>Solution Engineer</span>",
        unsafe_allow_html=True,
    )
with col2:
    st.image(str(IMG.joinpath("Alida_logo.png")), use_container_width=True)

st.markdown("Montpellier (full remote), 2021-01 / 2023-02")

if local == EN:
    st.markdown(
        """
    - **Maps the prospect’s business and technology needs to Alida's solutions** and helps validate key use cases. **Work in collaboration with sales team** to close deals
    - Provides solution expertise through **product demonstrations** and **technical consultation**
    - **Works collaboratively with Product Management and Product Marketing** during the development, launch, and refinement of Alida solutions
    - **Conducting Tech Product webinar** for prospects and customers
    """
    )
else:
    st.markdown(
        """
    - **Cartographier les besoins commerciaux et technologiques du prospect avec les solutions d'Alida** et aider à valider les cas d'utilisation clés. **Travail en collaboration avec les équipes commerciales**
    - Fournir une expertise des solutions Alida par le biais de **démos produits** et de **consultations techniques**
    - **Travail en collaboration avec les équipes Product Management et Product Marketing** pendant le développement, le lancement et l'amélioration des solutions Alida
    - **Animation de webinaire** sur les solutions Alida à destination des prospects et clients
    """
    )

st.divider()
#### ALIDA - Senior CSM

col1, col2 = st.columns([10, 4], vertical_alignment="center")
with col1:
    st.markdown(
        "<span style='font-size:25px; font-weight:bold'>Senior Customer Success Manager</span>",
        unsafe_allow_html=True,
    )
with col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/f/f1/Alida_logo.png",
        use_container_width=True,
    )

st.markdown("Montpellier (full remote), 2017-09 / 2021-01")

if local == EN:
    st.markdown(
        """
    - **Responsible for managing 14 accounts** across various verticals (insurance, utilities, retail, media, FMCG, charities. . . ) and focused on opportunities to develop them. **Management of junior collaborators**.
    - **Product Champion:** In charge of gathering client feedbacks in order to improve our software, managing EAP and showcasing new features to customers.
    """
    )
else:
    st.markdown(
        """
    - **Responsable de la gestion de 14 comptes** dans divers secteurs (assurance, services publics, retail, médias, produits de grande consommation, organisations caritatives...) et des possibilités de les développer. **Management de collaborateurs juniors**
    - **Product Champion :** Chargé de recueillir les feedback clients afin d'améliorer nos solutions, de gérer l'adoption de nouvelles fonctionnalités et de présenter les innovations aux clients.
    """
    )

st.divider()

#### Vision Critical CSM

col1, col2 = st.columns([10, 4], vertical_alignment="center")
with col1:
    st.markdown(
        "<span style='font-size:25px; font-weight:bold'>Customer Success Manager</span>",
        unsafe_allow_html=True,
    )
with col2:
    st.image(str(IMG.joinpath("Vision-Critical-logo.jpg")), width=200)

st.markdown("""London & Paris, 2014-09 / 2017-09""")
if local == EN:
    st.markdown(
        """
    - **Worked on many research (qual & quant)**: end-to-end projects from brief to questionnaire design, data analysis, reports, recommendation and insight workshops.
    - **Managed all elements of the communities’ lifecycle**, including recruitment, engagement, health and satisfaction, overall success and ROI.
    - **Worked hand in hand with clients**, in order to understand clearly their needs and help them to be successful.
    """
    )
else:
    st.markdown(
        """
    - **A travaillé sur de nombreuses études (qualitatives et quantitatives)** : phase de brief, conception du questionnaire, analyse des données, rapports, recommandations et aux ateliers de réflexion
    - **Gestion de tous les éléments du cycle de vie des communautés** : recrutement, engagement, santé et satisfaction, critères de succès et validation du ROI
    - **Travailler en étroite collaboration avec les clients**, afin de comprendre clairement leurs besoins et de les accompagner
"""
    )


#### Etudes

st.divider()
if local == EN:
    st.header(":male-student: Educational Background", anchor="educ")
else:
    st.header(":male-student: Education", anchor="educ")
st.divider()

col1, col2 = st.columns([2, 15], vertical_alignment="center")
with col1:
    st.image(
        str(IMG.joinpath("logo_wagon.png")), width=75
    )  ### use_container_width=True)
with col2:
    if local == EN:
        st.markdown(
            """
                    - Data Analytics Bootcamp, Le Wagon, 2024
                    - RNCP Certification “Designer Developer in Artificial Intelligence and Big Data Analysis, Data Analysis option”
                    """
        )
    else:
        st.markdown(
            """
                    - Data Analytics Bootcamp, Le Wagon, 2024
                    - Certification RNCP "Concepteur Développeur en Intelligence Artificielle et Analyse Big Data, option Data Analyse"
                    """
        )

col1, col2 = st.columns([2, 15], vertical_alignment="center")
with col1:
    st.image(
        str(IMG.joinpath("logo_univ_mtp.png")), width=75
    )  ### use_container_width=True)
with col2:
    if local == EN:
        st.markdown(
            """
            - Master’s Degree in « Surveys and Consulting » M2CO, Political Science University of Montpellier, 2014
            - University Diploma in Market Research and Opinion Polls, Political Science University of Montpellier, 2014
            """
        )
    else:
        st.markdown(
            """
            - Master 2 « Métiers des études et du conseil » M2CO, Université de Science Politique de Montpellier, 2014
            - Diplôme universitaire en études de marché et d'opinion, Université de Science Politique de Montpellier, 2014
            """
        )
col1, col2 = st.columns([2, 15], vertical_alignment="center")
with col1:
    st.image(
        str(IMG.joinpath("logo_univ_prague.png")), width=75
    )  ### use_container_width=True)
with col2:
    if local == EN:
        st.markdown(
            "- First year of Master’s Degree in Political Science in Erasmus Exchange Program, at the Charles University of Prague. With first class honors, 2013"
        )
    else:
        st.markdown(
            "- Master 1 en sciences politiques, programme d'échange Erasmus à l'université Charles de Prague, mention Très Bien, 2013"
        )

col1, col2 = st.columns([2, 15], vertical_alignment="center")
with col1:
    st.image(
        str(IMG.joinpath("logo_univ_mtp.png")), width=75
    )  ### use_container_width=True)
with col2:
    if local == EN:
        st.markdown(
            """
            - Degree in Political Science, University of Montpellier, 2012
            """
        )
    else:
        st.markdown(
            """
            - Licence en sciences politiques, Université de Montpellier, 2012
            """
        )
col1, col2 = st.columns([2, 15], vertical_alignment="center")
with col1:
    st.image(
        str(IMG.joinpath("logo_educ.png")), width=75
    )  ### use_container_width=True)
with col2:
    if local == EN:
        st.markdown(
            """
            - Baccalauréat, equivalent « A » Level, Economic and Social section, 2009
            """
        )
    else:
        st.markdown(
            """
            - Baccalauréat économique et social, 2009
            """
        )

#### Skills

st.divider()
if local == EN:
    st.header(":toolbox: Skills", anchor="skill")
else:
    st.header(":toolbox: Compétences", anchor="skill")
st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    if local == EN:
        st.markdown(
            """
            ### Computing

            - **Python**: specialization in data analytics
            - Packages worked with : Pandas, Scikit Learn, Plotly, Matplotlib, Seaborn, python-pptx, streamlit, requests, Beautiful Soup, poetry...
            - **SQL**: worked on MySQL, Google BigQuery, DBT
            - **Dataviz**: Looker, PowerBi, Apache Superset
            - **Automation**: Fivetran, Zapier, Airflow
            - **Collaboration**: GitHub
            - Knowledge in **HTML, CSS**
            """
        )
    else:
        st.markdown(
            """
            ### Informatique

            - **Python**: spécialisation en data analytics
            - Packages utilisés : Pandas, Scikit Learn, Plotly, Matplotlib, Seaborn, python-pptx, streamlit, requests, Beautiful Soup, poetry...
            - **SQL**: a travaillé sur MySQL, Google BigQuery, DBT
            - **Dataviz**: Looker, PowerBi, Apache Superset
            - **Automation**: Fivetran, Zapier, Airflow
            - **Collaboration**: GitHub
            - Connaissances en **HTML, CSS**
            """
        )

with col2:
    if local == EN:
        st.markdown(
            """
            ### Project Management

            - Customer Success Project Management, from Project Kick Off to Renewal
            - Designing and analysing market research projects from brief to recommendation
            - Animation of training for students, coworkers and customers: Python for Data Analytics, Excel, Dataviz, Market Research
            - Advanced knowledge in **MS Excel, Word** and **PowerPoint**
            """
        )
    else:
        st.markdown(
            """
            ### Gestion de projet

            - Gestion des projets Customer SUccess, du lancement du projet à son renouvellement
            - Conception et analyse de projets d'études de marché, du briefing à la recommandation
            - Animation de formations pour les étudiants, les collaborateurs et les clients : Python pour l'analyse de données, Excel, Dataviz, études de marché.
            - Connaissances avancées en **MS Excel, Word** et **PowerPoint**.
            """
        )


#### Languages

st.divider()
if local == EN:
    st.header(":speaking_head_in_silhouette: Languages", anchor="language")
else:
    st.header(":speaking_head_in_silhouette: Langues", anchor="language")
st.divider()


if local == EN:
    st.markdown(
        """
        - :fr: **French**: Native
        - :uk: **English**: Full professional proficiency
        - :es: **Spanish**: Elementary level
        """
    )
else:
    st.markdown(
        """
        - :fr: **Français** : Natif
        - :uk: **Anglais** : Compétence professionnelle totale
        - :es: **Espagnol** : Niveau élémentaire
        """
    )

#### Hobbies

st.divider()
if local == EN:
    st.header(":video_game: Hobbies", anchor="hobbie")
else:
    st.header(":video_game: Loisirs", anchor="hobbie")
st.divider()

if local == EN:
    st.markdown(
        """
        - :musical_note: **Music enthusiast** : (Rock, Metal, Jazz, Hip Hop, Folk…). Self-taught guitar, bass and piano
        - :chess_pawn: **Chess & Role-Playing Games**
        """
    )
else:
    st.markdown(
        """
        - :musical_note: **Amateur de musique** : (Rock, Metal, Jazz, Hip Hop, Folk…). Apprentissage autodidacte de la basse, de la guitare et du piano
        - :chess_pawn: **Échecs & Jeux de rôle**
        """
    )
