-- 코드를 작성해주세요
# '스킬코드 2진수 비트연산자 사용'
# 검색조건 : skillcode 테이블의 col값이 "Front End"
# id 기준 오름차순 

-- row가 여러줄 나옴
# select dp.id, dp.email, dp.first_name, dp.last_name
#   from developers as dp
#  inner join skillcodes as sc 
#     on (sc.code & dp.skill_code) = sc.code
#  where sc.category = 'Front End'
#  order by dp.id asc

select dp.id, dp.email, dp.first_name, dp.last_name
  from developers dp
 where exists (
    select 1
     from skillcodes sc
    where (sc.code & dp.skill_code) = sc.code
      and sc.category = 'Front End'
 )
 order by dp.id asc