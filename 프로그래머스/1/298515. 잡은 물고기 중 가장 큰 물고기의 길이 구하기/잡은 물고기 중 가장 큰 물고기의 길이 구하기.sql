-- 코드를 작성해주세요
# select concat(max(fi.length), 'cm') as MAX_LENGHT
#   from fish_info as fi
#  group by fi.fish_type
 
 select concat(max(fi.length), 'cm') as MAX_LENGTH
   from fish_info as fi