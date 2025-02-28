WITH
    transactions AS (
        SELECT * FROM {{ ref('int_france_metrics_1') }}
        
    )
    ,
    taux_interet AS (
        SELECT * FROM {{ ref('stg_streamlit_cv__taux_interet_raw') }}
    )
SELECT
    t.date_year_month,
    t.count_transaction,
    t.avg_price,
    t.avg_price_squaredmetters,
    ti.taux AS avg_interest_rate
FROM transactions t
LEFT JOIN taux_interet ti ON ti.date = t.date_year_month