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
_Updated 1/12/2021, 8:15pm_

Because of changes the schedules forced by the pandemic, resume-based rankings for college football are more difficult this year. Where for previous years, bias-free rankings using this method produce reasonable results, the lack of cross-conference play and full schedules complicate this year's rankings. The formula that I ended up using is:

1. All P5 teams start with a rating of 1500 and all G5 teams start with a rating of 1200. Other, non-FBS teams, if encountered in the schedule, are added to the table starting with a rating of 800. All teams start with a rating deviation of 600 and a volatility of 0.6.
2. The 2019 schedule is run through 1 time to give initial ratings. Note that, after this run, the RD remains high and so the ratings are still quite fluid.
3. The 2020 schedule is run through 50 times.

Thanks to [https://collegefootballdata.com](https://collegefootballdata.com) for the game data tables.

### NFL
| Rank  | Team                       | Record   | Rating |
| ---:  | ---:                       | :---     | ---:   |
| 1     | Kansas City Chiefs         | 14-2     | 1916   |
| 2     | Buffalo Bills              | 14-3     | 1870   |
| 3     | New Orleans Saints         | 13-4     | 1742   |
| 4     | Green Bay Packers          | 13-3     | 1735   |
| 5     | Baltimore Ravens           | 12-5     | 1700   |
| 6     | Tampa Bay Buccaneers       | 12-5     | 1699   |
| 7     | Cleveland Browns           | 12-5     | 1668   |
| 8     | Pittsburgh Steelers        | 12-5     | 1657   |
| 9     | Seattle Seahawks           | 12-5     | 1648   |
| 10    | Miami Dolphins             | 10-6     | 1637   |
| 11    | Los Angeles Rams           | 11-6     | 1633   |
| 12    | Indianapolis Colts         | 11-6     | 1621   |
| 13    | Tennessee Titans           | 11-6     | 1617   |
| 14    | Las Vegas Raiders          | 8-8      | 1554   |
| 15    | New England Patriots       | 7-9      | 1500   |
| 16    | Los Angeles Chargers       | 7-9      | 1499   |
| 17    | Arizona Cardinals          | 8-8      | 1476   |
| 18    | Chicago Bears              | 8-9      | 1453   |
| 19    | San Francisco 49ers        | 6-10     | 1432   |
| 20    | Minnesota Vikings          | 7-9      | 1425   |
| 21    | Denver Broncos             | 5-11     | 1418   |
| 22    | Washington Football Team   | 7-10     | 1405   |
| 23    | New York Giants            | 6-10     | 1403   |
| 24    | Dallas Cowboys             | 6-10     | 1367   |
| 25    | Carolina Panthers          | 5-11     | 1365   |
| 26    | Atlanta Falcons            | 4-12     | 1334   |
| 27    | Philadelphia Eagles        | 4-11-1   | 1317   |
| 28    | Cincinnati Bengals         | 4-11-1   | 1317   |
| 29    | Detroit Lions              | 5-11     | 1301   |
| 30    | Houston Texans             | 4-12     | 1252   |
| 31    | New York Jets              | 2-14     | 1246   |
| 32    | Jacksonville Jaguars       | 1-15     | 955    |
_Updated 1/12/2021, 8:15pm_

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Gonzaga              | WCC        | 12-0     | 3208   |
| 2     | Michigan             | Big 10     | 10-0     | 3002   |
| 3     | Baylor               | Big 12     | 11-0     | 2946   |
| 4     | Winthrop             | Big South  | 11-0     | 2709   |
| 5     | Drake                | MVC        | 13-0     | 2685   |
| 6     | Texas                | Big 12     | 10-1     | 2659   |
| 7     | Kansas               | Big 12     | 10-2     | 2618   |
| 8     | Iowa                 | Big 10     | 11-2     | 2544   |
| 9     | Villanova            | Big East   | 8-1      | 2541   |
| 10    | The Citadel          | Southern   | 8-0      | 2535   |
| 11    | Clemson              | ACC        | 9-1      | 2466   |
| 12    | Louisville           | ACC        | 8-1      | 2459   |
| 13    | Houston              | AAC        | 10-1     | 2445   |
| 14    | Tennessee            | SEC        | 9-1      | 2410   |
| 15    | Siena                | MAAC       | 4-0      | 2397   |
| 16    | Creighton            | Big East   | 10-2     | 2394   |
| 17    | Minnesota            | Big 10     | 10-4     | 2383   |
| 18    | Virginia Tech        | ACC        | 9-2      | 2383   |
| 19    | Wisconsin            | Big 10     | 10-2     | 2360   |
| 20    | UConn                | Big East   | 7-1      | 2357   |
| 21    | Boise St.            | MWC        | 11-1     | 2345   |
| 22    | Missouri             | SEC        | 7-2      | 2309   |
| 23    | Alabama A&M          | SWAC       | 2-0      | 2303   |
| 24    | Illinois             | Big 10     | 9-4      | 2293   |
| 25    | West Virginia        | Big 12     | 9-4      | 2267   |
_Updated 1/12/2021, 8:15pm_

Script for scraping data by [Luke Benz](https://github.com/lbenz730/NCAA_Hoops).
