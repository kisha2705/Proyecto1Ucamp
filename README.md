# Ucamp
## Proyecto 1
### Calculadora de I.M.C.


Este es el primer repositorio que creo sola para cumplir con la primer tarea de este curso.

Para realizar el proyecto, lo primero que hice fue elaborar una lista en base a la descripción de los puntos que requiere el ejercicio, entre ellos están pedir al usuario:

* Nombre
* Apellido paterno
* Apellido materno
* Edad
* Peso
* Estatura
* Tomar en cuenta que ningún dato quede vacio
* Los datos que se ingresen en edad, peso y estatura tienen que ser una cifra
* Calcular el I.M.C.
* Desplegar en pantalla todos los datos anterios y el I.M.C que tiene el usuario

Aparte de los datos solicitados, agregué unos donde marca si el usuario tiene un peso bajo, normal o sobrepeso, de acuerdo al resultado que arroja su I.M.C. 

Elabore los puntos en base a los temas abordados en este primer módulo, variables, operadores y cadenas de texto, asi como algunos condicionales.

Para pedir datos al ususario utilicé el input, creando variables donde se guardan los datos que este proporcionará, el print no puede faltar para desplegar en pantalla lo que solicita y dar el resultado de su I.M.C con la ayuda de operadores como el / que es para dividir y el ** que es para expresar potencias, utilizados en la fórmula para saber el I.M.C., en las variables creadas para el peso, edad y estatura utilice el int y float para asegurarme que se ingrese una cifra, el if lo utilice para condicionar que se cumpla que los datos no pueden estar vacios y el while para que se repitan algunos si es que el dato a quedado vacio, en caso de que otros datos esten vacios utilice el sys.exit(-1) para que se salga del programa si el usuario no coloca nada en el dato que se le pide, también utilicé el if para que si el I.M.C esta en un rango se imprima su peso acorde a lo expresado en el programa, el elif para que si no se cumple lo marcado en el if se imprima las diferentes opciones que hay en los rangos establecidos y el else por si no se cumple ni el if, ni el elif, haya una opción diferente. Utilicé una cadena formateada para desplegar en pantalla todos los datos que se han guardado y el resultado del I.M.C. y en este asegurarme que en peso y estatura aparezcan dos decimales.


### Experiencia dentro del Bootcamp
El bootcamp ha cumplido las expectativas que tenía respecto a este, gracias a el, me puedo dar cuenta que la programación es muy interesante y todo un reto, bien dicen que la práctica hace al maestro y para ser bueno programando se necesita de mucha práctica, con la ayuda del material que nos brindan en la plataforma de trabajo se me hace más fácil entender como poder realizar un programa, asi como las clases tan interesantes que he tenido, se complementan perfecto para terminar de entender el tema que se aborda y si hay dudas aclararlas.