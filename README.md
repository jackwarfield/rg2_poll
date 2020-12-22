# Reinforced Glicko-2 Poll

This poll is based on the Glicko-2 rating system [\(Glickman 2013\)](http://glicko.net/glicko/glicko2.pdf) to produce resume-based sports rankings.

### College Football
| Rank	| Team					| Conference	| Record	| Rating	|
| ---:	| ---:					| ---:			| ---:		| ---:		|
| 1		| Alabama				| SEC			| 11-0		| 2971		|
| 2		| Ohio State			| Big Ten		| 6-0		| 2816		|
| 3		| Coastal Carolina		| Sun Belt		| 11-0		| 2769		|
| 4		| Cincinnati			| AAC			| 9-0		| 2571		|
| 5		| Clemson				| ACC			| 10-1		| 2454		|
| 6		| Texas A&amp;M			| SEC			| 8-1		| 2452		|
| 7		| Notre Dame			| ACC			| 10-1		| 2428		|
| 8		| San Jos&eacute; State | Mountain West | 7-0		| 2330		|
| 9		| Indiana				| Big Ten		| 6-1		| 2308		|
| 10	| Louisiana				| Sun Belt		| 9-1		| 2290		|
| 11	| BYU					| Independent	| 10-1		| 2239		|
| 12	| Georgia				| SEC			| 7-2		| 2006		|
| 13	| Florida				| SEC			| 8-3		| 1966		|
| 14	| Miami of Florida		| ACC			| 8-2		| 1952		|
| 15	| Oklahoma				| Big 12		| 8-2		| 1926		|
| 16	| Northwestern			| Big Ten		| 6-2		| 1919		|
| 17	| Iowa State			| Big 12		| 8-3		| 1900		|
| 18	| USC					| Pac-12		| 5-1		| 1881		|
|		| Tulsa					| AAC			| 6-2		| 1881		|
| 20	| Colorado				| Pac-12		| 4-1		| 1871		|
| 21	| Washington			| Pac-12		| 3-1		| 1858		|
| 22	| Utah					| Pac-12		| 3-2		| 1845		|
| 23	| North Carolina		| ACC			| 8-3		| 1842		|
| 24	| Stanford				| Pac-12		| 4-2		| 1834		|
| 25	| Iowa					| Big Ten		| 6-2		| 1820		|

Because of changes the schedules forced by the pandemic, resume-based rankings for college football are more difficult this year. Where for previous years, bias-free rankings using this method produce reasonable results, the lack of cross-conference play and full schedules complicate this year's rankings. The formula that I ended up using is:

1. All P5 teams start with a rating of 1500 and all G5 teams start with a rating of 1200. Other, non-FBS teams, if encountered in the schedule, are added to the table starting with a rating of 800. All teams start with a rating deviation of 600 and a volatility of 0.6.
2. The 2019 schedule is run through 1 time to give initial ratings. Note that, after this run, the RD remains high and so the ratings are still quite fluid.
3. The 2020 schedule is run through 50 times.

Thanks to [https://collegefootballdata.com](https://collegefootballdata.com) for the game data tables.

### NFL
| Rank  | Team                       | Record   | Rating |
| ---:  | ---:                       | ---:     | ---:   |
| 1     | Kansas City Chiefs         | 13-1     | 2044   |
| 2     | Pittsburgh Steelers        | 11-2     | 1851   |
| 3     | Buffalo Bills              | 11-3     | 1839   |
| 4     | Tennessee Titans           | 10-4     | 1720   |
| 5     | Baltimore Ravens           | 9-5      | 1706   |
| 6     | Indianapolis Colts         | 10-4     | 1696   |
| 7     | Cleveland Browns           | 10-4     | 1692   |
| 8     | New Orleans Saints         | 10-4     | 1683   |
| 9     | Green Bay Packers          | 11-3     | 1677   |
| 10    | Tampa Bay Buccaneers       | 9-5      | 1640   |
| 11    | Seattle Seahawks           | 10-4     | 1629   |
| 12    | Miami Dolphins             | 9-5      | 1595   |
| 13    | Los Angeles Rams           | 9-5      | 1587   |
| 14    | Las Vegas Raiders          | 7-7      | 1534   |
| 15    | Arizona Cardinals          | 8-6      | 1527   |
| 16    | Chicago Bears              | 7-7      | 1479   |
| 17    | New England Patriots       | 6-8      | 1474   |
| 18    | Denver Broncos             | 5-9      | 1464   |
| 19    | Washington Football Team   | 6-8      | 1431   |
| 20    | Minnesota Vikings          | 6-8      | 1420   |
| 21    | New York Giants            | 5-9      | 1388   |
| 22    | San Francisco 49ers        | 5-9      | 1387   |
| 23    | Philadelphia Eagles        | 4-9-1    | 1378   |
| 24    | Dallas Cowboys             | 5-9      | 1368   |
| 25    | Detroit Lions              | 5-9      | 1354   |
| 26    | Los Angeles Chargers       | 5-9      | 1348   |
| 27    | Houston Texans             | 4-10     | 1341   |
| 28    | Atlanta Falcons            | 4-10     | 1323   |
| 29    | Carolina Panthers          | 4-10     | 1317   |
| 30    | Cincinnati Bengals         | 2-10-1   | 1186   |
| 31    | New York Jets              | 1-13     | 1101   |
| 32    | Jacksonville Jaguars       | 1-13     | 978    |

NFL data comes from [https://www.pro-football-reference.com](https://www.pro-football-reference.com).
