with weather_info as(
    select country_id, avg(weather_state) weat
    from weather
    where day between '2019-11-01' and '2019-11-30'
    group by country_id
)
select country_name,
case when weat<=15 then 'Cold'
     when weat>=25 then 'Hot'
     else 'Warm' end weather_type
from countries join weather_info using(country_id)
order by country_name;