# Trapping Rain Water


# v1 - Brute Force
# Time: O(n^2)
# Space: O(1)

class SolutionV1:
    def trap(self, height):
        tot_water = 0

        for i in range(len(height)):
            left_max = 0
            right_max = 0

            if i == 0 or i == len(height) - 1:
                continue

            for left in range(i):
                if height[left] > left_max:
                    left_max = height[left]

            for right in range(i + 1, len(height)):
                if height[right] > right_max:
                    right_max = height[right]

            water = min(left_max, right_max) - height[i]

            if water > 0:
                tot_water += water

        return tot_water


# v2 - Left Max + Right Max Arrays
# Time: O(n)
# Space: O(n)

class SolutionV2:
    def trap(self, height):
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        tot_water = 0

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i - 1])

        for j in range(len(height) - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], height[j + 1])

        for k in range(len(height)):
            water = min(left_max[k], right_max[k]) - height[k]

            if water > 0:
                tot_water += water

        return tot_water


# v3 - Left Max Array + Running Right Max
# Time: O(n)
# Space: O(n)

class SolutionV3:
    def trap(self, height):
        left_max = [0] * len(height)
        right_max = 0
        tot_water = 0

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i - 1])

        for j in range(len(height) - 1, -1, -1):
            water = min(left_max[j], right_max) - height[j]

            if water > 0:
                tot_water += water

            right_max = max(right_max, height[j])

        return tot_water


# v4 - Two Pointers using Current Heights
# Time: O(n)
# Space: O(1)

class SolutionV4:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0
        tot_water = 0

        while left < right:

            if height[left] <= height[right]:

                if height[left] > left_max:
                    left_max = height[left]
                else:
                    tot_water += left_max - height[left]

                left += 1

            else:

                if height[right] > right_max:
                    right_max = height[right]
                else:
                    tot_water += right_max - height[right]

                right -= 1

        return tot_water


# v5 - Two Pointers using Left Max vs Right Max
# Time: O(n)
# Space: O(1)

class Solution:
    def trap(self, height):
        if not height:
            return 0

        left = 1
        right = len(height) - 2

        left_max = height[0]
        right_max = height[-1]

        tot_water = 0

        while left <= right:

            if left_max < right_max:
                water = left_max - height[left]

                if height[left] > left_max:
                    left_max = height[left]

                left += 1

            else:
                water = right_max - height[right]

                if height[right] > right_max:
                    right_max = height[right]

                right -= 1

            if water > 0:
                tot_water += water

        return tot_water