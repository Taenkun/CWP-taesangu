def get_board(board): # เตรียมกระดานและเช็คขนาด
    lines = board.split('\n')
    clean_lines = [] # ลบบรรทัดที่ว่าง
    
    for line in lines:
        if len(line) > 0:
            clean_lines.append(line) 
    if len(clean_lines) == 0:
        return None
        
    size = len(clean_lines)
    for line in clean_lines:     # กระดานสี่เหลี่ยมมั้ย
        if len(line) != size:
            return None
            
    return clean_lines

def find_king(clean_lines, size): # หา King 
    king_r = -1
    king_c = -1
    king_count = 0
    for r in range(size):
        for c in range(size):
            if clean_lines[r][c] == 'K':
                king_r = r
                king_c = c
                king_count += 1
    if king_count != 1:
        return -1, -1 # ผิดกฎ ติดลบ
        
    return king_r, king_c

def straight_check(clean_lines, king_r, king_c, size): # เช็คแนวตรง

    # ซ้าย, ขวา, บน, ล่าง เดินไปในแต่ละทิศ [แถว, คอลัมน์] ในทางตรง
    straight_moves = [
        [-1, 0], # ขึ้นบน แถวลด
        [1, 0],  # ลงล่าง แถวเพิ่ม
        [0, -1], # ซ้าย คอลัมน์ลด
        [0, 1]   # ขวา คอลัมน์เพิ่มขึ้น
    ]
    
    for move in straight_moves:
        step_r = move[0]
        step_c = move[1]
        current_r = king_r + step_r   # จุดเริ่มต้น = ช่องถัดจาก King
        current_c = king_c + step_c
        
        # เดินหน้าจนกว่าจะตกขอบ
        while current_r >= 0 and current_r < size and current_c >= 0 and current_c < size:
            piece = clean_lines[current_r][current_c]
            if piece == 'R' or piece == 'Q': # เจอ Rook หรือ Queen = โดนรุก
                return True
            elif piece == 'P' or piece == 'B' or piece == 'K': # เจอตัวอื่น
                break # ไปทิศอื่นต่อ
            current_r += step_r  # เดินต่อทิศเดิม
            current_c += step_c
            
    return False

# เช็คแนวทแยง
def diagonal_check(clean_lines, king_r, king_c, size):
    diagonal_moves = [
        [-1, -1], # ซ้ายบน
        [-1, 1],  # ขวาบน
        [1, -1],  # ซ้ายล่าง
        [1, 1]    # ขวาล่าง
    ]
    
    for move in diagonal_moves:
        step_r = move[0]
        step_c = move[1]
        current_r = king_r + step_r
        current_c = king_c + step_c
        distance = 1 # นับระยะห่าง เอาไว้เช็คเงื่อนไขของ Pawn
        
        while current_r >= 0 and current_r < size and current_c >= 0 and current_c < size:
            piece = clean_lines[current_r][current_c]  
            if piece == 'B' or piece == 'Q':             # Bishop หรือ Queen = โดนรุก
                return True
            # Pawn รุกทแยงขึ้นด้านบน+จะต้องอยู่ด้านล่างในมุมK step_r == 1 distance == 1 แถวเพิ่ม+อยู่ติดกัน
            elif piece == 'P' and distance == 1 and step_r == 1:
                return True
            elif piece == 'P' or piece == 'R' or piece == 'K': # เจอตัวอื่น
                break
            current_r += step_r
            current_c += step_c
            distance += 1 
    return False

# main func
def checkmate(board):
    # call get_board
    clean_lines = get_board(board)
    if clean_lines == None:
        return
    size = len(clean_lines)

    # call find_king
    king_r, king_c = find_king(clean_lines, size)
    if king_r == -1:
        return
        
    # call straight_check
    if straight_check(clean_lines, king_r, king_c, size) == True:
        print("Success")
        return
        
    # call diagonal_check
    if diagonal_check (clean_lines, king_r, king_c, size) == True:
        print("Success")
        return
    print("Fail") # รอดหมดเลย