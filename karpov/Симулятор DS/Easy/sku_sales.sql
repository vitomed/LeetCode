

SELECT
    cal_date AS days,
    sum(cnt) AS sku
FROM
    transactions_another_one
GROUP BY
    cal_date
ORDER BY
    cal_date;