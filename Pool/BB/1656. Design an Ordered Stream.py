class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.stream = [None] * n
        self.pointer = 0

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey-1] = value
        result = []
        while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:
            result.append(self.stream[self.pointer])
            self.pointer += 1
        return result

