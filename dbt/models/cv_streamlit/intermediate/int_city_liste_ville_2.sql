SELECT
    unique_city_id,
    formated_cleaned_ville,
FROM
{{ ref('int_city_liste_ville') }}
WHERE rn = 1