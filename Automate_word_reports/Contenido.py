import pandas as pd

titulo_port = "Reporte de Avance diario, Acceso y Camino Deposito Cerro Gris"
fecha_hoy = pd.to_datetime("today").strftime("%d/%m/%Y")

trabajador_texto = "Un trabajador es la persona física que con la edad legal mínima presta servicios retribuidos " \
                   "subordinados a otra persona, a una empresa o institución. Si su edad es menor a la legal " \
                   "establecida, puede considerarse trabajo infantil y puede ser ilegal a menos que tenga, " \
                   "en ciertos casos, permiso de sus padres o tutores. Si, aun siendo una persona adulta, " \
                   "no presta los servicios de forma voluntaria, se considera esclavitud o servidumbre. "


nombre_tabla_1 = "Descripción de Trabajadores en Faena"