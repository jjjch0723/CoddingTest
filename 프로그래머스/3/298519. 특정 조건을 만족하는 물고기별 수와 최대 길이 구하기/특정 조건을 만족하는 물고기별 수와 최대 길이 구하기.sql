-- 코드를 작성해주세요
# 잡은 수, 최대 길이, 물고기의 종류
#MAX(COALESCE(LENGTH, 10)) AS MAX_LENGTH
select count(fi.fish_type) as FISH_COUNT, max(coalesce(fi.length, 10)) as MAX_LENGTH, fi.fish_type as FISH_TYPE
  from fish_info as fi
 group by fi.fish_type
 having avg(coalesce(fi.length, 10)) > 32
 order by fi.fish_type


# select *
#   from fish_info
 