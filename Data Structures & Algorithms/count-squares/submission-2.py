class CountSquares:

    def __init__(self):
        self.x_map = defaultdict(int)
        self.points_map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_map[x] += 1
        self.points_map[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x_map = self.x_map
        points_map = self.points_map
        count = 0
        queryX, queryY = point
        for x in x_map:
            if (x, queryY) not in points_map:
                continue
            dx = queryX - x
            if dx == 0:
                continue
            # two distinct points [x, queryY] and [queryX, queryY]
            # count up and down
            if (x, queryY + dx) in points_map and (queryX, queryY + dx) in points_map:
                count += points_map[(x, queryY + dx)] * points_map[(queryX, queryY + dx)] * points_map[(x, queryY)]
            if (x, queryY - dx) in points_map and (queryX, queryY - dx) in points_map:
                count += points_map[(x, queryY - dx)] * points_map[(queryX, queryY - dx)] * points_map[(x, queryY)]
            
        return count
