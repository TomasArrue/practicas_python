"""
    10. Dada una lista con nombres de imágenes:

    imagenes=['im1','im2','im3']
    
    Generar una estructura que asocie 3 coordenadas ingresadas por teclado (x1, y1) , (x2, y2) y
    (x3, y3) , con cada elemento de la lista (en el mismo orden en que son ingresadas). Además
    verifique, mientras se van ingresando las coordenadas, que no hayan repetidas para una misma
    imagen; en dicho caso deberá volver a ingresarla.
"""
imagenes = ['im1','im2','im3']
dic = {}

for elem in imagenes:
    ok = False
    while not ok:
        x = int(input(("ingrese coord x: ")))
        y = int(input(("ingrese coord y: ")))
        coord =(x,y)
        if not coord in dic.values():
            ok = True
        if not ok:
            print("coordenada invalida, intente de nuevo")
    dic[elem] = coord
    print("coordenada guardada")

print(dic)

    