select * from t_ponto;

-- registros por usuário
select
    t.username,
    count(1)
from t_ponto t
group by 1
order by 2 desc
;

--registros por dia
select
    date_trunc('day', t.insert_date)::date as insert_date,
    count(1)
from t_ponto t
group by 1
order by 2 desc
;

-- registros por empresa
select
    t.company,
    date_trunc('day', t.insert_date)::date as insert_date,
    count(1)
from t_ponto t
group by 1, 2
order by 1 desc
;
