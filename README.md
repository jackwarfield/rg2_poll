# Reinforced Glicko-2 Poll

This poll is based on the Glicko-2 rating system [\(Glickman 2013\)](http://glicko.net/glicko/glicko2.pdf) to produce resume-based sports rankings.

### College Football
| Rank  | Team                 | Conference           | Record   | Rating |
| ---:  | ---:                 | ---:                 | ---:     | ---:   |
| 1     | Alabama              | SEC                  | 12-0     | 3089   |
| 2     | Ohio State           | Big Ten              | 7-0      | 2879   |
| 3     | Texas A&M            | SEC                  | 8-1      | 2550   |
| 4     | Clemson              | ACC                  | 10-2     | 2322   |
| 5     | Notre Dame           | ACC				  | 10-2     | 2303   |
| 6     | Georgia              | SEC                  | 8-2      | 2226   |
| 7     | Coastal Carolina     | Sun Belt             | 11-1     | 2161   |
| 8     | Oklahoma             | Big 12               | 9-2      | 2121   |
| 9     | Louisiana            | Sun Belt             | 10-1     | 2120   |
| 10    | Florida              | SEC                  | 8-4      | 2059   |
| 11    | Cincinnati           | American Athletic    | 9-1      | 2058   |
| 12    | Ball State           | Mid-American         | 7-1      | 2032   |
| 13    | Northwestern         | Big Ten              | 7-2      | 2024   |
| 14    | Iowa State           | Big 12               | 8-3      | 2022   |
| 15    | BYU                  | FBS Independents     | 11-1     | 2018   |
| 16    | Liberty              | FBS Independents     | 10-1     | 1987   |
| 17    | San José State       | Mountain West        | 7-1      | 1941   |
| 18    | Oklahoma State       | Big 12               | 8-3      | 1930   |
| 19    | Indiana              | Big Ten              | 6-2      | 1929   |
| 20    | Auburn               | SEC                  | 6-5      | 1929   |
| 21    | Texas                | Big 12               | 7-3      | 1918   |
| 22    | Buffalo              | Mid-American         | 6-1      | 1915   |
| 23    | Miami		           | Mid-American         | 2-1      | 1867   |
| 24    | LSU                  | SEC                  | 5-5      | 1866   |
| 25    | USC                  | Pac-12               | 5-1      | 1856   |
_Updated 1/02/2021, 5:45pm_

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
_Updated 1/02/2021, 5:45pm_

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Tennessee            | SEC        | 7-0      | 3214   |
| 2     | Gonzaga              | WCC        | 9-0      | 3145   |
| 3     | Baylor               | Big 12     | 9-0      | 2939   |
| 4     | Michigan             | Big 10     | 8-0      | 2911   |
| 5     | Missouri             | SEC        | 7-1      | 2853   |
| 6     | SMU                  | AAC        | 6-0      | 2648   |
| 7     | Texas                | Big 12     | 8-1      | 2621   |
| 8     | Drake                | MVC        | 11-0     | 2596   |
| 9     | Kansas               | Big 12     | 8-2      | 2581   |
| 10    | Villanova            | Big East   | 8-1      | 2578   |
| 11    | Winthrop             | Big South  | 7-0      | 2555   |
| 12    | Virginia Tech        | ACC        | 8-1      | 2533   |
| 13    | Clemson              | ACC        | 8-1      | 2505   |
| 14    | Colgate              | Patriot    | 1-0      | 2496   |
| 15    | Washington St.       | Pac 12     | 8-0      | 2492   |
| 16    | Iowa                 | Big 10     | 9-2      | 2470   |
| 17    | The Citadel          | Southern   | 7-0      | 2467   |
| 18    | Arkansas             | SEC        | 9-1      | 2446   |
| 19    | West Virginia        | Big 12     | 8-2      | 2443   |
| 20    | Houston              | AAC        | 7-1      | 2428   |
| 21    | Oregon               | Pac 12     | 7-1      | 2421   |
| 22    | Illinois             | Big 10     | 7-3      | 2412   |
| 23    | Minnesota            | Big 10     | 9-2      | 2381   |
| 24    | Rutgers              | Big 10     | 7-2      | 2364   |
| 25    | UCF                  | AAC        | 3-2      | 2350   |
_Updated 1/02/2021, 5:45pm_

Script for scraping data by [Luke Benz](https://github.com/lbenz730/NCAA_Hoops).
