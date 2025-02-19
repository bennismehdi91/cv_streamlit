 WITH source AS (
    SELECT * FROM {{ ref('stg_streamlit_cv__transactions_raw') }}
)
    SELECT
        FORMAT_DATE('%Y - %m', date_transaction) AS date_year_month,
        COUNT(id_transaction) as count_transaction,
        CAST(ROUND(AVG(prix),0) AS int) as avg_price,
        CAST(ROUND(AVG(SAFE_DIVIDE(prix, surface_habitable)),0) AS int) as avg_price_squaredmetters
    FROM source
    GROUP BY date_year_month
    ORDER BY date_year_month