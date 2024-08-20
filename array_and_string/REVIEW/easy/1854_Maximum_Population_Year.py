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
    def maximumPopulation2(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        mapping = collections.defaultdict(int)
        max_years = []
        max_pop = 0
        for log in logs:
            for year in range(log[0], log[1]):
                mapping[year] += 1
                if mapping[year] > max_pop:
                    max_pop = mapping[year]
                    max_years = [year]
                elif mapping[year] == max_pop:
                    max_years.append(year)


        return min(max_years)

    def maximumPopulation3(self, logs):
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
