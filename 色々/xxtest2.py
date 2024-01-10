import win32gui
import ctypes

def forground( hwnd, title):
    name = win32gui.GetWindowText(hwnd)
    if name.find(title) >= 0:

        # 最初化を戻す
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd,1) # SW_SHOWNORMAL

        ctypes.windll.user32.SetForegroundWindow(hwnd)
        return False # 列挙終了

win32gui.EnumWindows( forground, 'WAVE')

