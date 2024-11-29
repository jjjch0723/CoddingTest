-- 코드를 입력하세요
select MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
  from MEMBER_PROFILE
 where GENDER = 'W' and TLNO is not null and DATE_FORMAT(DATE_OF_BIRTH, '%m') = '03'
 order by MEMBER_ID;