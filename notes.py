# -*- coding: utf-8 -*-
"""
Leetcode notes

Created on Tue Sep 24 22:56:10 2019

@author: z.chen7
"""

# OrderedDict objects
"""
An OrderedDict is a dict that remembers the order that keys were first inserted.
If a new entry overwrites an existing entry, the original insertion position is left unchanged.
Deleting an entry and reinserting it will move it to the end."""

from collections import OrderedDict

# regular unsorted dictionary
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
OrderedDict(sorted(d.items(), key=lambda t:t[0]))

# dictionary sorted by value
OrderedDict(sorted(d.items(), key=lambda t:t[1]))

# dictionary sorted by length of the key string
OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
