-- 코드를 입력하세요
# 조인 조건 : animal_id
# 데이터가 유실된 테이블 : animal_ins
# left혹은 right 조인 이용해서(left를 사용시 animal_out테이블을 from절에 사용) animal_ins에서 null 값 찾아내기
SELECT ao.animal_id, ao.name
  from animal_ins as ai
 right join animal_outs as ao on ai.animal_id = ao.animal_id
 where ai.animal_id is null
  
