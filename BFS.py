from collections import deque
def countIslands(grid):
    count = 0
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 or (i, j) in visited:
                continue
            bfs(grid, visited, i, j)
            count += 1

    return count
# map grid to graph
# perform bfs while traversing
# have a visted map of places you've been 
# update with bfs
# if you visit a node already don't bfs add one to count for that island
def bfs(grid, visited, row, col):
    queue = deque([(row, col)])
    visited.add((row, col))

    while len(queue) > 0:
        row, col = queue.popleft()
        for nr, nc in adjacent_lands(grid, row, col):
            if (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            queue.append((nr, nc))


# Iterator that generates land coordinates
def adjacent_lands(grid, row, col):
    for next_row, next_col in dirs(row, col):
        if out_of_bounds(grid, next_row, next_col):
            continue
        if grid[next_row][next_col] != '1':
            continue
        yield next_row, next_col


# Iterator that generates all the directions
def dirs(row, col):
    yield row + 1, col
    yield row - 1, col
    yield row, col + 1
    yield row, col - 1
def out_of_bounds(grid, next_row, next_col):
    if 0 <= next_row <= len(grid):
        return True
    if 0 <= next_col <= len(grid[0]):
        return True
    return False

class Solution:
    def numIslands(self, grid = [[]]):
        countIslands(grid)
ans = Solution()
# std::vector<std::vector<bool>> mylist = {}
print(ans.numIslands([ ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"] ]))

# class Solution {
# private:
#     vector<vector<bool>> visited;
#     vector<int> dx  {0, 0, 1, -1};
#     vector<int> dy {1, -1, 0, 0};
    
# public:
    
#     int numIslands(vector<vector<char>>& grid) {
#         if (grid.empty() || grid[0].empty())
#             return 0;
        
#         vector<vector<char>> islands = grid;
#         visited = vector<vector<bool>>(grid.size(), vector<bool>(grid[0].size(), false));
        
#         int count = 0;
#         for (int i = 0; i < grid.size(); ++i) {
#             for (int j = 0; j < grid[i].size(); ++j) {
#                 if (!visited[i][j] && grid[i][j] == '1') {
#                     bfs(grid, i, j);
#                     ++count;
#                 }
#             }
#         }
#         return count;
#     }
    
#     void bfs(vector<vector<char>> &grid, int row, int col) {
#         queue<tuple<int, int>> que;
#         visited[row][col] = true;
        
#         for (que.push({row, col}); !que.empty(); que.pop()) {
#             auto [row, col] = que.front();
#             for (int i = 0; i < 4; ++i) {
#                 int nextRow = row + dx[i];
#                 int nextCol = col + dy[i];
                
#                 if (!inBounds(grid, nextRow, nextCol))
#                     continue;
#                 if (visited[nextRow][nextCol])
#                     continue;
#                 if (grid[nextRow][nextCol] == '0')
#                     continue;
                
#                 que.push({nextRow, nextCol});
#                 visited[nextRow][nextCol] = true;
#             }
#         }
#     }
    
#     bool inBounds(vector<vector<char>> &grid, int row, int col) {
#         return (0 <= row) && (row < grid.size()) && (0 <= col) && (col < grid[row].size());
#     }
# };