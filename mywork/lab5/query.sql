use ratfeeder;
select rats.*, cookies.type_of_cookie, cookies.diameter from rats left join cookies on rats.cookieid = cookies.cookieid where rats.rat_weight < 600;
