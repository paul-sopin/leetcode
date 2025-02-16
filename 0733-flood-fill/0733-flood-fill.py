class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        image_height = len(image)
        image_length = len(image[0])
        og_color = image[sr][sc]
        def fill(sr, sc):
            if color == image[sr][sc]:
                return
            image[sr][sc] = color
            if sc > 0 and image[sr][sc - 1] == og_color:
                fill(sr, sc - 1)
            if sc < image_length - 1 and image[sr][sc + 1] == og_color:
                fill(sr, sc + 1)
            if sr > 0 and image[sr - 1][sc] == og_color:
                fill(sr - 1, sc)
            if sr < image_height - 1 and image[sr + 1][sc] == og_color:
                fill(sr + 1, sc)
        fill(sr,sc)
        return image