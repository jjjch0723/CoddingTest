-- 코드를 입력하세요
# 조인조건 : aniaml_id, left or right join
# 테이블명 : animal_ins, animal_outs
# 검색어 : ai.name, ai.datetime
# 검색조건 : 입양을 못 간 동물 중 가장 오래 머물고 있는 동물 3마리 이름, 보호시작일
SELECT ai.name, ai.datetime
  from animal_ins as ai
 left join animal_outs as ao on ai.animal_id = ao.animal_id
 where ao.datetime is null
 order by ai.datetime asc
 limit 3