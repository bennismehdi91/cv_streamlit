WITH
    dpt_region AS (
        SELECT * FROM {{ ref('stg_streamlit_cv__dpt_regions_raw') }}
    ),
    agg_dpt AS (
        SELECT * FROM {{ ref('int_dpt_1') }}
    )
    
SELECT
    agg_dpt.*,
    dr.dep_name,
    dr.region_name,
    dr.code_region
FROM agg_dpt
LEFT JOIN dpt_region dr ON dr.num_dep = agg_dpt.departement_int