-- 코드를 입력하세요
SELECT ai.animal_id, ai.animal_type, ai.datetime, ai.intake_condition, 
       ai.name, ai.sex_upon_intake
  from animal_ins as ai
 order by ai.animal_id