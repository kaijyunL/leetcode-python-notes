# 方法1：按 key 存所有版本，get 时从后往前找

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

        for current_timestamp, current_value in reversed(self.store[key]):
            if current_timestamp <= timestamp:
                return current_value

        return ""


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
    assert time_map.get("bar", 7) == "x"
    assert time_map.get("bar", 8) == "x"

    print("all tests passed")
