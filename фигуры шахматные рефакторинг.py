start = input()
final = input()
letters_list = ['a','b','c','d','e','f','g','h']
for i in range(0,8):
    start = start.replace(letters_list[i], str(i+1))
    final = final.replace(letters_list[i], str(i+1))
x1 = start[0] 
y1 = start[1]
x2 = final[0]
y2 = final[1]
delta_x = int(x2) - int(x1)
delta_y = int(y2) - int(y1)
name = input()
coords = []
def pawn(x1, y1, x2, y2):
    if delta_x == 0 and abs(delta_y) == 1:
        coords.append(final)
def horse(x1, y1, x2, y2):
    if (abs(delta_x) == 1 and abs(delta_y) == 2) or (abs(delta_x) == 2 and abs(delta_y) == 1):
        coords.append(final)
def rook(x1, y1, x2, y2):
    if delta_x == 0 or delta_y == 0:
        coords.append(final)
def elephant(x1, y1, x2, y2):
    if abs(delta_x) == abs(delta_y):
        coords.append(final)
def king(x1, y1, x2, y2):
    if abs(delta_x) <= 1 and abs(delta_y) <= 1:
        coords.append(final)
if name == 'пешка':
    pawn(x1,y1, x2, y2)
if name == 'ладья':
    rook(x1, y1, x2, y2)
if name == 'конь':
    horse(x1, y1, x2, y2)
if name == 'слон':
    elephant(x1, y1, x2, y2)
if name == 'королева':
    rook(x1, y1, x2, y2)
    elephant(x1, y1, x2, y2)
if name == 'король':
    king(x1, y1, x2, y2)
if final in coords:
    print('сможет')
else:
    print('не сможет')
    
