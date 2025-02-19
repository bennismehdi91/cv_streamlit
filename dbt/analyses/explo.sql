with 

source as (

    select * from {{ ref('stg_streamlit_cv__transactions_raw') }}

)

SELECT
    min(year),
    max(year),
FROM
    source