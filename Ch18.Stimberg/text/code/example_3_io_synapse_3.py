astro_eqs = '''
#  [...]
# Fraction of gliotransmitter resources available:
dx_A/dt = Omega_A * (1 - x_A)      : 1
# gliotransmitter concentration in the extracellular space:
dG_A/dt = -Omega_e*G_A             : mmolar
'''
glio_release = '''
G_A += rho_e * G_T * U_A * x_A
x_A -= U_A *  x_A
'''