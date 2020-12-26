# Reinforced Glicko-2 Poll

This poll is based on the Glicko-2 rating system [\(Glickman 2013\)](http://glicko.net/glicko/glicko2.pdf) to produce resume-based sports rankings.

### College Football
| Rank  | Team                 | Conference           | Record   | Rating |
| ---:  | ---:                 | ---:                 | ---:     | ---:   |
| 1     | Alabama              | SEC                  | 11-0     | 2971   |
| 2     | Ohio State           | Big Ten              | 6-0      | 2816   |
| 3     | Coastal Carolina     | Sun Belt             | 11-0     | 2785   |
| 4     | Cincinnati           | AAC			      | 9-0      | 2539   |
| 5     | Texas A&M            | SEC                  | 8-1      | 2452   |
| 6     | Clemson              | ACC                  | 10-1     | 2451   |
| 7     | Notre Dame           | ACC			      | 10-1     | 2425   |
| 8     | San José State       | Mountain West        | 7-0      | 2379   |
| 9     | Indiana              | Big Ten              | 6-1      | 2308   |
| 10    | Louisiana            | Sun Belt             | 9-1      | 2290   |
| 11    | BYU                  | FBS Independents     | 11-1     | 2280   |
| 12    | Georgia              | SEC                  | 7-2      | 2006   |
| 13    | Florida              | SEC                  | 8-3      | 1966   |
| 14    | Miami of Florida     | ACC                  | 8-2      | 1943   |
| 15    | Northwestern         | Big Ten              | 6-2      | 1919   |
| 16    | Oklahoma             | Big 12               | 8-2      | 1916   |
| 17    | Iowa State           | Big 12               | 8-3      | 1891   |
| 18    | USC                  | Pac-12               | 5-1      | 1887   |
| 19    | Colorado             | Pac-12               | 4-1      | 1878   |
| 20    | Boise State          | Mountain West        | 5-2      | 1864   |
| 21    | North Carolina       | ACC                  | 8-3      | 1835   |
| 22    | Tulsa                | AAC				  | 6-2      | 1834   |
| 23    | Washington           | Pac-12               | 3-1      | 1827   |
| 24    | Utah                 | Pac-12               | 3-2      | 1822   |
| 25    | Iowa                 | Big Ten              | 6-2      | 1820   |
_Updated 12/26/2020, 7:30am_

Because of changes the schedules forced by the pandemic, resume-based rankings for college football are more difficult this year. Where for previous years, bias-free rankings using this method produce reasonable results, the lack of cross-conference play and full schedules complicate this year's rankings. The formula that I ended up using is:

1. All P5 teams start with a rating of 1500 and all G5 teams start with a rating of 1200. Other, non-FBS teams, if encountered in the schedule, are added to the table starting with a rating of 800. All teams start with a rating deviation of 600 and a volatility of 0.6.
2. The 2019 schedule is run through 1 time to give initial ratings. Note that, after this run, the RD remains high and so the ratings are still quite fluid.
3. The 2020 schedule is run through 50 times.

Thanks to [https://collegefootballdata.com](https://collegefootballdata.com) for the game data tables.

### NFL
| Rank  | Team                       | Record   | Rating |
| ---:  | ---:                       | :---     | ---:   |
| 1     | Kansas City Chiefs         | 13-1     | 2040   |
| 2     | Buffalo Bills              | 11-3     | 1823   |
| 3     | Pittsburgh Steelers        | 11-3     | 1733   |
| 4     | Tennessee Titans           | 10-4     | 1703   |
| 5     | New Orleans Saints         | 11-4     | 1700   |
| 6     | Indianapolis Colts         | 10-4     | 1690   |
| 7     | Baltimore Ravens           | 9-5      | 1684   |
| 8     | Cleveland Browns           | 10-4     | 1681   |
| 9     | Green Bay Packers          | 11-3     | 1677   |
| 10    | Tampa Bay Buccaneers       | 9-5      | 1643   |
| 11    | Seattle Seahawks           | 10-4     | 1630   |
| 12    | Miami Dolphins             | 9-5      | 1599   |
| 13    | Los Angeles Rams           | 9-5      | 1588   |
| 14    | Las Vegas Raiders          | 7-7      | 1535   |
| 15    | Arizona Cardinals          | 8-6      | 1529   |
| 16    | Chicago Bears              | 7-7      | 1477   |
| 17    | New England Patriots       | 6-8      | 1474   |
| 18    | Denver Broncos             | 5-9      | 1461   |
| 19    | Washington Football Team   | 6-8      | 1436   |
| 20    | Minnesota Vikings          | 6-9      | 1406   |
| 21    | New York Giants            | 5-9      | 1394   |
| 22    | San Francisco 49ers        | 5-9      | 1391   |
| 23    | Philadelphia Eagles        | 4-9-1    | 1384   |
| 24    | Dallas Cowboys             | 5-9      | 1374   |
| 25    | Los Angeles Chargers       | 5-9      | 1359   |
| 26    | Detroit Lions              | 5-9      | 1353   |
| 27    | Houston Texans             | 4-10     | 1334   |
| 28    | Atlanta Falcons            | 4-10     | 1325   |
| 29    | Carolina Panthers          | 4-10     | 1318   |
| 30    | Cincinnati Bengals         | 3-10-1   | 1295   |
| 31    | New York Jets              | 1-13     | 1104   |
| 32    | Jacksonville Jaguars       | 1-13     | 993    |
_Updated 12/26/2020, 7:30am_

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Gonzaga              | WCC        | 6-0      | 3178   |
| 2     | Houston              | AAC        | 6-0      | 3075   |
| 3     | Michigan             | Big 10     | 7-0      | 2999   |
| 4     | Missouri             | SEC        | 6-0      | 2963   |
| 5     | SMU                  | AAC        | 5-0      | 2886   |
| 6     | Baylor               | Big 12     | 6-0      | 2870   |
| 7     | Kansas               | Big 12     | 8-1      | 2845   |
| 8     | Chattanooga          | Southern   | 9-0      | 2832   |
| 9     | Tennessee            | SEC        | 6-0      | 2796   |
| 10    | UCF                  | AAC        | 3-1      | 2640   |
| 11    | Boise St.            | MWC        | 6-1      | 2621   |
| 12    | Arkansas             | SEC        | 8-0      | 2609   |
| 13    | Georgia              | SEC        | 7-0      | 2605   |
| 14    | Southern Ill.        | MVC        | 6-0      | 2563   |
| 15    | Minnesota            | Big 10     | 8-1      | 2533   |
| 16    | Washington St.       | Pac 12     | 8-0      | 2516   |
| 17    | Drake                | MVC        | 9-0      | 2515   |
| 18    | St. Bonaventure      | A-10       | 2-0      | 2512   |
| 19    | West Virginia        | Big 12     | 7-2      | 2494   |
| 20    | Texas Tech           | Big 12     | 7-2      | 2485   |
| 21    | The Citadel          | Southern   | 7-0      | 2478   |
| 22    | Villanova            | Big East   | 8-1      | 2454   |
| 23    | Illinois             | Big 10     | 6-3      | 2446   |
| 24    | Virginia Tech        | ACC        | 7-1      | 2426   |
| 25    | Rutgers              | Big 10     | 6-1      | 2425   |
_Updated 12/26/2020, 7:30am_

Script for scraping data by [Luke Benz](https://github.com/lbenz730/NCAA_Hoops).
