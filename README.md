# calculadora-de-IMC
¿Cómo hice mi programa?

Para realizar el proyecto me guié directamente del ejemplo y las variables que nos dio el profesor en clase y link, asegurándome de usar lo que hemos aprendido:

•	Ciclo repetitivo: Usé un bucle while para que, si alguien comete un error al ingresar un dato, el programa no se cierre y vuelva a pedir la información desde el inicio.

•	Captura de nombres: Pido el nombre y los apellidos con input() y reviso con un if que no dejen ningún espacio en blanco.

•	Control de errores en números: Para la edad, el peso y la estatura, usé un bloque try / except. Así, si alguien escribe letras en lugar de números o no pone nada, el programa avisa del error y pide los datos de nuevo sin trabarse.

•	Validación de datos reales: Me aseguro con un if de que los valores numéricos sean mayores a 0.

•	Cálculo y resultado: Convierto la estatura de centímetros a metros (dividiendo entre 100) y aplico la fórmula del IMC con el operador ** para la potencia de 2. Luego, con varios if / elif, clasifico el resultado (desde delgadez hasta obesidad mórbida) y al final muestro todo el resumen en pantalla.

Reflexión del Bootcamp

Ha sido una experiencia llena de retos pero muy gratificante. Al principio la lógica de programación imponía un reto grande, pero este proyecto me ayudó a entender lo importante que es validar lo que escribe el usuario para que el programa no falle. También le perdí el miedo a los errores en consola, ya que ahora los veo como una ayuda para corregir el código. 
