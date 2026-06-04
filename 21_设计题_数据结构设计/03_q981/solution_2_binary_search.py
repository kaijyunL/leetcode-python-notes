# 方法2：按 key 存时间序列 + 二分查找（面试主推）

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        records = self.store[key]
        left = 0
        right = len(records) - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2
            current_timestamp, current_value = records[mid]

            if current_timestamp <= timestamp:
                answer = current_value
                left = mid + 1
            else:
                right = mid - 1

        return answer


if __name__ == "__main__":
    time_map = TimeMap()

    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"

    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"

    assert time_map.get("foo", 0) == ""
    assert time_map.get("missing", 10) == ""

    time_map.set("bar", "x", 7)
    time_map.set("bar", "y", 9)
    assert time_map.get("bar", 6) == ""
    assert time_map.get("bar", 7) == "x"
    assert time_map.get("bar", 8) == "x"
    assert time_map.get("bar", 9) == "y"
    assert time_map.get("bar", 100) == "y"

    print("all tests passed")
