{{ config(materialized='table') }}

SELECT * FROM {{ ref('int_city_snapshot_2') }}