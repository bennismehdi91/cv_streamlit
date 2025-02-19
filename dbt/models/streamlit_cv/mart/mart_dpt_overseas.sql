{{ config(materialized='table') }}

WITH
    dpt_overseas AS (
        SELECT * FROM {{ ref('int_dpt_2') }}
    )
    
SELECT
    *
FROM dpt_overseas
WHERE departement_int > 100