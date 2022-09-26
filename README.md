# Documentación Dojos Equipo Verde

## Integrantes 
- Alexis Aranda Jara
- Sebastian Sartorato
- Nicolas De Bella
- Braian Nicolas Acosta Florentin
- Kervin Briceño
- Juan Manuel De Larrosa
- Manuel Gerez

## Proyecto: Empresa Frigorífica.

## Descripción
- Un sistema que mide la temperatura para una cámara frigorífica indicando la temperatura por el monitor en serie, utilizando un  display 7 segmentos que nos indique el nivel de temperatura

## Función principal
- En el loop se mapea la temperatura, si esta da un numero mayor a 24, se prende el led rojo, si la temperatura es menor a 0, es decir, si está fría, se prende el led azul, y si está entre 0 y 24 se prende el led amarillo, si es que está templada.


~~~ c (lenguaje en el que esta escrito)
void EncenderBinario(int estado3, int estado2,int estado1,int estado0)
{
  digitalWrite(B3,estado3);
  digitalWrite(B2,estado2);
  digitalWrite(B1,estado1);
  digitalWrite(B0,estado0);
}
~~~

## Link al proyecto
- [proyecto](https://www.tinkercad.com/things/cpsXQ8M7DW7-copy-of-empresa-frigorifica/editel?sharecode=9WF3Xlxy_DZAHYp1vw7OcVmMp6Cvaa7Vk7EJUZnH3Pg)
## :tv: Link al video del proceso
- [video]()

---






