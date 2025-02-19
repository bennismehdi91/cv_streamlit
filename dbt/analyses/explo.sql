WITH source AS (
    SELECT * FROM {{ ref('stg_streamlit_cv__transactions_raw') }}
)

SELECT
    date_transaction,
    FORMAT_DATE('%B %Y', date_transaction) AS date_month_year,
    departement
FROM source