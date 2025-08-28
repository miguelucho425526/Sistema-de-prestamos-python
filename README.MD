# 📦 Sistema de Préstamos de Equipos

Este proyecto es un programa en **Python** que permite gestionar un inventario de equipos, registrar préstamos, devoluciones, historial y agregar nuevos elementos.  
El sistema funciona en **modo consola** y utiliza estructuras de datos básicas (diccionarios, listas y tuplas).

---

## 📝 Explicación de la solución implementada

La solución está basada en un **diccionario principal** llamado `equipos`, donde cada clave es el nombre de un equipo, y su valor es otro diccionario con:

- `disponible`: un valor booleano (`True` o `False`) que indica si el equipo está disponible.
- `prestamos`: una lista de tuplas inmutables `(usuario, fecha)` que guarda el historial de préstamos.

### Funciones principales:

1. **`mostrar_equipos()`**  
   Muestra todos los equipos del sistema con su estado actual.

2. **`registrar_prestamo()`**  
   Permite al usuario registrar un préstamo:
   - Pide el nombre del equipo.  
   - Pide el nombre del usuario.  
   - Registra el préstamo en el historial.  
   - Marca el equipo como *no disponible*.  

3. **`devolver_equipo()`**  
   Cambia el estado de un equipo a *disponible* si estaba prestado.  

4. **`ver_historial()`**  
   Muestra todos los préstamos realizados por cada equipo (usuario + fecha).  

5. **`agregar_equipo()`**  
   Permite registrar un nuevo equipo en el inventario con estado *disponible*.  

6. **`menu()`**  
   Es el menú interactivo principal que controla la ejecución del programa hasta que el usuario decida salir.  

---

## ▶️ Ejemplos de ejecución

### 1. Visualizar equipos disponibles

## 📂 Estructura del proyecto

  SISTEMA DE PRESTAMOS DE EQUIPOS
│── prestamos_equipos.py   
│── README.md           