"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
 

Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""
import collections


class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        """
        The problem can be represented as a graph, where each gene string is a node, and there is an edge between two nodes if one gene can mutate to the other with exactly one character change. We need to find the shortest path from startGene to endGene, where each mutation is an edge in this graph.
        BFS is ideal for finding the shortest path in an unweighted graph.

        Start from startGene and treat it as the root node.
        For each gene string, explore all valid mutations (i.e., all gene strings that are one mutation away and are in the gene bank).
        Track visited nodes to prevent cycles and redundant work.
        When endGene is found, return the number of mutations.

        The queue will store tuples (currentGene, mutationCount) where currentGene is the current gene string, and mutationCount is the number of mutations taken to reach it.
        """
        bank_set = set(bank)
        
        if endGene not in bank_set:
            return -1

        valid_chars = ["A", "C", "G", "T"]
        queue = collections.deque([(startGene, 0)])

        visited = set()
        visited.add(startGene)

        while queue:
            curr_gene, mutations = queue.popleft()

            if curr_gene == endGene:
                return mutations

            for i in range(8):
                for char in valid_chars:
                    if curr_gene[i] == char:
                        continue

                    mutated_gene = curr_gene[:i] + char + curr_gene[i+1:]

                    if mutated_gene in bank_set and mutated_gene not in visited:
                        visited.add(mutated_gene)
                        queue.append((mutated_gene, mutations+1))

        return -1
