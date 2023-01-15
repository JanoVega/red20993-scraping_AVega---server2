from pyvirtualdisplay import Display

from main_scraper import Crawler
from utils.date_utils import get_date
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

items = [#'ingenieria en informacion y control de gestion'\
          #  ,'ingenieria en administracion logistica'\
             'fonoaudiologa'\
         #'medicina nuclear'
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
dia_primera_ejecucion = '15/1/2023'

if get_date('hoy') == dia_primera_ejecucion:
    """ para instanciar los csv """
    Crawler.reset_data_base('Ofertas_de_empleos')


display = Display(visible=0, size=(800, 600))
display.start()

Crawler.search(items, sites)


display.stop()