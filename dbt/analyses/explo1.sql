/*  Check unique ID of transactions


SELECT
    CONCAT(id_ville, '-', departement, '-', FORMAT_DATE('%Y', date_transaction)) AS unique_id,
    COUNT(*) AS nb_lines
FROM
    {{ ref('stg_streamlit_cv__transactions_raw') }}
GROUP BY
    id_ville, departement, date_transaction
HAVING
    COUNT(*) > 1

 Check unique ID of foyers_fiscaux
SELECT
    CONCAT(id_ville, '-', departement, '-', date) AS unique_id,
    COUNT(*) AS nb_lines
FROM
    {{ ref('stg_streamlit_cv__foyers_fiscaux_raw') }}
GROUP BY
    id_ville, departement, date
*/