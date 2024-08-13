-- 코드를 입력하세요
SELECT cc.car_type as CAR_TYPE, count(*) as CARS
  from car_rental_company_car as cc
 where cc.options like '%통풍시트%' 
    or cc.options like '%열선시트%' 
    or cc.options like '%가죽시트%'
 group by cc.car_type
 order by cc.car_type asc