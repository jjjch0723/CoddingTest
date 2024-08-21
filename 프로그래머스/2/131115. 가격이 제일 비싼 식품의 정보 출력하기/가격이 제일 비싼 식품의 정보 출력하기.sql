-- 코드를 입력하세요
# 조건 : 가격이 제일 비싼 식품의 id, 이름, 코드, 분류, 가격
# SELECT fb.product_id, fb.product_name, fb.product_cd, 
#        fb.category, max(fb.price) as price
#   from food_product as fb
#  group by fb.category
select fb.product_id, fb.product_name, fb.product_cd, 
       fb.category, fb.price
  from food_product as fb
 order by fb.price desc
 limit 1