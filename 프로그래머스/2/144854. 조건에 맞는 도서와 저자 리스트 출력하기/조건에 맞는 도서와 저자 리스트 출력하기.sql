-- 코드를 입력하세요
# 조인 조건 author_id(integer)
# 경제 카테고리의 도서id, 저자명, 출판일 
SELECT bk.book_id as BOOK_ID, at.author_name as AUTHOR_NAME, 
       date_format(bk.published_date, '%Y-%m-%d') as PUBLISHED_DATE
  from book as bk
 inner join author as at on bk.author_id = at.author_id
 where bk.category like "경제"
 order by bk.published_date