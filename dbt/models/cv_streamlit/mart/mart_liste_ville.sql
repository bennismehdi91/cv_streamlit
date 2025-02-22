{{ config(materialized='table') }}

WITH coordinates AS (
    SELECT
        CONCAT(id_ville,'-', departement) AS unique_city_id,
        AVG(latitude) AS city_latitude,
        AVG(longitude) AS city_longitude
    FROM
    {{ ref('stg_streamlit_cv__transactions_raw') }}
    GROUP BY unique_city_id
)

SELECT
    lv.unique_city_id,
    lv.cleaned_ville,
    lv.departement,
    CONCAT(lv.cleaned_ville,' (', lv.departement, ')') AS formated_cleaned_ville,
    c.city_latitude,
    c.city_longitude
FROM
{{ ref('int_city_liste_ville') }} lv
LEFT JOIN coordinates c ON lv.unique_city_id = c.unique_city_id
WHERE rn = 1