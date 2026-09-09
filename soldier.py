import consts
import game_field


soldier_location = [consts.SOLDIER_X, consts.SOLDIER_Y]

def move_soldier(dx, dy):
    soldier_location[0] += dx
    soldier_location[1] += dy

def check_collision_with_bomb():
    for bomb in game_field.list_of_mines:
        if (soldier_location[0] < bomb[1] + consts.CELL_SIZE and
            soldier_location[0] + consts.CELL_SIZE > bomb[1] and
            soldier_location[1] < bomb[0] + consts.CELL_SIZE and
            soldier_location[1] + consts.CELL_SIZE > bomb[0]):
            return True
    return False




# if __name__=="__main__":
    # print_char(consts.SOLDIER_ROWS,consts.SOLDIER_COLS, 4)


