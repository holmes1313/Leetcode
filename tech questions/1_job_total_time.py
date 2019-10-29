# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:28:25 2019

@author: z.chen7
"""

# Write function to find a job's total time, including any child jobs.
"""
job_id, job_time, child_job_ids
jobs = [[1, 10, [2, 3]],
  [2, 20, [4]],
  [4, 40, []],
  [3, 30, []]
]

Examples
find_job_total_time(job_id=4, jobs=jobs)  # 40
find_job_total_time(job_id=1, jobs=jobs)  # 10 + (20 + 40) + 30 = 100
"""


class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def find_job_total_time(self, job_id, jobs):      
        jobs = {job[0]: (job[1], job[2]) for job in jobs}
        if job_id not in jobs:
            return None
        return self.helper(job_id, jobs)
        
    def helper(self, job_id, jobs):
        if self.memo[job_id]:
            return self.memo[job_id]
        job = jobs[job_id]        
        job_time, child_ids = job[0], job[1]
        for child_id in child_ids:
            job_time += self.helper(child_id, jobs)
        self.memo[job_id] = job_time
        return job_time
  



def find_job_total_time(job_id, jobs):
    jobs = {job[0]: (job[1], job[2]) for job in jobs}
    return helper(job_id, jobs)
    
def helper(job_id, jobs):
    job_time, child_ids = jobs[job_id]
    for child_id in child_ids:
        job_time += helper(child_id, jobs) 
    return job_time
    
    
jobs = [[1, 10, [2, 3]],
  [2, 20, [4]],
  [4, 40, []],
  [3, 30, []],
  [5, 10, [1, 2]]
]

find_job_total_time(job_id=1, jobs=jobs)
        
Solution().find_job_total_time(job_id=4, jobs=jobs)
Solution().find_job_total_time(job_id=1, jobs=jobs)
            
        






