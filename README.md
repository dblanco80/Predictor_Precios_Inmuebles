# Predictor Precios Inmuebles

**Alumno**: Diego Blanco
 
Este repositorio contiene el trabajo final del curso de Data Science de CoderHouse. **Comision 48610**

## En el repositorio encontrará:

1. Notebook Colab con la consigna final del trabajo. Se recomienda visualizar la misma directamente desde google colab desde este [enlace](https://colab.research.google.com/drive/1gD-rPDXd8coG_37EIZa1FvkN2CxqiwqH?usp=sharing)
2. Modelo entrenado (modelo_entrenado.pkl)
3. Aplicación para interactuar con el modelo (app.py). La misma se realizó con la librería Flask.
4. Pequeño set de datos con algunos datos de prueba (pruebas_produccion.txt)

## Implementación del modelo

En una primera instancia la idea para poner el modelo productivo era utilizar una funcion lambda de aws que acceda a S3 para recuperar el modelo, esta funcion se accedería a través de AWS.
Esta implementación se descartó por problemas técnicos y se decidió montar un servidor EC2 en donde se tuvieron que instalar todas las dependencias y su posterior configuracion para poder se accedido desde internet.
Para interactuar con el modelo haga click en el siguiente [enlace](http://ec2-54-207-150-208.sa-east-1.compute.amazonaws.com:5000/)

## Consideraciones importantes

Se priorizó el funcionamiento del modelo y la implementación en AWS sobre cuestiones estéticas.
En una futura iteración se mejorará el diseño y la url.
