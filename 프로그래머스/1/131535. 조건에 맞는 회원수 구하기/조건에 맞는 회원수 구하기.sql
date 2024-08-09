-- 코드를 입력하세요
SELECT count(user_id)
  from user_info
 where joined like "2021%"
   and age <= 29
   and age >= 20