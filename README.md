# Reinforced Glicko-2 Poll

This poll is based on the Glicko-2 rating system [\(Glickman 2013\)](http://glicko.net/glicko/glicko2.pdf) to produce resume-based sports rankings.

### College Football
| Rank  | Team                 | Conference           | Record   | Rating |
| ---:  | ---:                 | ---:                 | ---:     | ---:   |
| 1     | Alabama              | SEC                  | 11-0     | 2971   |
| 2     | Ohio State           | Big Ten              | 6-0      | 2816   |
| 3     | Coastal Carolina     | Sun Belt             | 11-0     | 2788   |
| 4     | Cincinnati           | American Athletic    | 9-0      | 2540   |
| 5     | Clemson              | ACC                  | 10-1     | 2452   |
| 6     | Texas A&M            | SEC                  | 8-1      | 2452   |
| 7     | Notre Dame           | FBS Independents     | 10-1     | 2426   |
| 8     | San José State       | Mountain West        | 7-0      | 2380   |
| 9     | Indiana              | Big Ten              | 6-1      | 2308   |
| 10    | Louisiana            | Sun Belt             | 9-1      | 2295   |
| 11    | BYU                  | FBS Independents     | 11-1     | 2282   |
| 12    | Georgia              | SEC                  | 7-2      | 2006   |
| 13    | Florida              | SEC                  | 8-3      | 1966   |
| 14    | Miami                | ACC                  | 8-2      | 1946   |
| 15    | Northwestern         | Big Ten              | 6-2      | 1919   |
| 16    | Oklahoma             | Big 12               | 8-2      | 1918   |
| 17    | Iowa State           | Big 12               | 8-3      | 1892   |
| 18    | USC                  | Pac-12               | 5-1      | 1887   |
| 19    | Colorado             | Pac-12               | 4-1      | 1878   |
| 20    | Boise State          | Mountain West        | 5-2      | 1865   |
| 21    | North Carolina       | ACC                  | 8-3      | 1837   |
| 22    | Tulsa                | American Athletic    | 6-2      | 1836   |
| 23    | Washington           | Pac-12               | 3-1      | 1827   |
| 24    | Utah                 | Pac-12               | 3-2      | 1822   |
| 25    | Iowa                 | Big Ten              | 6-2      | 1820   |

Because of changes the schedules forced by the pandemic, resume-based rankings for college football are more difficult this year. Where for previous years, bias-free rankings using this method produce reasonable results, the lack of cross-conference play and full schedules complicate this year's rankings. The formula that I ended up using is:

1. All P5 teams start with a rating of 1500 and all G5 teams start with a rating of 1200. Other, non-FBS teams, if encountered in the schedule, are added to the table starting with a rating of 800. All teams start with a rating deviation of 600 and a volatility of 0.6.
2. The 2019 schedule is run through 1 time to give initial ratings. Note that, after this run, the RD remains high and so the ratings are still quite fluid.
3. The 2020 schedule is run through 50 times.

Thanks to [https://collegefootballdata.com](https://collegefootballdata.com) for the game data tables.

### NFL
| Rank  | Team                       | Record   | Rating |
| ---:  | ---:                       | :---     | ---:   |
| 1     | Kansas City Chiefs         | 13-1     | 2037   |
| 2     | Buffalo Bills              | 11-3     | 1822   |
| 3     | Pittsburgh Steelers        | 11-3     | 1733   |
| 4     | Tennessee Titans           | 10-4     | 1705   |
| 5     | Indianapolis Colts         | 10-4     | 1691   |
| 6     | Baltimore Ravens           | 9-5      | 1684   |
| 7     | New Orleans Saints         | 10-4     | 1683   |
| 8     | Cleveland Browns           | 10-4     | 1681   |
| 9     | Green Bay Packers          | 11-3     | 1677   |
| 10    | Tampa Bay Buccaneers       | 9-5      | 1640   |
| 11    | Seattle Seahawks           | 10-4     | 1630   |
| 12    | Miami Dolphins             | 9-5      | 1599   |
| 13    | Los Angeles Rams           | 9-5      | 1588   |
| 14    | Las Vegas Raiders          | 7-7      | 1533   |
| 15    | Arizona Cardinals          | 8-6      | 1529   |
| 16    | Chicago Bears              | 7-7      | 1478   |
| 17    | New England Patriots       | 6-8      | 1473   |
| 18    | Denver Broncos             | 5-9      | 1459   |
| 19    | Washington Football Team   | 6-8      | 1436   |
| 20    | Minnesota Vikings          | 6-8      | 1419   |
| 21    | New York Giants            | 5-9      | 1394   |
| 22    | San Francisco 49ers        | 5-9      | 1390   |
| 23    | Philadelphia Eagles        | 4-9-1    | 1383   |
| 24    | Dallas Cowboys             | 5-9      | 1375   |
| 25    | Los Angeles Chargers       | 5-9      | 1357   |
| 26    | Detroit Lions              | 5-9      | 1354   |
| 27    | Houston Texans             | 4-10     | 1336   |
| 28    | Atlanta Falcons            | 4-10     | 1325   |
| 29    | Carolina Panthers          | 4-10     | 1318   |
| 30    | Cincinnati Bengals         | 3-10-1   | 1295   |
| 31    | New York Jets              | 1-13     | 1103   |
| 32    | Jacksonville Jaguars       | 1-13     | 995    |

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).

### Men's College Basketball
| Rank  | Team                 | Conference | Record   | Rating |
| ---:  | ---:                 | ---:       | ---:     | ---:   |
| 1     | Gonzaga              | WCC        | 6-0      | 3230   |
| 2     | Houston              | AAC        | 6-0      | 3072   |
| 3     | Michigan             | Big 10     | 6-0      | 3069   |
| 4     | Missouri             | SEC        | 6-0      | 2933   |
| 5     | SMU                  | AAC        | 5-0      | 2905   |
| 6     | Kansas               | Big 12     | 8-1      | 2873   |
| 7     | Baylor               | Big 12     | 6-0      | 2872   |
| 8     | Chattanooga          | Southern   | 9-0      | 2780   |
| 9     | Tennessee            | SEC        | 6-0      | 2765   |
| 10    | UCF                  | AAC        | 3-1      | 2710   |
| 11    | Boise St.            | MWC        | 6-1      | 2626   |
| 12    | Arkansas             | SEC        | 8-0      | 2626   |
| 13    | Iowa                 | Big 10     | 7-1      | 2598   |
| 14    | St. Bonaventure      | A-10       | 2-0      | 2597   |
| 15    | Southern Ill.        | MVC        | 6-0      | 2579   |
| 16    | Washington St.       | Pac 12     | 8-0      | 2559   |
| 17    | Georgia              | SEC        | 7-0      | 2558   |
| 18    | Winthrop             | Big South  | 5-0      | 2526   |
| 19    | Drake                | MVC        | 9-0      | 2517   |
| 20    | West Virginia        | Big 12     | 7-2      | 2510   |
| 21    | Villanova            | Big East   | 8-1      | 2499   |
| 22    | Texas Tech           | Big 12     | 7-2      | 2495   |
| 23    | Virginia Tech        | ACC        | 7-1      | 2481   |
| 24    | Florida St.          | ACC        | 5-1      | 2473   |
| 25    | Rutgers              | Big 10     | 6-1      | 2464   |

Script for scraping data by [Luke Benz](https://github.com/lbenz730/NCAA_Hoops).
