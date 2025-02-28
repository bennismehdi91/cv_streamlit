WITH
    foyers AS (
        SELECT
        CONCAT(id_ville, '-', departement, '-', date) AS id_city_dpt_year,
        ville
        FROM {{ ref('stg_streamlit_cv__foyers_fiscaux_raw') }}
    )

SELECT
    t.*,
    f.ville
FROM {{ ref('int_city_snapshot_1') }} t
LEFT JOIN foyers f ON t.id_city_dpt_year = f.id_city_dpt_year