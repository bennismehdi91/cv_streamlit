SELECT
    CONCAT(id_ville, '-', departement, "-", FORMAT_DATE('%Y', date_transaction)) AS id_city_dpt_year,
    CONCAT(id_ville,'-', departement) AS unique_city_id,
    FORMAT_DATE('%Y', date_transaction) AS date_year,
    departement,
    COUNT(id_transaction) as count_transaction,
    SUM(CASE WHEN type_batiment = 'Maison' THEN 1 ELSE 0 END) AS count_maison,
    SUM(CASE WHEN type_batiment = 'Appartement' THEN 1 ELSE 0 END) AS count_appartement,
    SUM(CASE WHEN vefa = TRUE THEN 1 ELSE 0 END) AS count_vefa,
    CAST(AVG(CASE WHEN type_batiment = 'Maison' THEN prix ELSE NULL END) AS int) as avg_price_maison,
    CAST(AVG(CASE WHEN type_batiment = 'Appartement' THEN prix ELSE NULL END) AS int) as avg_price_appartement,
    CAST(AVG(CASE WHEN type_batiment = 'Maison' THEN surface_habitable ELSE NULL END) AS int) as avg_surface_maison,
    CAST(AVG(CASE WHEN type_batiment = 'Appartement' THEN surface_habitable ELSE NULL END) AS int) as avg_surface_appartement,
    CAST(ROUND(AVG(SAFE_DIVIDE(prix, surface_habitable)),0) AS int) as avg_price_squaredmetters
FROM {{ ref('stg_streamlit_cv__transactions_raw') }}
GROUP BY 
    id_city_dpt_year,
    unique_city_id,
    date_year,
    departement
