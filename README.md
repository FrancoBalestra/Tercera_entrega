# Proyecto Final Django

En este proyecto hay 3 clases, (Notebooks, celulares y monitores) las cuales se encuentran en models.py de aplicaciones, con sus respectivos formularios en forms.py y en las views.py
si ejecutamos la pagina en el navegador podemos ver que tenemos 7 botones, el (Digital Delights), que es el nombre del proyecto el cual si lo tocamos nos lleva al inicio con una breve introduccion de la pagina, despues tenemos el de (Notebooks), en el cual podemos ver el listado de notebooks que hay, el cual podemos buscarlas por nombre y podemos actualizar la informacion, borrar siempre y cuando estemos en una cuenta, si no estas con la sesion iniciada para poder actualizar y borrar es un requerimiento, despues tenemos los botones (Monitores y Celulares) en los cuales en ambos se puede hacer lo mismo que en el de Notebooks, solamente que lo que cambia es que estan programadas con clases basadas en vista, y que en estos ultimos no tenes un formulario de busqueda pero si tenes una confirmacion al momento de borrar algun elemento de la lista. Por ultimo, tenemos los ultimos 3 botones que son el de (Iniciar Sesion/la cuenta) en el cual podemos loguearnos y en el mismo boton ver la informacion del perfil que esta ingresado, en el boton de registrarse nos permite registrarse y el ultimo es el about, que nos sirve para ver un poco mas de info sobre mi.

los codigos que habria que poner en la terminal para arrancar el proyecto serian:

. myvenv/Scripts/activate

y

python manage.py runserver
