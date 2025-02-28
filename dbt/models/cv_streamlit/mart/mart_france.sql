{{ config(materialized='table') }}

WITH
    france_metrics AS (
        SELECT * FROM {{ ref('int_france_metrics_2') }}
    )
    
SELECT
    *
FROM france_metrics