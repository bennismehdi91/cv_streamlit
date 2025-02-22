SELECT
*,
NTILE(8) OVER (ORDER BY n_foyers_fiscaux) AS foyers_fiscaux_bracket,
NTILE(8) OVER (ORDER BY revenu_fiscal_moyen) AS revenue_fiscal_bracket
FROM
{{ ref('int_city_snapshot_2') }}
WHERE ville IS NOT NULL AND n_foyers_fiscaux IS NOT NULL AND revenu_fiscal_moyen IS NOT NULL