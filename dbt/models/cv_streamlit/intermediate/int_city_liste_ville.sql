WITH
    clean AS(
        SELECT
            unique_city_id,
            TRANSLATE(
                UPPER(ville),
                'ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜÝ',
                'AAAAAACEEEEIIIIOOOOOUUUUY'
            ) AS cleaned_ville
        FROM {{ ref('int_city_snapshot_2') }}
        WHERE ville IS NOT NULL
        ),
    count_table AS (
        SELECT
            unique_city_id,
            cleaned_ville,
            count(*) AS count_ville_name
        FROM clean
        GROUP BY unique_city_id, cleaned_ville
    )

SELECT
    unique_city_id,
    cleaned_ville,
    count_ville_name,
    ROW_NUMBER() OVER (PARTITION BY unique_city_id ORDER BY count_ville_name DESC) AS rn
FROM count_table