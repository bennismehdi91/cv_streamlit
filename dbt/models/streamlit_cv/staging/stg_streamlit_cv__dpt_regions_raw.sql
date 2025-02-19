with 

source as (

    select * from {{ source('streamlit_cv', 'dpt_regions_raw') }}

),

renamed as (

    select
        num_dep,
        dep_name,
        region_name,
        code_region

    from source

)

select * from renamed
