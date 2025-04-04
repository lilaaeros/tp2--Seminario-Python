Requerimientos:
Hay que tener Python instalado desde python.org. 
Despues, instalá Jupyter con el comando desde el PowerShell de Windows
pip install notebook
Para ejecutar el notebook, ahi mismo pone:
jupyter notebook
Cuando se abre la ventana del navegador, tenes que abrir el archivo test.ipynb dentro de la carpeta notebooks/ y ejecutá las celdas en orden.
El código con las funciones necesarias está en la carpeta src/, en el archivo mis_funciones.py  (src/mis_funciones.py), por lo que el notebook debe estar configurado para importar desde ahí. 
Si en Jupyter aparece un error al importar funciones, hay que asegurarse de que el kernel esté usando el entorno de Python 3