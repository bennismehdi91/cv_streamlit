WITH
    transactions AS (
        SELECT * FROM {{ ref('stg_streamlit_cv__transactions_raw') }}
    )
SELECT
    departement,
    CAST(departement AS int) AS departement_int,
    FORMAT_DATE('%Y', date_transaction) AS date_year,
    COUNT(id_transaction) as count_transaction,
    CAST(ROUND(AVG(prix),0) AS int) as avg_price,
    CAST(ROUND(AVG(SAFE_DIVIDE(prix, surface_habitable)),0) AS int) as avg_price_squaredmetters
FROM transactions
GROUP BY departement, date_year