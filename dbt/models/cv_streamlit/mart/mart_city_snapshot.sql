{{ config(materialized='table') }}

WITH liste_ville AS (
    SELECT * FROM {{ ref('int_city_liste_ville_2') }}
)

SELECT 
    city.*,
    lv.formated_cleaned_ville
FROM {{ ref('int_city_snapshot_2') }} city
LEFT JOIN liste_ville lv ON city.unique_city_id = lv.unique_city_id