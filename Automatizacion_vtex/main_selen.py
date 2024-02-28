from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del navegador
driver = webdriver.Edge()  # Puedes usar otro navegador y configurarlo según lo necesario
driver.get("https://ledstudiocl.myvtex.com/admin/Site/produto.aspx")  # Abrir la página web

# Esperar a que el campo de correo electrónico esté presente y sea visible
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))
email_field.send_keys("wherrera@ledstudio.cl")

# Localizar y hacer clic en el botón "Siguiente" o cualquier otro botón relevante para continuar
continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='email-form-continue']")))
continue_button.click()

# Esperar a que el campo de contraseña esté presente y sea visible
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
password_field.send_keys("Ea7hava5*")

# Cerrar el navegador
driver.quit()


""" # Localizar y hacer clic en el botón "Siguiente" o cualquier otro botón relevante para continuar
continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='request-password-continue']")))
continue_button.click()

# Encontrar el botón de inicio de sesión y hacer clic en él
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Iniciar sesión')]")))
login_button.click()

# Esperar a que el inicio de sesión se complete
# Aquí podría esperar a que aparezca un elemento específico en la página de inicio después del inicio de sesión """

