
def main(): 
    f_val = open('bingo.txt') 
    f_boards = open('boards.txt')   
    values = [] 
    bingo_values = []
    boards = []
    board = [] 

    min_bingo = 1000

    #populate list of boards
    for b in f_boards:  
        if b != '\n': 
            items = b.replace('\n', '').split(' ') 

            if '' in items: 
                #items.remove('') 
                temp_item = [i for i in items if i != '']  
                items = temp_item

            board.append(items)
            
        else: 
            boards.append(board) 
            board = [] 
            bingo_values.append(0)

    for val in f_val: 
        values = val.split(',')

    
    

    for b in range(len(boards)): 
        print(f"board: {b}")
        for v in range(len(values)): 
            
            boards[b] = find_value(boards[b], values[v]) 
            if v > 3: 
                value = check_board(boards[b]) 

                #print(value)

                if value == True: 
                    bingo_values[b] = v 

                    if v < min_bingo: 
                        min_bingo = b

                    break 


    print("Final Values")
    print(*bingo_values) 



    print(f"Winning Value: {bingo_values[min_bingo]}")
     
    print(sum_board(boards[min_bingo]))
        


def find_value(board, value): 
    for i in range(len(board)): 
        for x in range(len(board[i])): 
            if board[i][x] == value: 
                board[i][x] = 'x' 
                #print(f"Value Found {value}: row:{i}, col:{x}")
                return board 
    return board


                
'''iterate through a board to check for bingo''' 
def check_board(board):
    isBingo = False 
    count = 0

    try:
        #check x axis 
        for r in range(len(board)): 
            for i in range(len(board[r])): 
                
                if board[r][i] == 'x': 
                    count += 1 
                    
            if count == len(board): 
                return True 
            else: 
                count = 0 

        #check y axis 
        for i in range(len(board)): 
            for r in range(len(board[i])):  
                        
                if board[r][i] == 'x': 
                    count += 1 
                    #print(count)

            if count == len(board): 
                return True 
            else: 
                count = 0  
        
        return False 
    except:  
        print('Error') 
        print('---------------------------------------')
        print(board) 
        quit()
        

#print board in readable format 
def print_board(print_board): 
     for b in print_board:
        for r in print_board: 
            for i in r: 
                print(f"i ", endl='')
            
            print() 
     print()


def sum_board(board): 
    sum_val = 0
    for i in range(len(board)): 
        for x in range(len(board)):
            if board[i][x] != 'x': 
                sum_val += int(board[i][x]) 
    return sum_val

if __name__ == '__main__': 
    main()