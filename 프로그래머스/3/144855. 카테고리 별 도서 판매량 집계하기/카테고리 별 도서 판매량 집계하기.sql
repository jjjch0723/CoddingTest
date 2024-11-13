-- 코드를 입력하세요
# 조인조건 : book_id
# 테이블명 : book, book_sales
# 검색어 : category, total_sales, 도서별 판매량 합산
# 검색조건 : 2022년 1월의 도서 판매량, 카테고리명 기준 오름차순
SELECT b.category as CATEGORY, sum(bs.sales) as TOTAL_SALES
  from book_sales as bs
 inner join book as b on bs.book_id = b.book_id
 where bs.sales_date between '2022-01-01' and '2022-01-31'
 group by b.category
 order by b.category