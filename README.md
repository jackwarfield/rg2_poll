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
| 6     | Notre Dame           | FBS Independents     | 10-1     | 2440   |
| 7     | San José State       | Mountain West        | 7-0      | 2367   |
| 8     | Indiana              | Big Ten              | 6-1      | 2308   |
| 9     | Coastal Carolina     | Sun Belt             | 11-1     | 2186   |
| 10    | Louisiana            | Sun Belt             | 10-1     | 2086   |
| 11    | BYU                  | FBS Independents     | 11-1     | 2071   |
| 12    | Liberty              | FBS Independents     | 10-1     | 2061   |
| 13    | Georgia              | SEC                  | 7-2      | 2006   |
| 14    | Miami                | ACC                  | 8-2      | 1987   |
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
| 1     | Kansas City Chiefs         | 13-1     | 2040   |
| 2     | Buffalo Bills              | 11-3     | 1825   |
| 3     | Pittsburgh Steelers        | 11-3     | 1733   |
| 4     | Tennessee Titans           | 10-4     | 1702   |
| 5     | New Orleans Saints         | 11-4     | 1700   |
| 6     | Indianapolis Colts         | 10-4     | 1686   |
| 7     | Baltimore Ravens           | 9-5      | 1683   |
| 8     | Cleveland Browns           | 10-4     | 1678   |
| 9     | Green Bay Packers          | 11-3     | 1678   |
| 10    | Tampa Bay Buccaneers       | 10-5     | 1653   |
| 11    | Miami Dolphins             | 10-5     | 1635   |
| 12    | Seattle Seahawks           | 10-4     | 1633   |
| 13    | Los Angeles Rams           | 9-5      | 1597   |
| 14    | Las Vegas Raiders          | 7-8      | 1505   |
| 15    | Arizona Cardinals          | 8-7      | 1493   |
| 16    | New England Patriots       | 6-8      | 1479   |
| 17    | Chicago Bears              | 7-7      | 1475   |
| 18    | Denver Broncos             | 5-9      | 1461   |
| 19    | San Francisco 49ers        | 6-9      | 1440   |
| 20    | Washington Football Team   | 6-8      | 1438   |
| 21    | Minnesota Vikings          | 6-9      | 1404   |
| 22    | New York Giants            | 5-9      | 1398   |
| 23    | Philadelphia Eagles        | 4-9-1    | 1387   |
| 24    | Dallas Cowboys             | 5-9      | 1376   |
| 25    | Los Angeles Chargers       | 5-9      | 1357   |
| 26    | Detroit Lions              | 5-10     | 1336   |
| 27    | Houston Texans             | 4-10     | 1332   |
| 28    | Atlanta Falcons            | 4-10     | 1321   |
| 29    | Carolina Panthers          | 4-10     | 1312   |
| 30    | Cincinnati Bengals         | 3-10-1   | 1298   |
| 31    | New York Jets              | 1-13     | 1109   |
| 32    | Jacksonville Jaguars       | 1-13     | 992    |
_Updated 12/27/2020, 12:00pm_

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Gonzaga              | WCC        | 7-0      | 3207   |
| 2     | Houston              | AAC        | 7-0      | 3164   |
| 3     | Michigan             | Big 10     | 7-0      | 3018   |
| 4     | Missouri             | SEC        | 6-0      | 3000   |
| 5     | Baylor               | Big 12     | 6-0      | 2940   |
| 6     | SMU                  | AAC        | 5-0      | 2928   |
| 7     | Kansas               | Big 12     | 8-1      | 2861   |
| 8     | Chattanooga          | Southern   | 9-0      | 2809   |
| 9     | Tennessee            | SEC        | 6-0      | 2808   |
| 10    | Boise St.            | MWC        | 6-1      | 2656   |
| 11    | UCF                  | AAC        | 3-2      | 2635   |
| 12    | Georgia              | SEC        | 7-0      | 2620   |
| 13    | Arkansas             | SEC        | 8-0      | 2619   |
| 14    | Southern Ill.        | MVC        | 6-0      | 2576   |
| 15    | Minnesota            | Big 10     | 8-1      | 2570   |
| 16    | Drake                | MVC        | 9-0      | 2532   |
| 17    | Washington St.       | Pac 12     | 8-0      | 2530   |
| 18    | St. Bonaventure      | A-10       | 2-0      | 2512   |
| 19    | West Virginia        | Big 12     | 7-2      | 2509   |
| 20    | Illinois             | Big 10     | 7-3      | 2504   |
| 21    | Texas Tech           | Big 12     | 7-2      | 2499   |
| 22    | Villanova            | Big East   | 8-1      | 2483   |
| 23    | The Citadel          | Southern   | 7-0      | 2475   |
| 24    | Virginia Tech        | ACC        | 7-1      | 2457   |
| 25    | Saint Louis          | A-10       | 7-1      | 2431   |
_Updated 12/26/2020, 9:30pm_

Script for scraping data by [Luke Benz](https://github.com/lbenz730/NCAA_Hoops).
