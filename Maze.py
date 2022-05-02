import Viewer

EMPTY = 0
WALL = 1
START = 2
END = 3
VISITED = 4
    
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

if __name__ == "__main__":
    grid = [
        [ WALL,  WALL,  EMPTY,  WALL,  WALL,  WALL,  EMPTY,  EMPTY,  WALL, WALL],
        [START, EMPTY,  WALL,  WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, WALL],
        [ WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, EMPTY,  WALL, WALL],
        [ WALL,  WALL,  WALL,  WALL, EMPTY,  WALL, EMPTY,  WALL, EMPTY, WALL],
        [ WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, EMPTY, EMPTY, EMPTY, WALL],
        [ WALL,  WALL, EMPTY,  WALL,  WALL, EMPTY, EMPTY,  WALL, EMPTY, WALL],
        [ WALL,  WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL,  WALL, EMPTY,  END],
        [ WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL, WALL],
    ]
                    
    Viewer.view(grid)
 

    print("Find a solution to get from ^^ to $$, using the characters " 
        + "'" + NORTH + "', '" + EAST + "', '" + SOUTH + "' and '" + WEST + "'"
        + " (for north, east, south and west).")
    solution = input("Your solution: ")

    currentRow = 1
    currentCol = 0
    done = False
    solved = False
    charIndex = 0
    solutionLength = len(solution)

    while not done and charIndex < solutionLength:
        
        direction = solution[charIndex]
        print("Location: (" + str(Row) + ", " + str(currentCol) 
            + "), next direction: '" + direction + "'")
        
        if direction == NORTH:
            Row -= 1
            
        elif direction == EAST:
            currentCol += 1
                
        elif direction == SOUTH:
            Row += 1
                
        elif direction == WEST:
            currentCol -= 1
        
        else:
            print("WRONG") # Invalid direction.
        
        if (Row < 0 or currentCol < 0 
                        or Row >= len(grid) 
                        or currentCol >= len(grid[Row])):
            done = True
            print("YOU FELL") # Out of bounds.
            
        else:
            if grid[Row][currentCol] == EMPTY:
                grid[Row][currentCol] = VISITED
                
            elif grid[Row][currentCol] == WALL:
                done = True
                print("HIT THE WALL") # Hit wall.

            elif grid[Row][currentCol] == END:
                done = True
                solved = True
                print("YOU LEFT!") # Solved.
                
            else:
                pass # Do nothing
        
        charIndex += 1
    # end-while


    if not solved:
        print("DEAD") # Did not reach the end.


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if grid[i][j] == EMPTY:
                print("  ", end = "")
                    
            elif grid[i][j] == WALL:
                print("##", end = "")
                    
            elif grid[i][j] == START:
                print("^^", end = "")
                    
            elif grid[i][j] == END:
                print("$$", end = "")
                    
            elif grid[i][j] == VISITED:
                print("..", end = "")
                    
            else:
                raise AssertionError
            
        print()
