{{ config(materialized='table') }}

WITH
    dpt_metro_metrics AS (
        SELECT * FROM {{ ref('int_dpt_2') }}
    )
    
SELECT
    *
FROM dpt_metro_metrics
WHERE departement_int < 100