Con esta práctica, leemos de un fichero (divisas.txt) los datos proporcionados respecto al dinero que tenemos en diferentes divisas. 

Leemos estos datos y nos conectamos a la API https://api.exchangeratesapi.io/latest con el fin de obtener los datos para hacer
la conversión a euros y obtener el total de euros que tenemos en la fecha actual. Es decir, buscamos entre los datos proporcionados por la API cuanto vale en euros la divisa y lo convertimos y así vamos convirtiendo las diferentes divisas sumando hasta dar con el total.

Estos datos luego los guardamos en ahorros.txt, con la información de nuestros dinero total en la fecha realizada la conversión. 

Al obtener los datos que nos proporciona la API, los decodificamos con json para poder utilizarlos luego como csv, ya que facilita el trabajo a la hora de leer los datos y comparar.
