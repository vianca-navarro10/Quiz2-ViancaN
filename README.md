Propietario del Repositorio: Vianca Navarro Chaves
En este repositorio se encuentra un código que permite a quien lo use convertir una cantidad deseada de dinero de dólares 
a la moneda colones, esto utilizando una tasa de conversión de 517.47.

Instrucciones de uso.
Tras clonar y correr el código:
1. Ingrese el valor numérico de dólares que desea cambiar en laentrada. (De colocar una entrada no numérica la aplicación le indicara el error.)
2. Presione la casilla "convertir", el resultado dado será el valor en colones del monto colocado.
3. Presione "limpiar" si desea limpiar la pantalla y convertir más datos.
4. En caso de que desee salir, presione la "X", se le mostrará una pantalla para verificar que usted desee salir.

Implementación del código:
Se inicia importando el módulo tkinter para llevar al cabo el programa, después de esto, se definen las funciones: "conversion", "limpiar_pantalla" y "cerrar",
en las que, respectivamente, se define la tasa de conversión y el proceso a llevar a cabo para el proceso, para después definir una que limpie la pantalla y 
una que cierre a la misma. Estas funciones serás llamadas después para el desarrollo de la aplicación.
1. Ventana principal: con "tk.Tk()" se crea la ventana principal de la aplicación, para después definir su título con "ventana.title" y, finalmente,
"con ventana.geometry" definir el tamaño deseado o indicado de la pantalla.
2. Entrada de datos y diseño: Se muestra el uso de "tk.label, entry y grid" para mostrar el texto que le indica al usuario qué hacer (ingresar monto en USD), con label, dar
al usuario un espacio en el que dé la entrada numérica del monto en dólares, y grid, coloca los widgets en una cuadrícula.
3. Botones: Para este espacio utilizamos el uso correcto de Button y grid. Button es utilizado para comandar los botones de "convertir" y "limpiar". Mientras que el grid se implementa
para definir las columnas en las que se colocan los botones.
4. Mostrar el resultado: Se utilizael label y el grid para indicar los resultados y posicionarlos en la pantalla.  
5. Salida del programa: Con el "ventana.protocol("WM_DELETE_WINDOW", cerrar)" se cierra la pantalla, pidiendo primero en una subventana la confirmación para salir.

Resultados:

