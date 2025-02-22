WITH
    foyers AS (
        SELECT
        CONCAT(id_ville, '-', departement, '-', date) AS id_year_city,
        *
        FROM {{ ref('stg_streamlit_cv__foyers_fiscaux_raw') }}
    ),
    transactions AS (
        SELECT
        *
        FROM {{ ref('int_city_snapshot_1') }}
    )
SELECT
    t.*,
    f.ville,
    f.n_foyers_fiscaux,
    f.revenu_fiscal_moyen
FROM transactions t
LEFT JOIN foyers f ON t.id_year_city = f.id_year_city
ORDER BY departement, id_ville, date_year