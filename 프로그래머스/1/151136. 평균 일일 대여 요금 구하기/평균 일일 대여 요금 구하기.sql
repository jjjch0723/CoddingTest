-- 코드를 입력하세요
SELECT ROUND(sum(cr.daily_fee) /count(cr.daily_fee)) as AVERAGE_FEE
  from CAR_RENTAL_COMPANY_CAR as cr
 where cr.car_type like "SUV"