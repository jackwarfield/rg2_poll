# Reinforced Glicko-2 Poll

This poll is based on the Glicko-2 rating system [\(Glickman 2013\)](http://glicko.net/glicko/glicko2.pdf) to produce resume-based sports rankings.

### College Football
| Rank  | Team                 | Conference           | Record   | Rating |
| ---:  | ---:                 | ---:                 | ---:     | ---:   |
| 1     | Alabama              | SEC                  | 12-0     | 3099   |
| 2     | Ohio State           | Big Ten              | 7-0      | 2878   |
| 3     | Texas A&M            | SEC                  | 9-1      | 2572   |
| 4     | Clemson              | ACC                  | 10-2     | 2321   |
| 5     | Notre Dame           | ACC			      | 10-2     | 2302   |
| 6     | Georgia              | SEC                  | 8-2      | 2230   |
| 7     | Coastal Carolina     | Sun Belt             | 11-1     | 2167   |
| 8     | Oklahoma             | Big 12               | 9-2      | 2138   |
| 9     | Louisiana            | Sun Belt             | 10-1     | 2134   |
| 10    | Florida              | SEC                  | 8-4      | 2067   |
| 11    | Cincinnati           | American Athletic    | 9-1      | 2061   |
| 12    | Iowa State           | Big 12               | 9-3      | 2051   |
| 13    | Ball State           | Mid-American         | 7-1      | 2032   |
| 14    | Northwestern         | Big Ten              | 7-2      | 2025   |
| 15    | BYU                  | FBS Independents     | 11-1     | 2021   |
| 16    | Liberty              | FBS Independents     | 10-1     | 1989   |
| 17    | Oklahoma State       | Big 12               | 8-3      | 1943   |
| 18    | San José State       | Mountain West        | 7-1      | 1941   |
| 19    | Auburn               | SEC                  | 6-5      | 1932   |
| 20    | Texas                | Big 12               | 7-3      | 1930   |
| 21    | Indiana              | Big Ten              | 6-2      | 1930   |
| 22    | Buffalo              | Mid-American         | 6-1      | 1916   |
| 23    | LSU                  | SEC                  | 5-5      | 1870   |
| 24    | Miami		           | Mid-American         | 2-1      | 1867   |
| 25    | Iowa                 | Big Ten              | 6-2      | 1834   |
_Updated 1/07/2021, 1:30pm_

Because of changes the schedules forced by the pandemic, resume-based rankings for college football are more difficult this year. Where for previous years, bias-free rankings using this method produce reasonable results, the lack of cross-conference play and full schedules complicate this year's rankings. The formula that I ended up using is:

1. All P5 teams start with a rating of 1500 and all G5 teams start with a rating of 1200. Other, non-FBS teams, if encountered in the schedule, are added to the table starting with a rating of 800. All teams start with a rating deviation of 600 and a volatility of 0.6.
2. The 2019 schedule is run through 1 time to give initial ratings. Note that, after this run, the RD remains high and so the ratings are still quite fluid.
3. The 2020 schedule is run through 50 times.

Thanks to [https://collegefootballdata.com](https://collegefootballdata.com) for the game data tables.

### NFL
| Rank  | Team                       | Record   | Rating |
| ---:  | ---:                       | :---     | ---:   |
| 1     | Kansas City Chiefs         | 14-2     | 1907   |
| 2     | Buffalo Bills              | 13-3     | 1854   |
| 3     | Green Bay Packers          | 13-3     | 1740   |
| 4     | New Orleans Saints         | 12-4     | 1724   |
| 5     | Pittsburgh Steelers        | 12-4     | 1694   |
| 6     | Seattle Seahawks           | 12-4     | 1685   |
| 7     | Tampa Bay Buccaneers       | 11-5     | 1681   |
| 8     | Baltimore Ravens           | 11-5     | 1673   |
| 9     | Tennessee Titans           | 11-5     | 1653   |
| 10    | Indianapolis Colts         | 11-5     | 1643   |
| 11    | Cleveland Browns           | 11-5     | 1635   |
| 12    | Miami Dolphins             | 10-6     | 1634   |
| 13    | Los Angeles Rams           | 10-6     | 1599   |
| 14    | Las Vegas Raiders          | 8-8      | 1550   |
| 15    | New England Patriots       | 7-9      | 1496   |
| 16    | Los Angeles Chargers       | 7-9      | 1495   |
| 17    | Arizona Cardinals          | 8-8      | 1476   |
| 18    | Chicago Bears              | 8-8      | 1468   |
| 19    | San Francisco 49ers        | 6-10     | 1432   |
| 20    | Minnesota Vikings          | 7-9      | 1432   |
| 21    | Denver Broncos             | 5-11     | 1417   |
| 22    | Washington Football Team   | 7-9      | 1415   |
| 23    | New York Giants            | 6-10     | 1404   |
| 24    | Dallas Cowboys             | 6-10     | 1367   |
| 25    | Carolina Panthers          | 5-11     | 1366   |
| 26    | Atlanta Falcons            | 4-12     | 1334   |
| 27    | Cincinnati Bengals         | 4-11-1   | 1318   |
| 28    | Philadelphia Eagles        | 4-11-1   | 1317   |
| 29    | Detroit Lions              | 5-11     | 1307   |
| 30    | Houston Texans             | 4-12     | 1259   |
| 31    | New York Jets              | 2-14     | 1244   |
| 32    | Jacksonville Jaguars       | 1-15     | 961    |
_Updated 1/07/2021, 1:30pm_

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Gonzaga              | WCC        | 10-0     | 3122   |
| 2     | Michigan             | Big 10     | 10-0     | 3012   |
| 3     | Baylor               | Big 12     | 10-0     | 2933   |
| 4     | Drake                | MVC        | 13-0     | 2666   |
| 5     | Texas                | Big 12     | 9-1      | 2605   |
| 6     | Kansas               | Big 12     | 9-2      | 2576   |
| 7     | Winthrop             | Big South  | 9-0      | 2576   |
| 8     | Villanova            | Big East   | 8-1      | 2507   |
| 9     | Clemson              | ACC        | 9-1      | 2478   |
| 10    | Houston              | AAC        | 9-1      | 2478   |
| 11    | Louisville           | ACC        | 8-1      | 2467   |
| 12    | The Citadel          | Southern   | 7-0      | 2463   |
| 13    | Iowa                 | Big 10     | 9-2      | 2440   |
| 14    | Minnesota            | Big 10     | 10-3     | 2414   |
| 15    | Siena                | MAAC       | 2-0      | 2391   |
| 16    | Tennessee            | SEC        | 8-1      | 2385   |
| 17    | Virginia Tech        | ACC        | 8-2      | 2379   |
| 18    | Creighton            | Big East   | 9-2      | 2365   |
| 19    | Illinois             | Big 10     | 8-3      | 2357   |
| 20    | Missouri             | SEC        | 7-2      | 2340   |
| 21    | Alabama A&M          | SWAC       | 2-0      | 2338   |
| 22    | Hawaii               | Big West   | 2-0      | 2338   |
| 23    | UC San Diego         | Big West   | 2-0      | 2338   |
| 24    | Boise St.            | MWC        | 9-1      | 2337   |
| 25    | Wisconsin            | Big 10     | 9-2      | 2333   |
_Updated 1/07/2021, 1:30pm_

Script for scraping data by [Luke Benz](https://github.com/lbenz730/NCAA_Hoops).
