-- 코드를 입력하세요
# 조인 조건 : animla_id
# 검색어 : animal_id, name
# 테이블 명 : animal_ins, animal_outs
# 조건 : ai.datetime(보호시작일)보다 ao.datetime(입양일)이 더 빠른 row 탐색, 보호시작일이 빠른순으로 조회
SELECT ai.animal_id, ai.name
  from animal_ins as ai
 inner join animal_outs as ao on ai.animal_id = ao.animal_id
 where ai.datetime >= ao.datetime
 order by ai.datetime asc;
 