-- 코드를 작성해주세요
# left 조인 이용
select year(a.DIFFERENTIATION_DATE) as YEAR, (b.SIZE-a.SIZE_OF_COLONY) as YEAR_DEV, a.ID
from ECOLI_DATA as a
left join (select year(DIFFERENTIATION_DATE) as YEAR, max(SIZE_OF_COLONY) as SIZE
        from ECOLI_DATA
        group by year(DIFFERENTIATION_DATE)) as  b
on year(a.DIFFERENTIATION_DATE)=b.YEAR
order by YEAR, YEAR_DEV