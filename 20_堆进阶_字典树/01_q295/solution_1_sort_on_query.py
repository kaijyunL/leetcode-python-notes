# 方法1：每次查询时排序
# addNum 直接追加；findMedian 时临时排序再取中间
# addNum O(1)，findMedian O(n log n)，空间 O(n)


class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        nums = sorted(self.nums)
        n = len(nums)
        mid = n // 2

        if n % 2 == 1:
            return float(nums[mid])
        return (nums[mid - 1] + nums[mid]) / 2.0


if __name__ == "__main__":
    finder = MedianFinder()
    finder.addNum(1)
    assert finder.findMedian() == 1.0
    finder.addNum(2)
    assert finder.findMedian() == 1.5
    finder.addNum(3)
    assert finder.findMedian() == 2.0

    finder = MedianFinder()
    for num, expected in [(5, 5.0), (15, 10.0), (1, 5.0), (3, 4.0)]:
        finder.addNum(num)
        assert finder.findMedian() == expected

    print("all tests passed")
