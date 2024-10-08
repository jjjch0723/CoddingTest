-- 코드를 입력하세요
SELECT  ch.CAR_ID,
        ROUND(AVG(DATEDIFF(ch.END_DATE, ch.START_DATE) + 1), 1) AS AVERAGE_DURATION
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as ch
  GROUP BY ch.CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, ch.CAR_ID DESC;