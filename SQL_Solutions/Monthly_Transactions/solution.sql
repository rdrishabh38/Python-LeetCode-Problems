SELECT Date_format(trans_date, '%Y-%m') AS month,
       country,
       Count(1)                         AS trans_count,
       Sum(CASE
             WHEN state = 'approved' THEN 1
             ELSE 0
           end)                         AS approved_count,
       Sum(amount)                      AS trans_total_amount,
       Sum(CASE
             WHEN state = 'approved' THEN amount
             ELSE 0
           end)                         AS approved_total_amount
FROM   transactions
GROUP  BY Date_format(trans_date, '%Y-%m'),
          country 
