from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Scraperweb:
    def __init__(self, 
                 url, nombre_articulo, precio_tachado, precio_actual, porcentaje_de_descuento,
                 ranting, cuotas, envio_y_garantia, producto_full, seller, vendido_por, descripcion,
                 atributos, url_producto, url_img, modal_envio, url_ficha, url_img_principal):
        self.url = url
        self.options = Options()
        '''
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-gpu")'''
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        self.driver = webdriver.Chrome(options=self.options)

        # CONTENIDO
        self.nombre_articulo = nombre_articulo
        self.precio_tachado = precio_tachado
        self.precio_actual = precio_actual
        self.porcentaje_de_descuento = porcentaje_de_descuento
        self.ranting = ranting
        self.cuotas = cuotas
        self.envio_y_garantia = envio_y_garantia
        self.producto_full = producto_full
        self.seller = seller
        self.vendido_por = vendido_por
        self.descripcion = descripcion
        self.atributos = atributos
        self.url_producto = url_producto
        self.url_img = url_img
        
        # VENTANAS
        self.modal_envio = modal_envio

        # Obtener url y links img desde la card antes del acceder a la ficha del producto
        self.url_ficha = url_ficha
        self.url_img_principal = url_img_principal

    def obtener_urls_ficha(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            
        except Exception as e:
            return str(e)
        finally:
            self.driver.quit()


