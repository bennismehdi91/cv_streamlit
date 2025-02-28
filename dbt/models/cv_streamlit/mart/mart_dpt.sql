{{ config(materialized='table') }}

WITH
    dpt AS (
        SELECT * FROM {{ ref('int_dpt_2') }}
    )
    
SELECT
    *
FROM dpt