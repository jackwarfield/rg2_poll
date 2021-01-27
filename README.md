# Reinforced Glicko-2 Poll

This poll is based on the Glicko-2 rating system [\(Glickman 2013\)](http://glicko.net/glicko/glicko2.pdf) to produce resume-based sports rankings.

### College Football
| Rank  | Team                 | Conference           | Record   | Rating |
| ---:  | ---:                 | ---:                 | ---:     | ---:   |
| 1     | Alabama              | SEC                  | 13-0     | 3252   |
| 2     | Ohio State           | Big Ten              | 7-1      | 2693   |
| 3     | Texas A&M            | SEC                  | 9-1      | 2616   |
| 4     | Clemson              | ACC                  | 10-2     | 2287   |
| 5     | Notre Dame           | ACC			      | 10-2     | 2279   |
| 6     | Georgia              | SEC                  | 8-2      | 2235   |
| 7     | Coastal Carolina     | Sun Belt             | 11-1     | 2167   |
| 8     | Oklahoma             | Big 12               | 9-2      | 2140   |
| 9     | Louisiana            | Sun Belt             | 10-1     | 2134   |
| 10    | Florida              | SEC                  | 8-4      | 2072   |
| 11    | Cincinnati           | American Athletic    | 9-1      | 2064   |
| 12    | Iowa State           | Big 12               | 9-3      | 2052   |
| 13    | Ball State           | Mid-American         | 7-1      | 2032   |
| 14    | BYU                  | FBS Independents     | 11-1     | 2021   |
| 15    | Northwestern         | Big Ten              | 7-2      | 2019   |
| 16    | Liberty              | FBS Independents     | 10-1     | 1988   |
| 17    | Oklahoma State       | Big 12               | 8-3      | 1943   |
| 18    | San José State       | Mountain West        | 7-1      | 1941   |
| 19    | Auburn               | SEC                  | 6-5      | 1935   |
| 20    | Texas                | Big 12               | 7-3      | 1931   |
| 21    | Indiana              | Big Ten              | 6-2      | 1925   |
| 22    | Buffalo              | Mid-American         | 6-1      | 1916   |
| 23    | LSU                  | SEC                  | 5-5      | 1874   |
| 24    | Miami		           | Mid-American         | 2-1      | 1867   |
| 25    | USC                  | Pac-12               | 5-1      | 1833   |
_Updated 1/27/2021, 10:00am_

Because of changes the schedules forced by the pandemic, resume-based rankings for college football are more difficult this year. Where for previous years, bias-free rankings using this method produce reasonable results, the lack of cross-conference play and full schedules complicate this year's rankings. The formula that I ended up using is:

1. All P5 teams start with a rating of 1500 and all G5 teams start with a rating of 1200. Other, non-FBS teams, if encountered in the schedule, are added to the table starting with a rating of 800. All teams start with a rating deviation of 600 and a volatility of 0.6.
2. The 2019 schedule is run through 1 time to give initial ratings. Note that, after this run, the RD remains high and so the ratings are still quite fluid.
3. The 2020 schedule is run through 50 times.

Thanks to [https://collegefootballdata.com](https://collegefootballdata.com) for the game data tables.

### NFL
| Rank  | Team                       | Record   | Rating |
| ---:  | ---:                       | :---     | ---:   |
| 1     | Kansas City Chiefs         | 16-2     | 1992   |
| 2     | Buffalo Bills              | 15-4     | 1868   |
| 3     | Tampa Bay Buccaneers       | 14-5     | 1779   |
| 4     | Green Bay Packers          | 14-4     | 1731   |
| 5     | New Orleans Saints         | 13-5     | 1723   |
| 6     | Baltimore Ravens           | 12-6     | 1678   |
| 7     | Cleveland Browns           | 12-6     | 1652   |
| 8     | Pittsburgh Steelers        | 12-5     | 1649   |
| 9     | Seattle Seahawks           | 12-5     | 1644   |
| 10    | Miami Dolphins             | 10-6     | 1640   |
| 11    | Indianapolis Colts         | 11-6     | 1618   |
| 12    | Los Angeles Rams           | 11-7     | 1613   |
| 13    | Tennessee Titans           | 11-6     | 1612   |
| 14    | Las Vegas Raiders          | 8-8      | 1565   |
| 15    | Los Angeles Chargers       | 7-9      | 1510   |
| 16    | New England Patriots       | 7-9      | 1501   |
| 17    | Arizona Cardinals          | 8-8      | 1473   |
| 18    | Chicago Bears              | 8-9      | 1455   |
| 19    | Minnesota Vikings          | 7-9      | 1429   |
| 20    | San Francisco 49ers        | 6-10     | 1429   |
| 21    | Denver Broncos             | 5-11     | 1428   |
| 22    | Washington Football Team   | 7-10     | 1403   |
| 23    | New York Giants            | 6-10     | 1401   |
| 24    | Carolina Panthers          | 5-11     | 1374   |
| 25    | Dallas Cowboys             | 6-10     | 1363   |
| 26    | Atlanta Falcons            | 4-12     | 1343   |
| 27    | Cincinnati Bengals         | 4-11-1   | 1312   |
| 28    | Philadelphia Eagles        | 4-11-1   | 1312   |
| 29    | Detroit Lions              | 5-11     | 1304   |
| 30    | Houston Texans             | 4-12     | 1251   |
| 31    | New York Jets              | 2-14     | 1248   |
| 32    | Jacksonville Jaguars       | 1-15     | 955    |
_Updated 1/27/2021, 10:00am_

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Gonzaga              | WCC        | 15-0     | 3142   |
| 2     | Baylor               | Big 12     | 14-0     | 3112   |
| 3     | Drake                | MVC        | 14-0     | 2732   |
| 4     | Winthrop             | Big South  | 15-0     | 2589   |
| 5     | Michigan             | Big 10     | 13-1     | 2492   |
| 6     | Houston              | AAC        | 13-1     | 2463   |
| 7     | Boise St.            | MWC        | 13-1     | 2384   |
| 8     | Villanova            | Big East   | 10-1     | 2379   |
| 9     | Oklahoma             | Big 12     | 10-4     | 2353   |
| 10    | Texas                | Big 12     | 11-3     | 2345   |
| 11    | Kansas               | Big 12     | 10-5     | 2327   |
| 12    | Iowa                 | Big 10     | 12-3     | 2318   |
| 13    | West Virginia        | Big 12     | 11-4     | 2295   |
| 14    | Florida St.          | ACC        | 9-2      | 2275   |
| 15    | Virginia             | ACC        | 11-2     | 2268   |
| 16    | Oklahoma St.         | Big 12     | 10-4     | 2244   |
| 17    | Texas Tech           | Big 12     | 11-5     | 2234   |
| 18    | Minnesota            | Big 10     | 11-5     | 2229   |
| 19    | Alabama              | SEC        | 14-3     | 2221   |
| 20    | BYU                  | WCC        | 13-3     | 2215   |
| 21    | Wisconsin            | Big 10     | 12-4     | 2213   |
| 22    | Ohio St.             | Big 10     | 12-4     | 2207   |
| 23    | Xavier               | Big East   | 10-2     | 2199   |
| 24    | Illinois             | Big 10     | 10-5     | 2180   |
| 25    | Clemson              | ACC        | 9-4      | 2169   |
_Updated 1/27/2021, 10:00am_

Script for scraping data by [Luke Benz](https://github.com/lbenz730/NCAA_Hoops).
One potential standing issue is that, because of the way the games are scraped, every game is actually considered twice when constructing the ranking. I don't think that this can actually be considered an objectively good or bad thing, but regardless it is probably something that I should fix eventually.
