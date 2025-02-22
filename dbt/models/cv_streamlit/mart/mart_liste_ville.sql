{{ config(materialized='table') }}

WITH dpt AS (
    SELECT DISTINCT
        id_ville,
        departement,
        CONCAT(id_ville, '-',departement) AS unique_city_id
    FROM
    {{ ref('stg_streamlit_cv__foyers_fiscaux_raw') }}
)

SELECT
    lv.unique_city_id,
    lv.cleaned_ville,
    d.departement,
    CONCAT(lv.cleaned_ville,' (', d.departement, ')') AS formated_cleaned_ville
FROM
{{ ref('int_city_liste_ville') }} lv
LEFT JOIN dpt d ON lv.unique_city_id = d.unique_city_id
WHERE rn = 1