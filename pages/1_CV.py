import streamlit as st
from pathlib import Path

FR = "Français"
EN = "English"
IMG = Path("./files/images")

with st.sidebar.expander("**Language**"):
    local = st.radio("Select Language / Sélectionnez la langue:", (FR, EN))

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
        st.markdown("**Nationalité :** Français")
        st.markdown("**LinkedIn :** www.linkedin.com/in/mehdibennis")
        st.markdown(
            "**Points forts :** Analytique, agile, flexible, créatif et sociable."
        )


#### ACTIVITE PRO

######### EASYPICKY
st.divider()
if local == EN:
    st.header(":briefcase: Professional Experience", anchor="pro")
else:
    st.header(":briefcase: Expériences professionnelles", anchor="pro")

st.divider()

col1, col2 = st.columns([10, 4], vertical_alignment="center")
with col1:
    st.markdown(
        "<span style='font-size:25px; font-weight:bold'>Customer Success Manager, EasyPicky</span>",
        unsafe_allow_html=True,
    )
with col2:
    st.image(str(IMG.joinpath("EP_logo_png.png")), use_container_width=True)

st.markdown("Montpellier, 2023-02 / 2024-09")

if local == EN:
    st.markdown(
        """
    - Responsible for managing EasyPicky customer accounts.
    - Introduced Customer Success best practices at EasyPicky: quarterly account reviews,
    satisfaction surveys, user roundtables.
    - Drafted new KPIs to track account success based on users’ data, from data gathering to analysis.
    - Worked closely with developers to improve EasyPicky’s solution based on customer and
    users’ feedback
    """
    )
else:
    st.markdown(
        """
    - Responsable de la gestion des comptes clients d'EasyPicky.
    - Introduction de meilleures pratiques Customer Success : bilans trimestriels des comptes, enquêtes de satisfaction, tables rondes avec les utilisateurs.
    - Rédaction de nouveaux KPI pour suivre le succès des comptes en se basant sur les données des utilisateurs, de la compilation des données brutes à l'analyse des résultats.
    - Collaboration étroite avec les développeurs pour améliorer la solution EasyPicky en se basant sur les retours clients et utilisateurs.
"""
    )

#### ALIDA - SOLUTION ENGINEERING

st.divider()
col1, col2 = st.columns([10, 4], vertical_alignment="center")
with col1:
    st.markdown(
        "<span style='font-size:25px; font-weight:bold'>Solution Engineer, Alida</span>",
        unsafe_allow_html=True,
    )
with col2:
    st.image(str(IMG.joinpath("Alida_logo.png")), use_container_width=True)

st.markdown("Montpellier (full remote), 2021-01 / 2023-02")

if local == EN:
    st.markdown(
        """
    - Collaborates with sales teams to identify and uncover customer's strategic objectives and CX opportunities
    - Maps the prospect’s business and technology needs to Alida's solutions and helps validate key use cases
    - Provides solution expertise through product demonstrations and technical consultation
    - Identifies opportunities for data integrations to enhance platform value and user adoption
    - Works collaboratively with Product Management and Product Marketing during the development, launch, and refinement of Alida products
    - Tech Product webinar host to prospects and customers
    """
    )
else:
    st.markdown(
        """
    - Collaboration avec les équipes de vente pour identifier les objectifs stratégiques du client et les opportunités CX.
    - Cartographier les besoins commerciaux et technologiques du prospect avec les solutions d'Alida et aider à valider les cas d'utilisation clés.
    - Fournir une expertise en matière de solutions par le biais de démonstrations de produits et de consultations techniques.
    - Identification les opportunités d'intégration de données afin d'améliorer la valeur de la plateforme et l'adoption par les utilisateurs.
    - Travail en collaboration avec le Product Management et le Product Marketing pendant le développement, le lancement et l'amélioration des produits Alida.
    - Animation de webinaire sur les produits Alida à destination des prospects et clients.
    """
    )

st.divider()
#### ALIDA - Senior CSM

col1, col2 = st.columns([10, 4], vertical_alignment="center")
with col1:
    st.markdown(
        "<span style='font-size:25px; font-weight:bold'>Senior Customer Success Manager, Alida</span>",
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
    - Responsible for managing 14 accounts across various verticals (insurance, utilities, retail, media, FMCG, charities. . . ) and focused on opportunities to develop them. Management of junior team workers.
    - **Product Champion:** In charge of gathering client feedbacks in order to improve our software, managing EAP and showcasing new features to customers.
    """
    )
else:
    st.markdown(
        """
    - Responsable de la gestion de 14 comptes dans divers secteurs (assurance, services publics, retail, médias, produits de grande consommation, organisations caritatives...) et des possibilités de les développer. Gestion d'une équipe de collaborateurs juniors.
    - **Product Champion:** Chargé de recueillir les feedback clients afin d'améliorer notre logiciel, de gérer l'adoption de nouvelles fonctionnalités et de présenter les nouvelles fonctionnalités aux clients.
    """
    )

st.divider()

#### Vision Critical CSM

col1, col2 = st.columns([10, 4], vertical_alignment="center")
with col1:
    st.markdown(
        "<span style='font-size:25px; font-weight:bold'>Customer Success Manager, Vision Critical</span>",
        unsafe_allow_html=True,
    )
with col2:
    st.image(str(IMG.joinpath("Vision-Critical-logo.jpg")), width=200)

st.markdown("""London & Paris, 2014-09 / 2017-09""")
if local == EN:
    st.markdown(
        """
    - Worked on many research (qual & quant): end-to-end projects from brief to questionnaire design, data analysis, reports, recommendation and insight workshops.
    - Managed all elements of the communities’ lifecycle, including recruitment, engagement, health and satisfaction, overall success and ROI.
    - Worked hand in hand with clients, in order to understand clearly their needs and help them to be successful.
    """
    )
else:
    st.markdown(
        """
    - A travaillé sur de nombreuses études (qualitatives et quantitatives) : phase de brief, conception du questionnaire, analyse des données, rapports, recommandations et aux ateliers de réflexion.
    - Gestion de tous les éléments du cycle de vie des communautés : recrutement, engagement, santé et satisfaction, critères de succès et validation du ROI.
    - Travailler en étroite collaboration avec les clients, afin de comprendre clairement leurs besoins et de les accompagner.
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
        st.markdown("- Data Analytics Bootcamp, Le Wagon, 2024")
    else:
        st.markdown("- Data Analytics Bootcamp, Le Wagon, 2024")

col1, col2 = st.columns([2, 15], vertical_alignment="center")
with col1:
    st.image(
        str(IMG.joinpath("logo_univ_mtp.png")), width=75
    )  ### use_container_width=True)
with col2:
    if local == EN:
        st.markdown(
            """
            - Master’s Degree in « Surveys and Consulting » M2CO, University of Montpellier, 2014
            - University Diploma in Market Research and Opinion Polls, University of Montpellier, 2014
            """
        )
    else:
        st.markdown(
            """
            - Master 2 « Métiers des études et du conseil » M2CO, Université de Montpellier, 2014
            - Diplôme universitaire en études de marché et d'opinion, Université de Montpellier, 2014
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

if local == EN:
    st.markdown(
        """
        - Python, specialization in data analytics : Pandas, Scikit Learn, Plotly, Matplotlib, Seaborn, python-pptx, Streamlit, requests, poetry
        - Advanced knowledge in SQL, worked on MySQL, Google BigQuery.
        - Dataviz : Looker, PowerBI, Apache Superset
        - Automation : Fivetran, Zapier, Airflow
        - Advanced knowledge in MS Excel, Word and PowerPoint
        - Knowledge in HTML, CSS
        """
    )
else:
    st.markdown(
        """
        - Python, spécialisations en analyse de données : Pandas, Scikit Learn, Plotly, Matplotlib, Seaborn, python-pptx, Streamlit, requests, poetry.
        - Connaissance avancée du langage SQL, travail sur MySQL, Google BigQuery.
        - Data visualisation : Looker, PowerBI, Apache Superset
        - Automatisation : Fivetran, Zapier, Airflow
        - Connaissances avancées en MS Excel, Word et PowerPoint
        - Connaissances en HTML, CSS
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
        - **French**: Native
        - **English**: Full professional proficiency
        - **Spanish**: Elementary level
        """
    )
else:
    st.markdown(
        """
        - **French**: Natif
        - **English**: Compétence professionnelle totale
        - **Spanish**: Niveau élémentaire
        """
    )
