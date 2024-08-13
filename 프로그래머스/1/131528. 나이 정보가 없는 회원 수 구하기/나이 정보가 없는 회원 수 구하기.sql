-- 코드를 입력하세요
SELECT count(ui.user_id) as 'USERS'
  from user_info as ui
 where ui.age is null