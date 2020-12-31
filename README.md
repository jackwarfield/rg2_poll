# Reinforced Glicko-2 Poll

This poll is based on the Glicko-2 rating system [\(Glickman 2013\)](http://glicko.net/glicko/glicko2.pdf) to produce resume-based sports rankings.

### College Football
| Rank  | Team                 | Conference           | Record   | Rating |
| ---:  | ---:                 | ---:                 | ---:     | ---:   |
| 1     | Alabama              | SEC                  | 11-0     | 2945   |
| 2     | Ohio State           | Big Ten              | 6-0      | 2823   |
| 3     | Cincinnati           | American Athletic    | 9-0      | 2551   |
| 4     | Clemson              | ACC                  | 10-1     | 2432   |
| 5     | Texas A&M            | SEC                  | 8-1      | 2411   |
| 6     | Notre Dame           | FBS Independents     | 10-1     | 2408   |
| 7     | San José State       | Mountain West        | 7-0      | 2364   |
| 8     | Indiana              | Big Ten              | 6-1      | 2322   |
| 9     | Coastal Carolina     | Sun Belt             | 11-1     | 2193   |
| 10    | Louisiana            | Sun Belt             | 10-1     | 2128   |
| 11    | Oklahoma             | Big 12               | 9-2      | 2077   |
| 12    | BYU                  | FBS Independents     | 11-1     | 2074   |
| 13    | Liberty              | FBS Independents     | 10-1     | 2038   |
| 14    | Iowa State           | Big 12               | 8-3      | 2001   |
| 15    | Georgia              | SEC                  | 7-2      | 1957   |
| 16    | Northwestern         | Big Ten              | 6-2      | 1941   |
| 17    | Oklahoma State       | Big 12               | 8-3      | 1937   |
| 18    | Texas                | Big 12               | 7-3      | 1898   |
| 19    | Tulsa                | American Athletic    | 6-2      | 1886   |
| 20    | Florida              | SEC                  | 8-4      | 1872   |
| 21    | Miami                | ACC                  | 8-3      | 1865   |
| 22    | USC                  | Pac-12               | 5-1      | 1857   |
| 23    | Iowa                 | Big Ten              | 6-2      | 1841   |
| 24    | North Carolina       | ACC                  | 8-3      | 1822   |
| 25    | Boise State          | Mountain West        | 5-2      | 1814   |
_Updated 12/31/2020, 1:00pm_

Because of changes the schedules forced by the pandemic, resume-based rankings for college football are more difficult this year. Where for previous years, bias-free rankings using this method produce reasonable results, the lack of cross-conference play and full schedules complicate this year's rankings. The formula that I ended up using is:

1. All P5 teams start with a rating of 1500 and all G5 teams start with a rating of 1200. Other, non-FBS teams, if encountered in the schedule, are added to the table starting with a rating of 800. All teams start with a rating deviation of 600 and a volatility of 0.6.
2. The 2019 schedule is run through 1 time to give initial ratings. Note that, after this run, the RD remains high and so the ratings are still quite fluid.
3. The 2020 schedule is run through 50 times.

Thanks to [https://collegefootballdata.com](https://collegefootballdata.com) for the game data tables.

### NFL
| Rank  | Team                       | Record   | Rating |
| ---:  | ---:                       | :---     | ---:   |
| 1     | Kansas City Chiefs         | 14-1     | 2051   |
| 2     | Buffalo Bills              | 12-3     | 1841   |
| 3     | Pittsburgh Steelers        | 12-3     | 1744   |
| 4     | Green Bay Packers          | 12-3     | 1716   |
| 5     | New Orleans Saints         | 11-4     | 1711   |
| 6     | Seattle Seahawks           | 11-4     | 1665   |
| 7     | Baltimore Ravens           | 10-5     | 1664   |
| 8     | Tampa Bay Buccaneers       | 10-5     | 1663   |
| 9     | Miami Dolphins             | 10-5     | 1649   |
| 10    | Tennessee Titans           | 10-5     | 1639   |
| 11    | Indianapolis Colts         | 10-5     | 1634   |
| 12    | Cleveland Browns           | 10-5     | 1583   |
| 13    | Los Angeles Rams           | 9-6      | 1572   |
| 14    | Las Vegas Raiders          | 7-8      | 1516   |
| 15    | Arizona Cardinals          | 8-7      | 1497   |
| 16    | New England Patriots       | 6-9      | 1479   |
| 17    | Chicago Bears              | 8-7      | 1472   |
| 18    | San Francisco 49ers        | 6-9      | 1442   |
| 19    | Denver Broncos             | 5-10     | 1435   |
| 20    | Los Angeles Chargers       | 6-9      | 1424   |
| 21    | Minnesota Vikings          | 6-9      | 1404   |
| 22    | Dallas Cowboys             | 6-9      | 1393   |
| 23    | Washington Football Team   | 6-9      | 1389   |
| 24    | New York Giants            | 5-10     | 1370   |
| 25    | Carolina Panthers          | 5-10     | 1367   |
| 26    | Philadelphia Eagles        | 4-10-1   | 1342   |
| 27    | Atlanta Falcons            | 4-11     | 1338   |
| 28    | Detroit Lions              | 5-10     | 1330   |
| 29    | Cincinnati Bengals         | 4-10-1   | 1320   |
| 30    | Houston Texans             | 4-11     | 1265   |
| 31    | New York Jets              | 2-13     | 1260   |
| 32    | Jacksonville Jaguars       | 1-14     | 963    |
_Updated 12/31/2020, 1:00pm_

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Gonzaga              | WCC        | 9-0      | 3212   |
| 2     | Tennessee            | SEC        | 7-0      | 3147   |
| 3     | Baylor               | Big 12     | 8-0      | 2928   |
| 4     | Michigan             | Big 10     | 7-0      | 2864   |
| 5     | SMU                  | AAC        | 6-0      | 2852   |
| 6     | Kansas               | Big 12     | 8-1      | 2818   |
| 7     | Arkansas             | SEC        | 9-0      | 2781   |
| 8     | Missouri             | SEC        | 6-1      | 2769   |
| 9     | Drake                | MVC        | 11-0     | 2620   |
| 10    | Minnesota            | Big 10     | 9-1      | 2551   |
| 11    | Winthrop             | Big South  | 6-0      | 2513   |
| 12    | West Virginia        | Big 12     | 8-2      | 2504   |
| 13    | Washington St.       | Pac 12     | 8-0      | 2500   |
| 14    | Rutgers              | Big 10     | 7-1      | 2473   |
| 15    | Illinois             | Big 10     | 7-3      | 2472   |
| 16    | The Citadel          | Southern   | 7-0      | 2466   |
| 17    | Clemson              | ACC        | 7-1      | 2465   |
| 18    | Virginia Tech        | ACC        | 8-1      | 2461   |
| 19    | Houston              | AAC        | 7-1      | 2460   |
| 20    | Villanova            | Big East   | 8-1      | 2447   |
| 21    | Iowa                 | Big 10     | 8-2      | 2413   |
| 22    | Saint Louis          | A-10       | 7-1      | 2409   |
| 23    | Texas                | Big 12     | 7-1      | 2383   |
| 24    | UCF                  | AAC        | 3-2      | 2373   |
| 25    | Boise St.            | MWC        | 6-1      | 2369   |
_Updated 12/31/2020, 1:00pm_

Script for scraping data by [Luke Benz](https://github.com/lbenz730/NCAA_Hoops).
