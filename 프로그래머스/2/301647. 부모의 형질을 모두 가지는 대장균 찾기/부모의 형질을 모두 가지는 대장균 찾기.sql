-- 코드를 작성해주세요 
select ed.id, ed.genotype, ed_.genotype as parent_genotype
  from ecoli_data as ed
  inner join ecoli_data as ed_ on ed.parent_id = ed_.id
 where (ed.genotype & ed_.genotype) = ed_.genotype
 order by ed.id
 