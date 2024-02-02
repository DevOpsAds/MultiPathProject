#from .iA.Neuronio_1.Multipolar import multipolar_start,Table_studies
#from .iA.Matematica.Multipolar import math_multipolar_start,math_Table_studies
from .models import meterorologia,Supplier
from django.db.models import Q
from .iA.Memoria.Binary import binary_converter
from .iA.decea_mil import meteorologia
import datetime
'''
def neuro_training():
    print(multipolar_start())
    Table_studies()
    print('controlle na escuta o ---------> implemento de modulo iA')
    progress = 'controlle em atividade !@@ 06 : controlle.py'
    return progress

def math_mathematical():
    print(math_multipolar_start())
    math_Table_studies()
    print('controlle na math_mathematical da supler na escuta o ---------> implemento de modulo iA')
    progress = 'controlle em atividade !@@ 06 : controlle.py'
    return progress
'''
def memory_binary():
    print('loading to activate de convertons!!!@by Controll py location supplier')

    #print(binary_converter.main('10101101101'))
    #print(binary_converter.hexa_main('56d'))
    print('controlle in Binary inteligency listener at supler  ON...na listen o ---------> implemento de modulo iA')
    progress = 'controlle em atividade !@@ 06 : controlle.py'
    return progress

def met_decea_mil():
    atvMeteorogica=meteorologia.cod_metar('ligad')  
    #atvMeteorogica=['SBBH', 'https//met.decea.mil.br', 'Taf', '08092023', '193138', '081400Z', '0818/0906', '06008KT', 'CAVOK', 'N', 'TX27/0818Z', 'TN18/0905Z', 'FM', '0821/0823', '10008KT', 'Qn', 'RMKPGF']

    return atvMeteorogica


def infor_meteorologia(inf): 
    data_hora_atual=datetime.datetime.now()

    dateToday= data_hora_atual.strftime("%d%m%Y")
    met_inf_today= meterorologia.objects.filter(Q(diadocsis=dateToday))


    if not met_inf_today:
        dados={}
        inf_mets=met_decea_mil()
        campos_modelo=["referencia","coleta","tipodoc","diadocsis","horadocsis","coletainfo1","coletainfo2","coletainfo3","coletainfo4","coletainfo5","coletainfo6","coletainfo7","coletainfo8","coletainfo9","coletainfo10","coletainfo12","coletainfo12",
            "coletainfo13","coletainfo14"]
        print("Capturados__Rede Meterologica!!!!",met_inf_today)
        for i,inf_met in enumerate(inf_mets):
            if i<len (campos_modelo):
                campos=campos_modelo[i]
                dados[campos]=inf_met
        objeto=meterorologia(**dados)

        objeto.save()

    else:
        print('infomações meteorologicas inseridas')

    #data=['SBBH', 'https//met.decea.mil.br', 'Metar', '08092023', '181056', '121520Z', '00545KT', 'cavok', '457THY', '27/12', 'Q1020']
 