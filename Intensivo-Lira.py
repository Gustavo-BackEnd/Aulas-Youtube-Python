import pyautogui
import time
import pandas as pd
import pyperclip
pyautogui.PAUSE = 2


# Passo 1 - Entrar no sistema da empresa
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('ctrl', 't')  # nova janela no navegador
pyautogui.write('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.press('enter')
time.sleep(5)

# Passo 2 - Navegar até o relatório(entrar na pasta
# pyautogui.position - mostrar a posição do mouse se não aparecer poem dentro do print
pyautogui.click(x=360, y=312, clicks=2)
time.sleep(5)
# Passo 3 - Fazer download do relatório
pyautogui.click(x=446, y=338)
pyautogui.click(x=1172, y=200)
pyautogui.click(x=947, y=585)
time.sleep(2)
pyautogui.click(x=1150, y=142)
time.sleep(2)
pyautogui.click(x=506, y=455)
time.sleep(5)

# Passo 4 - Calcular indicadores (Faturamento e quantidade de produtos)
tabela = pd.read_excel(r'C:\Users\gu_al\OneDrive\Área de Trabalho\Intencivo\Vendas - Dez.xlsx')
# O r no inicio do diretório, sempre tem que por para o Python entender que é o diretório
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

# Enviar e-mail para diretoria
pyautogui.hotkey('ctrl', 't')  # nova janela no navegador
pyautogui.write('https://mail.google.com/mail/u/0/?ogbl#inbox')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=92, y=192)
time.sleep(2)
pyautogui.write('helen-maris1@hotmail.com')
time.sleep(2)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')
texto = f"""Prezados, bom dia!
O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: R${quantidade:,}

Abs
Gustavo Alves - Equip Back-End
"""
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')
