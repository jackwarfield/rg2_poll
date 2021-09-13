# Reinforced Glicko-2 Poll

This poll is based on the Glicko-2 rating system [\(Glickman 2013\)](http://glicko.net/glicko/glicko2.pdf) to produce resume-based sports rankings.

### College Football
| Rank  | Team                 | Conference           | Record   | Rating |
| ---:  | ---:                 | ---:                 | ---:     | ---:   |
| 1     | Alabama              | SEC                  | 2-0      | 2670   |
| 2     | Georgia              | SEC                  | 2-0      | 2491   |
| 3     | Oregon               | Pac-12               | 2-0      | 2471   |
| 4     | Texas A&M            | SEC                  | 2-0      | 2362   |
| 5     | Iowa                 | Big Ten              | 2-0      | 2338   |
| 6     | BYU                  | FBS Independents     | 2-0      | 2298   |
| 7     | Notre Dame           | FBS Independents     | 2-0      | 2217   |
| 8     | Michigan State       | Big Ten              | 2-0      | 2211   |
| 9     | Penn State           | Big Ten              | 2-0      | 2199   |
| 10    | Kansas State         | Big 12               | 2-0      | 2190   |
| 11    | Oklahoma             | Big 12               | 2-0      | 2161   |
| 12    | Virginia Tech        | ACC                  | 2-0      | 2135   |
| 13    | Arkansas             | SEC                  | 2-0      | 2131   |
| 14    | Cincinnati           | American Athletic    | 2-0      | 2128   |
| 15    | Coastal Carolina     | Sun Belt             | 2-0      | 2076   |
| 16    | Florida              | SEC                  | 2-0      | 2063   |
| 17    | UCLA                 | Pac-12               | 2-0      | 2052   |
| 18    | Liberty              | FBS Independents     | 2-0      | 2043   |
| 19    | Mississippi State    | SEC                  | 2-0      | 2035   |
| 20    | Kentucky             | SEC                  | 2-0      | 2010   |
| 21    | UCF                  | American Athletic    | 2-0      | 1988   |
| 22    | Miami                | ACC                  | 1-1      | 1972   |
| 23    | Virginia             | ACC                  | 2-0      | 1959   |
| 24    | Oklahoma State       | Big 12               | 2-0      | 1933   |
| 25    | Maryland             | Big Ten              | 2-0      | 1929   |
_Updated 9/13/2021, 8:00pm_

Because of changes the schedules forced by the pandemic, resume-based rankings for college football are more difficult this year. Where for previous years, bias-free rankings using this method produce reasonable results, the lack of cross-conference play and full schedules complicate this year's rankings. The formula that I ended up using is:

1. All P5 teams start with a rating of 1500 and all G5 teams start with a rating of 1200. Other, non-FBS teams, if encountered in the schedule, are added to the table starting with a rating of 800. All teams start with a rating deviation of 600 and a volatility of 0.6.
2. The 2020 schedule is run through 1 time to give initial ratings. Note that, after this run, the RD remains high and so the ratings are still quite fluid.
3. The 2021 schedule is run through 50 times.

Thanks to [https://collegefootballdata.com](https://collegefootballdata.com) for the game data tables.

### NFL
| Rank  | Team                       | Record   | Rating |
| ---:  | ---:                       | :---     | ---:   |
| 1     | Kansas City Chiefs         | 1-0      | 2247   |
| 2     | Pittsburgh Steelers        | 1-0      | 2159   |
| 3     | New Orleans Saints         | 1-0      | 2075   |
| 4     | Tampa Bay Buccaneers       | 1-0      | 1988   |
| 5     | Seattle Seahawks           | 1-0      | 1983   |
| 6     | Miami Dolphins             | 1-0      | 1938   |
| 7     | Los Angeles Chargers       | 1-0      | 1855   |
| 8     | Arizona Cardinals          | 1-0      | 1848   |
| 9     | Los Angeles Rams           | 1-0      | 1821   |
| 10    | Baltimore Ravens           | 0-0      | 1782   |
| 11    | Denver Broncos             | 1-0      | 1725   |
| 12    | Cincinnati Bengals         | 1-0      | 1631   |
| 13    | San Francisco 49ers        | 1-0      | 1619   |
| 14    | Buffalo Bills              | 0-1      | 1584   |
| 15    | Philadelphia Eagles        | 1-0      | 1577   |
| 16    | Cleveland Browns           | 0-1      | 1568   |
| 17    | Las Vegas Raiders          | 0-0      | 1531   |
| 18    | Carolina Panthers          | 1-0      | 1529   |
| 19    | Green Bay Packers          | 0-1      | 1461   |
| 20    | Indianapolis Colts         | 0-1      | 1400   |
| 21    | Houston Texans             | 1-0      | 1316   |
| 22    | Tennessee Titans           | 0-1      | 1280   |
| 23    | New England Patriots       | 0-1      | 1257   |
| 24    | Dallas Cowboys             | 0-1      | 1198   |
| 25    | Chicago Bears              | 0-1      | 1178   |
| 26    | Washington Football Team   | 0-1      | 1177   |
| 27    | New York Giants            | 0-1      | 1123   |
| 28    | Minnesota Vikings          | 0-1      | 1029   |
| 29    | Detroit Lions              | 0-1      | 979    |
| 30    | Atlanta Falcons            | 0-1      | 974    |
| 31    | New York Jets              | 0-1      | 844    |
| 32    | Jacksonville Jaguars       | 0-1      | 524    |
_Updated 9/13/2021, 8:00pm_

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
