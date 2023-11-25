import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import sys

if len(sys.argv)>2:
    cal_comida = sys.argv[1]
    cal_servicio = sys.argv[2]
else:
    cal_comida = 8
    cal_servicio = 6
    
x_qual = np.arange(0, 11, 1)
x_serv = np.arange(0, 11, 1)
x_tip = np.arange(5, 26, 1)

qual_lo = fuzz.trimf(x_qual, [0, 0, 5])
qual_md = fuzz.trimf(x_qual, [0, 5, 10])
qual_hi = fuzz.trimf(x_qual, [5, 10, 10])

serv_lo = fuzz.trimf(x_serv, [0, 0, 5])
serv_md = fuzz.trimf(x_serv, [0, 5, 10])
serv_hi = fuzz.trimf(x_serv, [5, 10, 10])

tip_lo = fuzz.trimf(x_tip, [5, 5, 13])
tip_md = fuzz.trimf(x_tip, [5, 13, 25])
tip_hi = fuzz.trimf(x_tip, [13, 25, 25])


qual_level_lo = fuzz.interp_membership(x_qual, qual_lo, cal_comida)
qual_level_md = fuzz.interp_membership(x_qual, qual_md, cal_comida)
qual_level_hi = fuzz.interp_membership(x_qual, qual_hi, cal_comida)

serv_level_lo = fuzz.interp_membership(x_serv, serv_lo, cal_servicio)
serv_level_md = fuzz.interp_membership(x_serv, serv_md, cal_servicio)
serv_level_hi = fuzz.interp_membership(x_serv, serv_hi, cal_servicio)

#Reglas de producción
#Regla1
active_rule1 = np.fmax(qual_level_lo, serv_level_lo)
tip_activation_lo = np.fmin(active_rule1, tip_lo)
#Regla2
tip_activation_md = np.fmin(serv_level_md, tip_md)
#Regla3
active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
tip_activation_hi = np.fmin(active_rule3, tip_hi)


aggregated = np.fmax(tip_activation_lo, np.fmax(tip_activation_md, tip_activation_hi))
tip = fuzz.defuzz(x_tip, aggregated, 'centroid')
print(tip)