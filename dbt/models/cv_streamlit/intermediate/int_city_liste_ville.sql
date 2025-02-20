WITH
    foyers AS (
        SELECT * FROM {{ ref('stg_streamlit_cv__foyers_fiscaux_raw') }}
    )
SELECT
    DISTINCT f.id_ville, f.ville
FROM foyers f
