SELECT
    revenue_fiscal_bracket,
    MIN(revenu_fiscal_moyen) AS mini,
    MAX(revenu_fiscal_moyen) AS maxi
FROM
{{ ref('int_city_snapshot_bench') }}
GROUP BY
revenue_fiscal_bracket
ORDER BY revenue_fiscal_bracket

    
    
    
    
    
-- revenue_fiscal_bracket
-- f.revenu_fiscal_moyen