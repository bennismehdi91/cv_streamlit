with 

source as (

    select * from {{ source('streamlit_cv', 'transactions_raw') }}

),

renamed as (

    select
        id_transaction,
        date_transaction,
        prix,
        departement,
        id_ville,
        type_batiment,
        vefa,
        n_pieces,
        surface_habitable,
        latitude,
        longitude

    from source

)

select * from renamed
