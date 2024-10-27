"""
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.

 

Example 1:

Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
Example 2:

Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation: 
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.

"""
class Solution(object):
    def maximumPopulation(self, logs):
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))
            
        dates.sort()

        population = max_population = max_year = 0
        for year, change in dates:
            population += change
            if population > max_population:
                max_population = population
                max_year = year
        
        return max_year

    def maximumPopulation(self, logs):
        birth_years = []
        death_years = []
        for birth_y, death_y in logs:
            birth_years.append(birth_y)
            death_years.append(death_y)

        birth_years.sort()
        death_years.sort()

        p1 = p2 = 0
        max_pop = 0
        max_year = 0
        curr_pop = 0
        while p1 < len(birth_years):
            if birth_years[p1] < death_years[p2]:
                curr_pop += 1
                if curr_pop > max_pop:
                    max_pop = curr_pop
                    max_year = birth_years[p1]
                p1 += 1
            else:
                curr_pop -= 1
                p2 += 1
        
        return max_year

