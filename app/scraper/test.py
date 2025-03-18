from scraper import Scraperweb

nombre_articulo = ""
precio_tachado = ""
precio_actual = ""
porcentaje_de_descuento = ""
ranting = ""
cuotas = ""
envio_y_garantia = ""
producto_full = ""
seller = ""
vendido_por = ""
descripcion = ""
atributos = ""
url_producto = ""
url_img = ""

# VENTANAS
modal_envio = ""

# Obtener url y links img desde la card antes del acceder a la ficha del producto
url_ficha = ""
url_img_principal = ""

url = "https://www.fravega.com/"
test = Scraperweb(url, nombre_articulo, precio_tachado, precio_actual, porcentaje_de_descuento,
                 ranting, cuotas, envio_y_garantia, producto_full, seller, vendido_por, descripcion,
                 atributos, url_producto, url_img, modal_envio, url_ficha, url_img_principal)
result = test.obtener_urls_ficha()
print(result)