-- 코드를 입력하세요
SELECT ai.animal_type as ANIMAL_TYPE, ifnull(ai.name, 'No name') as NAME,
       ai.sex_upon_intake as SEX_UPON_INTAKE
  from animal_ins as ai