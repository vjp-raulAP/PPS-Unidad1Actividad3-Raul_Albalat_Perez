# PPS-Unidad1Actividad3-Raul_Albalat_Perez
# **Análisis de Grafos de Flujo y Estrategias de Pruebas**  

En esta práctica, analizamos los grafos de flujo correspondientes a las funciones `division` y `multiplicacion`, identificando los caminos posibles en su ejecución. Además, evaluamos estrategias de prueba basadas en caja blanca y caja negra.  

## **1. Grafo de Flujo para la Función `division`**  

### **Código de la función**  
```python
def division(a, b):
    if b == 0:  # Nodo 1
        return "Error: División por cero"  # Nodo 2
    return a / b  # Nodo 3
```

### **Descripción del flujo de control**  
1. **Inicio (Nodo 1):** Se evalúa la condición `b == 0`.  
2. **Camino Verdadero:** Si `b == 0`, la función retorna un mensaje de error (**Nodo 2**).  
3. **Camino Falso:** Si `b != 0`, se realiza la operación de división y se retorna el resultado (**Nodo 3**).  

### **Diagrama del Grafo de Flujo**  
```
    (1) [Inicio]
        |
      b == 0 ?
      /     \
    Sí       No
   (2)       (3)
 "Error"    a / b
```

![](imagenes/diagrama_grafo_division.png)

## **2. Grafo de Flujo para la Función `multiplicacion`**  

### **Código de la función**  
```python
def multiplicacion(a, b):
    return a * b  # Nodo único
```

### **Descripción del flujo de control**  
1. **Inicio (Nodo 1):** La función realiza la operación `a * b` y retorna el resultado sin ninguna bifurcación.  

### **Diagrama del Grafo de Flujo**  
```
    (1) [Inicio]
        |
      a * b
```