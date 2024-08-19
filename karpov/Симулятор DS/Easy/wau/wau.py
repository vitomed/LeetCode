# WAU (weekly active users) – количество активных пользователей в неделю.

# В таблице находятся данные по активности пользователей нашего Симулятора.
# Одна строка = одна попытка решения каким-то студентом какой-то задачи.
# Задание
# 1. Напишите запрос с расчётом WAU за весь период скользящим окном в неделю с шагом в 1 день,
#  при этом текущая дата должна включаться в расчет.
# Например, для даты 07.09.2022 нужно рассчитать WAU за период с 01.09.2022 по 07.09.2022.
#
# 2. Название столбцов должно быть day и wau. Столбы должны идти именно в таком порядке.
# churn_submits состоит из колонок:
#
# submit_id – id события-попытки
# timestamp – время попытки
# user_id  – id пользователя
# task_id  – id задания
# submit – номер попытки
# score – балл за задание
# is_solved – решил/не решил

"""TODO:
WITH activity_per_day AS (
    -- Получаем список уникальных пользователей за каждый день
    SELECT
        DATE(timestamp) AS day,
        user_id
    FROM churn_submits
    GROUP BY day, user_id
),
wau_calculation AS (
    -- Рассчитываем WAU, используя скользящее окно в 7 дней
    SELECT
        day,
        COUNT(DISTINCT user_id) OVER (
            ORDER BY day
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW -- Скользящее окно в 7 дней (включая текущий день)
        ) AS wau
    FROM activity_per_day
)
-- Финальный результат
SELECT
    day,
    wau
FROM wau_calculation
ORDER BY day;
"""