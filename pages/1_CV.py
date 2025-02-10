import streamlit as st
from pathlib import Path

FR = "Français"
EN = "English"
DIR = Path("/home/mehdibennis/projects/lewagon/projet_elections/")
IMG = DIR.joinpath("images")

with st.sidebar.expander("Language"):
    local = st.radio("Select Language / Sélectionnez la langue:", (FR, EN))


st.title("Curriculum Vitae")

if local == EN:
    st.header(":information_source: Overall Information")
else:
    st.header(":information_source: Informations générales")

col1, col2 = st.columns([2, 5], vertical_alignment="center")

with col1:

    st.image(str(IMG.joinpath("photo_profil.jpg")), use_container_width=True)

with col2:
    if local == EN:
        st.markdown("**Name:** Mehdi Bennis")
        st.markdown("**Phone: +33 (0)6 95 38 14 40**")
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
    st.header(":briefcase: Professional Experience")
else:
    st.header(":briefcase: Expériences professionnelles")

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
    - Drafted new KPIs to track account success based on users’ data.
    - Worked closely with developers to improve EasyPicky’s solution based on customer and
    users’ feedback
    """
    )
else:
    st.markdown(
        """
    - Responsable de la gestion des comptes clients d'EasyPicky.
    - Introduction des meilleures pratiques en matière de réussite des clients chez EasyPicky : examens trimestriels des comptes, enquêtes de satisfaction, tables rondes avec les utilisateurs, enquêtes de satisfaction, tables rondes d'utilisateurs.
    - Rédaction de nouveaux KPI pour suivre le succès des comptes en se basant sur les données des utilisateurs.
    - Collaboration étroite avec les développeurs pour améliorer la solution EasyPicky sur la base des commentaires des clients et des utilisateurs.
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
    - xxxx
    - xxxx
    """
    )
else:
    st.markdown(
        """
    - xxxx but in french
    - xxxx but in french
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
    - xxxx
    - xxxx
    """
    )
else:
    st.markdown(
        """
    - xxxx but in french
    - xxxx but in french
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
    - xxxx
    - xxxx
    """
    )
else:
    st.markdown(
        """
    - xxxx but in french
    - xxxx but in french
"""
    )

if local == EN:
    st.subheader("Other experiences")
    st.markdown(
        """
    - bliblablou
    - bloublibla
    """
    )
else:
    st.subheader("Autres expériences")
    st.markdown(
        """
    - bliblablou
    - bloublibla but in french
"""
    )


#### ACTIVITE PRO

######### EASYPICKY
st.divider()
if local == EN:
    st.header(":male-student: Educational Background")
else:
    st.header(":male-student: Education")
st.divider()

col1, col2 = st.columns([10, 4], vertical_alignment="center")
with col1:
    st.markdown(
        "<span style='font-size:25px; font-weight:bold'>Data Analytics Bootcamp, Le Wagon</span>",
        unsafe_allow_html=True,
    )
with col2:
    st.image(str(IMG.joinpath("le-wagon.jpg")), width=200)

st.markdown("Toulouse, 2024-10 / 2024-12")
if local == EN:
    st.markdown(
        """
    - xxx
    - xxx
    - xxx
    - xxxx
    """
    )
else:
    st.markdown(
        """
    - xxxx
    - xxx
    - xxx
"""
    )
