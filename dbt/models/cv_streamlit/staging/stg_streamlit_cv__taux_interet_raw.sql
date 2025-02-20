with 

source as (

    select * from {{ source('streamlit_cv', 'taux_interet_raw') }}

),

renamed as (

    select
        date,
        taux

    from source

)

select * from renamed
