SELECT
    CONCAT(id_ville, '-', departement, "-", FORMAT_DATE('%Y', date_transaction)) AS id_city_dpt_year,
    CONCAT(id_ville,'-', departement) AS unique_city_id,
    FORMAT_DATE('%Y', date_transaction) AS date_year,
    departement,
    id_transaction,
    type_batiment,
    CASE WHEN vefa = TRUE THEN 1 ELSE 0 END AS vefa,
    prix,
    surface_habitable,
    SAFE_DIVIDE(prix, surface_habitable) as avg_price_squaredmetters,
    latitude,
    longitude
FROM {{ ref('stg_streamlit_cv__transactions_raw') }}