
#Nombre: Darwin Rafael Castro Garcia
#Grupo: 7


Maiz_grano = 285.55
Cajas_v_M = 417
Pepino = 334.72
Cajas_v_P = 217
Tomate_verde = 129.00
Cajas_v_TV = 470
Venta_Productos = [
[ 2 , 122 ],
[ 1 , 89 ],
[ 1 , 22 ],
[ 3 , 48 ],
[ 1 , 75 ],
[ 3 , 322 ],
[ 2 , 95 ],
[ 1 , 148 ],
[ 1 , 83 ],
[ 3 , 100 ]
]

Id_producto_select = int(input('Ingrese el ID del producto: '))

if(Id_producto_select == 1):
  Resultado_cajaMaiz = Maiz_grano * Cajas_v_M
  print('El producto es: Maiz grano')
  print('El precio de la caja es: ',Maiz_grano)
  Porciento_M = Cajas_v_M > 1500
  print('Aplica el 20% de descuento: ',Porciento_M)
  print ('El costo total a pagar es: ',Resultado_cajaMaiz)

if(Id_producto_select == 2):
  Resultado_cajaPe = Pepino * Cajas_v_P
  print('El producto es: Pepino')
  print ('El precio de la caja es: ',Pepino)
  Porciento_P= Cajas_v_P > 1500
  print('Aplica el 20% de descuento: ',Porciento_P)
  print ('El costo total a pagar es: ',Resultado_cajaPe)
if(Id_producto_select == 3):
  Resultado_cajaToma = Tomate_verde * Cajas_v_TV
  print('El producto es: Tomate Verde')
  print('El precio de la caja es: ',Tomate_verde)
  Porciento_Tv = Cajas_v_TV > 1500
  print('Aplica el 20% de descuento: ',Porciento_Tv)
  print('El costo total a pagar es: ',Resultado_cajaToma)

  