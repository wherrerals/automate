import pyautogui
import time

# Función para abrir el bloc de notas
def abrir_notepad():
    # Abrir el menú de inicio (tecla Windows)
    pyautogui.press('win')
    # Escribir "bloc de notas" para buscarlo en el menú de inicio y esperar 1 segundo
    time.sleep(1)
    pyautogui.write('bloc de notas')
    # Esperar un poco para que aparezca la búsqueda y seleccionar "Bloc de notas" con la tecla Enter
    time.sleep(1)
    pyautogui.press('enter')

# Función para cerrar el bloc de notas
def cerrar_notepad():
    # Maximizar la ventana del bloc de notas
    pyautogui.hotkey('win', 'up')
    # Cerrar la ventana del bloc de notas
    pyautogui.hotkey('alt', 'f4')

# Llamar a las funciones para abrir y cerrar el bloc de notas
abrir_notepad()
time.sleep(5)  # Esperar 5 segundos antes de cerrar el bloc de notas
cerrar_notepad()
