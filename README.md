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
_Updated 2/18/2021, 12:00pm_

Because of changes the schedules forced by the pandemic, resume-based rankings for college football are more difficult this year. Where for previous years, bias-free rankings using this method produce reasonable results, the lack of cross-conference play and full schedules complicate this year's rankings. The formula that I ended up using is:

1. All P5 teams start with a rating of 1500 and all G5 teams start with a rating of 1200. Other, non-FBS teams, if encountered in the schedule, are added to the table starting with a rating of 800. All teams start with a rating deviation of 600 and a volatility of 0.6.
2. The 2019 schedule is run through 1 time to give initial ratings. Note that, after this run, the RD remains high and so the ratings are still quite fluid.
3. The 2020 schedule is run through 50 times.

Thanks to [https://collegefootballdata.com](https://collegefootballdata.com) for the game data tables.

### NFL
| Rank  | Team                       | Record   | Rating |
| ---:  | ---:                       | :---     | ---:   |
| 1     | Kansas City Chiefs         | 16-3     | 1922   |
| 2     | Buffalo Bills              | 15-4     | 1858   |
| 3     | Tampa Bay Buccaneers       | 15-5     | 1832   |
| 4     | Green Bay Packers          | 14-4     | 1743   |
| 5     | New Orleans Saints         | 13-5     | 1735   |
| 6     | Baltimore Ravens           | 12-6     | 1675   |
| 7     | Cleveland Browns           | 12-6     | 1650   |
| 8     | Pittsburgh Steelers        | 12-5     | 1649   |
| 9     | Seattle Seahawks           | 12-5     | 1646   |
| 10    | Miami Dolphins             | 10-6     | 1637   |
| 11    | Indianapolis Colts         | 11-6     | 1620   |
| 12    | Los Angeles Rams           | 11-7     | 1618   |
| 13    | Tennessee Titans           | 11-6     | 1614   |
| 14    | Las Vegas Raiders          | 8-8      | 1565   |
| 15    | Los Angeles Chargers       | 7-9      | 1511   |
| 16    | New England Patriots       | 7-9      | 1500   |
| 17    | Arizona Cardinals          | 8-8      | 1476   |
| 18    | Chicago Bears              | 8-9      | 1463   |
| 19    | Minnesota Vikings          | 7-9      | 1436   |
| 20    | San Francisco 49ers        | 6-10     | 1432   |
| 21    | Denver Broncos             | 5-11     | 1429   |
| 22    | Washington Football Team   | 7-10     | 1408   |
| 23    | New York Giants            | 6-10     | 1404   |
| 24    | Carolina Panthers          | 5-11     | 1381   |
| 25    | Dallas Cowboys             | 6-10     | 1366   |
| 26    | Atlanta Falcons            | 4-12     | 1350   |
| 27    | Philadelphia Eagles        | 4-11-1   | 1315   |
| 28    | Cincinnati Bengals         | 4-11-1   | 1314   |
| 29    | Detroit Lions              | 5-11     | 1311   |
| 30    | Houston Texans             | 4-12     | 1254   |
| 31    | New York Jets              | 2-14     | 1248   |
| 32    | Jacksonville Jaguars       | 1-15     | 958    |
_Updated 2/18/2021, 12:00pm_

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Gonzaga              | WCC        | 21-0     | 3161   |
| 2     | Baylor               | Big 12     | 17-0     | 3137   |
| 3     | Michigan             | Big 10     | 15-1     | 2493   |
| 4     | Ohio St.             | Big 10     | 18-4     | 2311   |
| 5     | Oklahoma             | Big 12     | 13-5     | 2280   |
| 6     | Illinois             | Big 10     | 15-5     | 2269   |
| 7     | Texas                | Big 12     | 13-5     | 2225   |
| 8     | Iowa                 | Big 10     | 16-6     | 2221   |
| 9     | Florida St.          | ACC        | 12-3     | 2214   |
| 10    | West Virginia        | Big 12     | 14-6     | 2210   |
| 11    | Kansas               | Big 12     | 16-7     | 2210   |
| 12    | Virginia             | ACC        | 15-4     | 2185   |
| 13    | Texas Tech           | Big 12     | 14-6     | 2173   |
| 14    | Southern California  | Pac 12     | 18-3     | 2171   |
| 15    | Villanova            | Big East   | 13-3     | 2168   |
| 16    | Alabama              | SEC        | 17-5     | 2165   |
| 17    | Clemson              | ACC        | 13-5     | 2161   |
| 18    | Purdue               | Big 10     | 14-8     | 2155   |
| 19    | Oklahoma St.         | Big 12     | 14-6     | 2155   |
| 20    | Wisconsin            | Big 10     | 15-8     | 2135   |
| 21    | BYU                  | WCC        | 16-5     | 2133   |
| 22    | Rutgers              | Big 10     | 12-8     | 2123   |
| 23    | Creighton            | Big East   | 16-5     | 2119   |
| 24    | Maryland             | Big 10     | 13-10    | 2106   |
| 25    | Minnesota            | Big 10     | 13-9     | 2103   |
_Updated 2/18/2021, 12:00pm_

Script for scraping data by [Luke Benz](https://github.com/lbenz730/NCAA_Hoops).
One potential standing issue is that, because of the way the games are scraped, every game is actually considered twice when constructing the ranking. I don't think that this can actually be considered an objectively good or bad thing, but regardless it is probably something that I should fix eventually.
