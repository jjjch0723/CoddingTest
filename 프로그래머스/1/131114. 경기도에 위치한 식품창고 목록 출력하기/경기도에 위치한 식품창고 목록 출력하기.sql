-- 코드를 입력하세요
SELECT fw.warehouse_id as WAREHOUSE_ID, fw.warehouse_name as WAREHOUSE_NAME,
       fw.address as ADDRESS, ifnull(fw.freezer_yn, 'N') as FREEZER_YN
  from food_warehouse as fw
 where fw.warehouse_name like '창고_경기%'