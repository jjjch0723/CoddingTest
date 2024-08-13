-- 코드를 입력하세요
SELECT ai.animal_type, count(ai.animal_type) as count
  from animal_ins as ai
 group by ai.animal_type
 order by ai.animal_type