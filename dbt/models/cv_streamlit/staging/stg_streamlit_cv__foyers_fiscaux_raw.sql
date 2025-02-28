with 

source as (

    select * from {{ source('streamlit_cv', 'foyers_fiscaux_raw') }}

),

renamed as (

    select
        date,
        departement,
        id_ville,
        ville,
        n_foyers_fiscaux,
        revenu_fiscal_moyen,
        montant_impot_moyen

    from source

)

select * from renamed
