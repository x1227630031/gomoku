import tkinter as tk
from tkinter import messagebox


board_size = 15
cell_size = 40
margin = 20
record_black = []
record_white = []
record_all = []

# 主窗口
root = tk.Tk()
root.title("五子棋游戏")

canvas = tk.Canvas(root, width=margin*2 + cell_size*(board_size-1),
                   height=margin*2 + cell_size*(board_size-1), bg="burlywood")
canvas.pack()

# 画棋盘
def draw_board():
    for i in range(board_size):
        canvas.create_line(margin, margin + i * cell_size,
                           margin + (board_size - 1) * cell_size, margin + i * cell_size)
        canvas.create_line(margin + i * cell_size, margin,
                           margin + i * cell_size, margin + (board_size - 1) * cell_size)


def get_index(x, y):
    col = round((x - margin) / cell_size)
    row = round((y - margin) / cell_size)
    return row * board_size + col, row, col

# 判断胜负
def check_win(record):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for idx in record:
        row = idx // board_size
        col = idx % board_size
        for dx, dy in directions:
            count = 1
            for d in [1, -1]:
                r, c = row, col
                while True:
                    r += d * dy
                    c += d * dx
                    if 0 <= r < board_size and 0 <= c < board_size and r * board_size + c in record:
                        count += 1
                    else:
                        break
            if count >= 5:
                return True
    return False

# 左键落黑子
def callback1(event):
    idx, row, col = get_index(event.x, event.y)
    if idx in record_all:
        return
    x = margin + col * cell_size
    y = margin + row * cell_size
    canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="black")
    record_black.append(idx)
    record_all.append(idx)
    if check_win(record_black):
        messagebox.showinfo("游戏结束", "黑棋获胜！🎉")

# 右键落白子
def callback2(event):
    idx, row, col = get_index(event.x, event.y)
    if idx in record_all:
        return
    x = margin + col * cell_size
    y = margin + row * cell_size
    canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white")
    record_white.append(idx)
    record_all.append(idx)
    if check_win(record_white):
        messagebox.showinfo("游戏结束", "白棋获胜！🎉")

# 开始游戏
def start_game():
    canvas.delete("all")
    global record_black, record_white, record_all
    record_black = []
    record_white = []
    record_all = []
    draw_board()

# 退出游戏
def quit_game():
    root.destroy()

# 顶部按钮区域
btn_frame = tk.Frame(root)
btn_frame.pack()

start_btn = tk.Button(btn_frame, text="Start", command=start_game)
start_btn.pack(side=tk.LEFT, padx=10, pady=5)

quit_btn = tk.Button(btn_frame, text="Quit", command=quit_game)
quit_btn.pack(side=tk.LEFT, padx=10, pady=5)

canvas.bind("<Button-1>", callback1)  # 左键
canvas.bind("<Button-3>", callback2)  # 右键


draw_board()


root.mainloop()
