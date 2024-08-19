WITH activity_per_day AS (
    SELECT
        DATE(timestamp) AS day,
        user_id
    FROM churn_submits
    GROUP BY day, user_id
),
wau_calculation AS (
    SELECT
        day,
        COUNT(DISTINCT user_id) OVER (
            ORDER BY day
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS wau
    FROM activity_per_day
)
SELECT
    day,
    wau
FROM wau_calculation
ORDER BY day;
