with 

source as (

    select * from {{ source('streamlit_cv', 'transactions_raw') }}

),

renamed as (

    select
        prix,
        departement,
        id_ville,
        type_batiment,
        vefa,
        n_pieces,
        surface_habitable,
        year,
        month

    from source

)

select * from renamed
