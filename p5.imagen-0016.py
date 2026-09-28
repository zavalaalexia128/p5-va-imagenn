import cv2
## Leer la imagen con cv2 = computer vision
print(cv2.__version__)
img = cv2.imread('horgirl.jpg')
# determinar el tipo de imagenews
print(type(img))
# imprimir imagen
print(img.shape)
# Mostrando imagen
cv2.imshow('horgirl.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()