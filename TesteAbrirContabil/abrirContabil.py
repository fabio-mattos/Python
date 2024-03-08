import pyautogui
import time


#pausa para poder escrever no navegador
pyautogui.PAUSE = 0.3

#abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#abrir o site
pyautogui.write('https://contabil.lucasmattos.com.br/')
pyautogui.press("enter")

time.sleep(3)
#seleciona o campo de login
pyautogui.click(x=1370, y=530)

# Seleciona todo o conteúdo no campo pressionando Ctrl+A

pyautogui.hotkey('ctrl', 'a')
pyautogui.press('backspace')
pyautogui.write('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')


pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('backspace')
pyautogui.write('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
