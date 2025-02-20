{{ config(materialized='table') }}

WITH
    city AS (
        SELECT * FROM {{ ref('int_city_liste_ville') }}
    )
    
SELECT
    *
FROM city