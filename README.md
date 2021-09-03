# Reinforced Glicko-2 Poll

This poll is based on the Glicko-2 rating system [\(Glickman 2013\)](http://glicko.net/glicko/glicko2.pdf) to produce resume-based sports rankings.

### College Football
| Rank  | Team                 | Conference           | Record   | Rating |
| ---:  | ---:                 | ---:                 | ---:     | ---:   |
| 1     | Alabama              | SEC                  | 0-0      | 2469   |
| 2     | Ohio State           | Big Ten              | 1-0      | 2349   |
| 3     | Clemson              | ACC                  | 0-0      | 2140   |
| 4     | Texas A&M            | SEC                  | 0-0      | 2103   |
| 5     | Utah                 | Pac-12               | 1-0      | 2101   |
| 6     | Notre Dame           | FBS Independents     | 0-0      | 2075   |
| 7     | Georgia              | SEC                  | 0-0      | 2025   |
| 8     | Coastal Carolina     | Sun Belt             | 1-0      | 2021   |
| 9     | Cincinnati           | American Athletic    | 0-0      | 1998   |
| 10    | Ball State           | Mid-American         | 1-0      | 1984   |
| 11    | Oklahoma             | Big 12               | 0-0      | 1950   |
| 12    | BYU                  | FBS Independents     | 0-0      | 1934   |
| 13    | San José State       | Mountain West        | 1-0      | 1921   |
| 14    | Northwestern         | Big Ten              | 0-0      | 1915   |
| 15    | UCF                  | American Athletic    | 1-0      | 1894   |
| 16    | Liberty              | FBS Independents     | 0-0      | 1884   |
| 17    | North Carolina       | ACC                  | 0-0      | 1881   |
| 18    | Louisiana            | Sun Belt             | 0-0      | 1870   |
| 19    | UCLA                 | Pac-12               | 1-0      | 1862   |
| 20    | Iowa                 | Big Ten              | 0-0      | 1841   |
| 21    | Buffalo              | Mid-American         | 1-0      | 1835   |
| 22    | Stanford             | Pac-12               | 0-0      | 1799   |
| 23    | USC                  | Pac-12               | 0-0      | 1789   |
| 24    | Iowa State           | Big 12               | 0-0      | 1782   |
| 25    | Appalachian State    | Sun Belt             | 1-0      | 1781   |
_Updated 9/03/2021, 12:00pm_

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
| 26    | Dallas Cowboys             | 6-10     | 1366   |
| 26    | Atlanta Falcons            | 4-12     | 1350   |
| 27    | Philadelphia Eagles        | 4-11-1   | 1315   |
| 28    | Cincinnati Bengals         | 4-11-1   | 1314   |
| 29    | Detroit Lions              | 5-11     | 1311   |
| 30    | Houston Texans             | 4-12     | 1264   |
| 31    | New York Jets              | 2-14     | 1248   |
| 32    | Jacksonville Jaguars       | 1-15     | 958    |
_Updated 4/10/2021, 12:00pm_

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Gonzaga              | WCC        | 31-1     | 2617   |
| 2     | Baylor               | Big 12     | 28-2     | 2538   |
| 3     | Illinois             | Big 10     | 24-7     | 2218   |
| 4     | Michigan             | Big 10     | 23-5     | 2215   |
| 5     | Southern California  | Pac 12     | 25-8     | 2182   |
| 6     | Houston              | AAC        | 28-4     | 2171   |
| 7     | Oklahoma St.         | Big 12     | 21-9     | 2169   |
| 8     | Kansas               | Big 12     | 21-9     | 2140   |
| 9     | Oregon               | Pac 12     | 21-7     | 2133   |
| 10    | Alabama              | SEC        | 26-7     | 2131   |
| 11    | Arkansas             | SEC        | 25-7     | 2126   |
| 12    | Iowa                 | Big 10     | 22-9     | 2123   |
| 13    | UCLA                 | Pac 12     | 22-10    | 2123   |
| 14    | Texas                | Big 12     | 19-8     | 2114   |
| 15    | BYU                  | WCC        | 20-7     | 2101   |
| 16    | Colorado             | Pac 12     | 23-9     | 2098   |
| 17    | Ohio St.             | Big 10     | 21-10    | 2095   |
| 18    | San Diego St.        | MWC        | 23-5     | 2074   |
| 19    | West Virginia        | Big 12     | 19-10    | 2066   |
| 20    | Oregon St.           | Pac 12     | 20-13    | 2063   |
| 21    | Loyola Chicago       | MVC        | 26-5     | 2044   |
| 22    | Villanova            | Big East   | 18-7     | 2036   |
| 23    | Texas Tech           | Big 12     | 18-11    | 2036   |
| 24    | Creighton            | Big East   | 22-9     | 2035   |
| 25    | Florida St.          | ACC        | 18-7     | 2033   |
_Updated 4/10/2021, 12:00pm_

Script for scraping data by [Luke Benz](https://github.com/lbenz731/NCAA_Hoops).
One potential standing issue is that, because of the way the games are scraped, every game is actually considered twice when constructing the ranking. I don't think that this can actually be considered an objectively good or bad thing, but regardless it is probably something that I should fix eventually.
