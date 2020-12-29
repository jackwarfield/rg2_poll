# Reinforced Glicko-2 Poll

This poll is based on the Glicko-2 rating system [\(Glickman 2013\)](http://glicko.net/glicko/glicko2.pdf) to produce resume-based sports rankings.

### College Football
| Rank  | Team                 | Conference           | Record   | Rating |
| ---:  | ---:                 | ---:                 | ---:     | ---:   |
| 1     | Alabama              | SEC                  | 11-0     | 2971   |
| 2     | Ohio State           | Big Ten              | 6-0      | 2816   |
| 3     | Cincinnati           | American Athletic    | 9-0      | 2537   |
| 4     | Clemson              | ACC                  | 10-1     | 2467   |
| 5     | Texas A&M            | SEC                  | 8-1      | 2452   |
| 6     | Notre Dame           | ACC			      | 10-1     | 2440   |
| 7     | San José State       | Mountain West        | 7-0      | 2367   |
| 8     | Indiana              | Big Ten              | 6-1      | 2308   |
| 9     | Coastal Carolina     | Sun Belt             | 11-1     | 2186   |
| 10    | Louisiana            | Sun Belt             | 10-1     | 2086   |
| 11    | BYU                  | FBS Independents     | 11-1     | 2071   |
| 12    | Liberty              | FBS Independents     | 10-1     | 2061   |
| 13    | Georgia              | SEC                  | 7-2      | 2006   |
| 14    | Miami of Florida     | ACC                  | 8-2      | 1987   |
| 15    | Florida              | SEC                  | 8-3      | 1966   |
| 16    | Northwestern         | Big Ten              | 6-2      | 1919   |
| 17    | Oklahoma             | Big 12               | 8-2      | 1902   |
| 18    | USC                  | Pac-12               | 5-1      | 1887   |
| 19    | North Carolina       | ACC                  | 8-3      | 1882   |
| 20    | Colorado             | Pac-12               | 4-1      | 1876   |
| 21    | Iowa State           | Big 12               | 8-3      | 1868   |
| 22    | NC State             | ACC                  | 8-3      | 1860   |
| 23    | Tulsa                | American Athletic    | 6-2      | 1829   |
| 24    | Washington           | Pac-12               | 3-1      | 1827   |
| 25    | Utah                 | Pac-12               | 3-2      | 1822   |
_Updated 12/27/2020, 12:00pm_

Because of changes the schedules forced by the pandemic, resume-based rankings for college football are more difficult this year. Where for previous years, bias-free rankings using this method produce reasonable results, the lack of cross-conference play and full schedules complicate this year's rankings. The formula that I ended up using is:

1. All P5 teams start with a rating of 1500 and all G5 teams start with a rating of 1200. Other, non-FBS teams, if encountered in the schedule, are added to the table starting with a rating of 800. All teams start with a rating deviation of 600 and a volatility of 0.6.
2. The 2019 schedule is run through 1 time to give initial ratings. Note that, after this run, the RD remains high and so the ratings are still quite fluid.
3. The 2020 schedule is run through 50 times.

Thanks to [https://collegefootballdata.com](https://collegefootballdata.com) for the game data tables.

### NFL
| Rank  | Team                       | Record   | Rating |
| ---:  | ---:                       | :---     | ---:   |
| 1     | Kansas City Chiefs         | 14-1     | 2050   |
| 2     | Buffalo Bills              | 11-3     | 1829   |
| 3     | Pittsburgh Steelers        | 12-3     | 1742   |
| 4     | Green Bay Packers          | 12-3     | 1716   |
| 5     | New Orleans Saints         | 11-4     | 1712   |
| 6     | Seattle Seahawks           | 11-4     | 1665   |
| 7     | Baltimore Ravens           | 10-5     | 1665   |
| 8     | Tampa Bay Buccaneers       | 10-5     | 1663   |
| 9     | Miami Dolphins             | 10-5     | 1649   |
| 10    | Tennessee Titans           | 10-5     | 1638   |
| 11    | Indianapolis Colts         | 10-5     | 1634   |
| 12    | Cleveland Browns           | 10-5     | 1583   |
| 13    | Los Angeles Rams           | 9-6      | 1572   |
| 14    | Las Vegas Raiders          | 7-8      | 1516   |
| 15    | Arizona Cardinals          | 8-7      | 1498   |
| 16    | New England Patriots       | 6-8      | 1488   |
| 17    | Chicago Bears              | 8-7      | 1472   |
| 18    | San Francisco 49ers        | 6-9      | 1443   |
| 19    | Denver Broncos             | 5-10     | 1435   |
| 20    | Los Angeles Chargers       | 6-9      | 1425   |
| 21    | Minnesota Vikings          | 6-9      | 1404   |
| 22    | Dallas Cowboys             | 6-9      | 1394   |
| 23    | Washington Football Team   | 6-9      | 1389   |
| 24    | New York Giants            | 5-10     | 1370   |
| 25    | Carolina Panthers          | 5-10     | 1368   |
| 26    | Philadelphia Eagles        | 4-10-1   | 1342   |
| 27    | Atlanta Falcons            | 4-11     | 1339   |
| 28    | Detroit Lions              | 5-10     | 1330   |
| 29    | Cincinnati Bengals         | 4-10-1   | 1320   |
| 30    | Houston Texans             | 4-11     | 1266   |
| 31    | New York Jets              | 2-13     | 1260   |
| 32    | Jacksonville Jaguars       | 1-14     | 963    |
_Updated 12/28/2020, 1:30pm_

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Gonzaga              | WCC        | 8-0      | 3185   |
| 2     | Houston              | AAC        | 7-0      | 3104   |
| 3     | Michigan             | Big 10     | 7-0      | 3007   |
| 4     | Missouri             | SEC        | 6-0      | 2986   |
| 5     | SMU                  | AAC        | 5-0      | 2968   |
| 6     | Baylor               | Big 12     | 6-0      | 2942   |
| 7     | Chattanooga          | Southern   | 9-0      | 2855   |
| 8     | Kansas               | Big 12     | 8-1      | 2831   |
| 9     | Arkansas             | SEC        | 8-0      | 2612   |
| 10    | UCF                  | AAC        | 3-2      | 2609   |
| 11    | Georgia              | SEC        | 7-0      | 2608   |
| 12    | Boise St.            | MWC        | 6-1      | 2604   |
| 13    | Drake                | MVC        | 11-0     | 2597   |
| 14    | Winthrop             | Big South  | 5-0      | 2565   |
| 15    | Tennessee            | SEC        | 6-0      | 2561   |
| 16    | St. Bonaventure      | A-10       | 2-0      | 2531   |
| 17    | Minnesota            | Big 10     | 9-1      | 2531   |
| 18    | Washington St.       | Pac 12     | 8-0      | 2519   |
| 19    | West Virginia        | Big 12     | 7-2      | 2489   |
| 20    | Illinois             | Big 10     | 7-3      | 2489   |
| 21    | Texas Tech           | Big 12     | 7-2      | 2468   |
| 22    | The Citadel          | Southern   | 7-0      | 2467   |
| 23    | Dayton               | A-10       | 4-1      | 2455   |
| 24    | East Carolina        | AAC        | 7-1      | 2441   |
| 25    | Alabama A&M          | SWAC       | 2-0      | 2435   |
_Updated 12/29/2020, 1:18am_

Script for scraping data by [Luke Benz](https://github.com/lbenz730/NCAA_Hoops).
