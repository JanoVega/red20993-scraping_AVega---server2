from pyvirtualdisplay import Display

from main_scraper import Crawler
from utils.date_utils import get_date
from utils.check_utils import get_not_0
from utils.email_utils import send_check_msg

"""
Sitios que funcionan:
    
    -chiletrabajos
    -opcionempleo
    -elmercurio
    -indeed
    -trabajando
    -laborum
    -computrabajo
    
Sitios que no funcionan

    -bne
    -empleospublicos

"""

items = ['ingenieria en informacion y control de gestion'\
            ,'ingenieria en administracion logistica'\
             'fonoaudiologa'\
         'medicina nuclear'
                ]


sites = ['chiletrabajos',\
         'opcionempleo',\
         'computrabajo',\
         'elmercurio',\
         'trabajando',\
         'laborum',\
         'indeed',\
         ]

    
""" formato  día/mes/año, dia y mes sin 0 a la izquerda, ej: 2/5/2022 """
dia_primera_ejecucion = '27/1/2023'

if get_date('hoy') == dia_primera_ejecucion:
    """ para instanciar los csv """
    Crawler.reset_data_base('Ofertas_de_empleos')


display = Display(visible=0, size=(800, 600))
display.start()

#Crawler.check(sites)
# se filtran los sitios que no tuvieron resultados
#sites = [sites[n] for n in get_not_0()]

Crawler.search(items, sites)
try:
    send_check_msg()
except Exception as e:
    print(e)

# SMTP para enviar correo

#correo normal
#correo extra en caso de errores
#https://docs.python.org/3/library/smtplib.html


display.stop()