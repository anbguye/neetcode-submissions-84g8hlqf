class TimeMap:

    def __init__(self):
        self.stored = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stored[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, vals = "", self.stored[key]
        l, r = 0, len(vals) - 1

        while l <= r:

            mid = (r + l) // 2

            if vals[mid][1] <= timestamp:
                res = vals[mid][0]
                l = mid + 1 
            else:
                r = mid - 1

        return res 
