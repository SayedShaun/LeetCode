def trap(heights):
    left, right = 0, len(heights) - 1
    water = 0

    maxLeft = heights[left]
    maxRight = heights[right]

    while left < right:
        if heights[left] < heights[right]:
            maxLeft = max(maxLeft, heights[left])
            water += maxLeft - heights[left]
            left += 1

        else:
            maxRight = max(maxRight, heights[right])
            water += maxRight - heights[right]
            right -= 1

    return water


heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(heights))
