from PIL import Image
img = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
