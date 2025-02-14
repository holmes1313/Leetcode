# https://1o24bbs.com/t/topic/2690/4
"""
https://www.1point3acres.com/bbs/thread-841257-1-1.html

**
现有两种运算方式: 乘二或除三。输入一个target数，输出从1开始如何运用两种运算得到target。如target=10，则可以1*2*2*2*2/3*2 = 10，输出****/*

1 -> 当前queue存了[1]
1*2=2, 1/3=0 -> 当前queue存了[2,0]
2*2=4, 2/3=0(0已经遇到过了所以跳过), 0*2=0, 0/3=0(这里两个0也都跳过) -> 当前queue存了[4]
4*2=8, 4/3=1(1跳过) -> 当前queue存了[8]
8*2=16, 8/3=2(2跳过) -> 当前queue存了[16]
16*2=32, 16/3=5 -> 当前queue存了[32,5]
...
一直用bfs枚举所有可能性

问从1开始要么*2要么/3如何找到是否可以得到目标数字，propose了backtracking但是实在是没有时间了，问了一下base case,如果不可能找到解什么时候程序停止。问了是BFS还是DFS。如果用DFS怎么实现，如果BFS怎么实现。


We are given a starting number 1 and we need to transform it to a target number by using the following operations:

Multiply by 2 (* 2)
Integer divide by 3 (// 3)
The goal is to return all possible operation sequences that transform 1 to the target number.
"""
from collections import deque

def find_operations_sequence(target):
    # Edge case: If target is 1, no operations are needed.
    if target == 1:
        return [""]

    # BFS initialization: start with (number 1, empty operation sequence)
    queue = deque([(1, "")])
    visited = set([1])  # to avoid revisiting numbers
    result = []
    max_num = target * 10
    min_num = target // 3 // 2
    # Perform BFS
    while queue:
        current, ops = queue.popleft()

        if current == target:
            return ops

        # Try multiplying by 2
        next_value = current * 2
        if next_value <= max_num and next_value not in visited:
            queue.append((next_value, ops + "*"))
            visited.add(next_value)

        # Try integer division by 3, only if divisible by 3
        #if current % 3 == 0:
        next_value = current // 3
        if next_value >= min_num and next_value not in visited:
            queue.append((next_value, ops + "/"))
            visited.add(next_value)

    return result

# target = 15
# sequences = find_operations_sequence(target)
# print(sequences)




"""

有两个有序数组，一个有n个数例如[2,4,6,7,8]，另一个为范围区间例如[2,5,10]，输出一个bucket，其中每个元素为范围内数的个数。上面例子输出[2,3]，其中有两个数（2、4）在范围[2, 5]内，有三个数（6、7、8）在范围[5, 10]内。

这题就是双指针就可以了
i = 0; j = 1;
[2,5,10] 就是在2-5的范围内，之后再遍历[2,4,6,7,8]，2、4在这个范围内就是2
i = 1; j = 2;
此时范围变成5-10，因为之前遍历过了2和4现在从6开始，6、7、8都在范围内就是3
输出[2,3]


https://www.1point3acres.com/bbs/thread-715409-1-1.html
2021
第一个是 linked list add two numbers。有问到recursion可不可以做，但是可以选择用reverse的方法做。
还问了如果有negative number怎么办。
第二个是arriving packet的问题
example：(1, "e"), (3, "h"), (2, "a")
(3, "h") 必须要等到(2, "a") print以后才能print

https://www.1point3acres.com/bbs/thread-839382-1-1.html
伊尔医，follow up说可以buy sell两次但不能同时hold两个stock，问maximum profit，
"""
"""
https://www.1point3acres.com/bbs/thread-764916-1-1.html
第二题不知道题号，题目挺长，加上小哥说话结巴，搞了半天才明白。大概意思就是跑马拉松，每隔一段有个sensor，有人跑过就发出一个信号包括这个人的ID和sensor的ID，怎么样处理这些信号，能快速知道跑者的排名。

一个马拉松比赛，假设路上有10个marker，然后你需要设计几个函数 Top(k)
返回跑在前面的k个人的id， Update（runnerId，markerId）每次跑到某个marker的时候 call这个函数。Hashmap + linkedlist （虽然这里我觉得好像和LRU没太大的关系。别人的面经）
k can is given at runtime.
"""

class RunnerNode:
    def __init__(self, runnerId, num_markers_passed):
        self.runnerId = runnerId  # Runner's ID
        self.num_markers_passed = num_markers_passed  # Number of markers passed
        self.prev = None  # Previous node in the list
        self.next = None  # Next node in the list

class TopKRuners:
    def __init__(self, k):
        self.k = k  # The number of top runners we need to track
        self.runner_progress = {}  # Dictionary to store runner info (runnerId -> (set of markers, node))
        self.head = RunnerNode(None, -1)  # Dummy head (to simplify list manipulation)
        self.tail = RunnerNode(None, -1)  # Dummy tail
        self.head.next = self.tail  # Connect head to tail
        self.tail.prev = self.head  # Connect tail to head
        self.size = 0  # Track number of nodes in the list

    def _remove_node(self, node):
        """ Removes the given node from the linked list """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def _add_to_head(self, node):
        """ Adds the given node right after the head node """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def _update_position(self, runnerId, num_markers_passed):
        """ Updates the runner's position in the linked list based on their marker count """
        node = self.runner_progress[runnerId][1]
        self._remove_node(node)
        node.num_markers_passed = num_markers_passed
        
        # Re-insert the node at the correct position based on marker count
        current = self.head.next
        while current != self.tail and current.num_markers_passed >= node.num_markers_passed:
            current = current.next
        
        # Insert the node before the current node
        node.next = current
        node.prev = current.prev
        current.prev.next = node
        current.prev = node
        self.size += 1

    def update(self, runnerId, markerId):
        """
        Update the runner's progress when they pass a marker
        :param runnerId: ID of the runner
        :param markerId: ID of the marker
        """
        if runnerId not in self.runner_progress:
            # If it's a new runner, add them to the list with this marker
            node = RunnerNode(runnerId, 1)  # New runner, so 1 marker passed
            self.runner_progress[runnerId] = (set([markerId]), node)  # Initialize with this marker
            self._add_to_head(node)
        else:
            # Runner exists, check if they have passed this marker before
            passed_markers, node = self.runner_progress[runnerId]
            if markerId not in passed_markers:
                # If the runner hasn't passed this marker, add it to the set and update their progress
                passed_markers.add(markerId)
                new_marker_count = len(passed_markers)
                self.runner_progress[runnerId] = (passed_markers, node)
                self._update_position(runnerId, new_marker_count)

    def top_k(self):
        """
        Get the top k runners
        :return: List of top k runners' IDs
        """
        # Collect the top k runners from the list, starting from head
        top_runners = []
        current_node = self.head.next
        count = 0
        while current_node != self.tail and count < self.k:
            top_runners.append(current_node.runnerId)
            current_node = current_node.next
            count += 1
        return top_runners

# Example usage:
# top_k_runners = TopKRuners(k=3)

# # Update the progress of various runners
# top_k_runners.update(1, 0)  # Runner 1 passes marker 0
# top_k_runners.update(2, 0)  # Runner 2 passes marker 0
# top_k_runners.update(3, 0)  # Runner 3 passes marker 0
# top_k_runners.update(1, 1)  # Runner 1 passes marker 1
# top_k_runners.update(2, 1)  # Runner 2 passes marker 1
# top_k_runners.update(1, 2)  # Runner 1 passes marker 2

# # Get the top 3 runners
# print(top_k_runners.top_k())  # Expected Output: [1, 2, 3]

# top_k_runners.update(3, 1)  # Runner 3 passes marker 1

# # Get the top 3 runners again after an update
# print(top_k_runners.top_k())  # Expected Output: [1, 3, 2]



from sortedcontainers import SortedList

class MarathonRunners:
    def __init__(self):
        self.id_to_marker = {}
        self.sorted_runners = SortedList()

    def update(self, runner_id, marker):
        if runner_id not in self.id_to_marker:
            self.id_to_marker[runner_id] = marker
            self.sorted_runners.add((-marker, runner_id))  # logn
        else:
            old_marker = self.id_to_marker[runner_id]
            self.sorted_runners.remove((-old_marker, runner_id))
            self.id_to_marker[runner_id] = marker
            self.sorted_runners.add((-marker, runner_id))

    def top(self, k):
        top_runners = []
        for _, runner_id in self.sorted_runners[:k]:
            top_runners.append(runner_id)

        return top_runners

# top_k_runners = MarathonRunners()

# # Update the progress of various runners
# top_k_runners.update(1, 0)  # Runner 1 passes marker 0
# top_k_runners.update(2, 0)  # Runner 2 passes marker 0
# top_k_runners.update(3, 0)  # Runner 3 passes marker 0
# top_k_runners.update(1, 1)  # Runner 1 passes marker 1
# top_k_runners.update(2, 1)  # Runner 2 passes marker 1
# top_k_runners.update(2, 2)  # Runner 2 passes marker 1
# top_k_runners.update(1, 2)  # Runner 1 passes marker 2

# print(top_k_runners.sorted_runners)

# # Get the top 3 runners
# print(top_k_runners.top(3))  # Expected Output: [1, 2, 3]

# top_k_runners.update(3, 1)  # Runner 3 passes marker 1

# # Get the top 3 runners again after an update
# print(top_k_runners.top(3))  # Expected Output: [1, 3, 2]
                       
class RunnerNode:
    def __init__(self, runnerId):
        self.runnerId = runnerId  # Runner's ID
        self.prev = None  # Previous node in the list
        self.next = None  # Next node in the list


class Marker:
    def __init__(self, marker_id):
        self.marker_id = marker_id
        self.count = 0
        self.id_to_node = {}
        self.head = RunnerNode(runnerId=-1)
        self.tail = RunnerNode(runnerId=-2)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_runner(self, runner_id):
        if runner_id not in self.id_to_node:
            
            node = RunnerNode(runnerId=runner_id)
            # add node to the head
            self._add_to_head(node)

            self.id_to_node[runner_id] = node
            self.count += 1
        else:
            node = self.id_to_node[runner_id]
            # delete node
            self._remove(node)

            # add node to the head
            self._add_to_head(node)

    def _remove(self, node):
        # delete node
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        nxt.prev = node
        node.next = nxt


    def remove_runner(self, runner_id):
        if runner_id not in self.id_to_node:
            return
        node = self.id_to_node[runner_id]
        self._remove(node)
        self.count -= 1
        del self.id_to_node[runner_id]


class Marathon:
    def __init__(self, marker_count):
        self.markers = [Marker(i) for i in range(marker_count)]

    def update(self, runner_id, marker_id):
        marker = self.markers[marker_id]
        marker.add_runner(runner_id)
        if marker_id > 0:
            old_marker = self.markers[marker_id - 1]
            old_marker.remove_runner(runner_id)

    def top(self, k):
        top_k_runners = []
        for i in range(len(self.markers)-1, -1, -1):
            marker = self.markers[i]
            if marker.count > 0:
                curr = marker.tail.prev
                while curr and curr.prev:
                    top_k_runners.append(curr.runnerId)
                    if len(top_k_runners) == k:
                        return top_k_runners
                    curr = curr.prev
        return top_k_runners
        

top_k_runners = Marathon(5)

# Update the progress of various runners
top_k_runners.update(1, 0)  # Runner 1 passes marker 0
top_k_runners.update(2, 0)  # Runner 2 passes marker 0
top_k_runners.update(3, 0)  # Runner 3 passes marker 0
top_k_runners.update(1, 1)  # Runner 1 passes marker 1
import pdb;pdb.set_trace()
top_k_runners.update(2, 1)  # Runner 2 passes marker 1
top_k_runners.update(2, 2)  # Runner 2 passes marker 1
top_k_runners.update(1, 2)  # Runner 1 passes marker 2


# Get the top 3 runners
print(top_k_runners.top(3))  # Expected Output: [1, 2, 3]

top_k_runners.update(3, 1)  # Runner 3 passes marker 1

# Get the top 3 runners again after an update
print(top_k_runners.top(3))  # Expected Output: [1, 3, 2]



"""
https://www.1point3acres.com/bbs/thread-1097901-1-1.html
Coding 1
写一个Iterator，要求支持next(), hasNext(), reset()，这就是linkedlist 但是另外记录一下head保留着别扔。
running window medium
Coding + BQ
聊简历，聊对他们项目的看法
写一个统计学校里面成绩的代码，要求给出各科前10
SD + BQ
team lead聊简历，culture，然后设计一个挂单竞价系统
BQ
team lead 她老板，就聊聊motivation，passion之类的，没聊项目
"""
"""

https://www.1point3acres.com/bbs/thread-1100830-1-1.html
写一个class只有一个method 如果这个class在过去3秒内被call了more than 3 times return True不然return False
写了常规的queue.popleft（）被要求优化；要求对比current time和timestamps list里最后三个时间戳。问了time and space complexity。

https://www.1point3acres.com/bbs/thread-1102578-1-1.html
Was given a problem to call a function multiple times and a time constraint, If you call more than 3 times in last 3 sec, you need to return true otherwise false. I did the brute force approach but failed in optimizing the solution.

"""
import collections
import time

class RateLimiter:
    def __init__(self):
        self.queue = collections.deque()  # only keep calls within 3 secs
        
    def call(self):
        curr_time = time.time()

        while self.queue and self.queue[0] < curr_time - 3:
            self.queue.popleft()

        self.queue.append(curr_time)

        if len(self.queue) > 3:
            return True
        else:
            return False


"""



79
https://www.1point3acres.com/bbs/thread-1034146-1-1.html

394:
https://www.1point3acres.com/bbs/thread-1034146-1-1.html

"""

"""
https://www.1point3acres.com/bbs/thread-1108296-1-1.html
二轮 1h 自己出的 encode number 输入1113344 输出312324 要求不能转成string做
"""


def encode_num(n):
    result = 0
    prev_digit = -1
    curr_count = 0
    while n > 0:
        curr_digit = n % 10
        n //= 10

        if curr_digit == prev_digit:
            curr_count += 1
        else:
            if prev_digit != -1:
                result = result * 100 + prev_digit * 10 + curr_count

            curr_count = 1
            prev_digit = curr_digit
    
    if prev_digit != -1:
        result = result * 100 + prev_digit * 10 + curr_count

    resvered_result = 0
    while result > 0:
        resvered_result = resvered_result * 10 + result % 10
        result //= 10
    return resvered_result

print(encode_num(1113344))
