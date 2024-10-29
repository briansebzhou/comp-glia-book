astro_eqs = '''
# Fraction of activated astrocyte receptors:
dGamma_A/dt = O_N * Y_S * (1 - Gamma_A) -
              Omega_N*(1 + zeta * C/(C + K_KC)) * Gamma_A : 1

# IP_3 dynamics:
dI/dt = J_beta + J_delta - J_3K - J_5P + J_ex     : mmolar
J_beta = O_beta * Gamma_A                         : mmolar/second
J_delta = O_delta/(1 + I/kappa_delta) *
                         C**2/(C**2 + K_delta**2) : mmolar/second
J_3K = O_3K * C**4/(C**4 + K_D**4) * I/(I + K_3K) : mmolar/second
J_5P = Omega_5P*I                                 : mmolar/second
delta_I_bias = I - I_bias : mmolar
J_ex = -F_ex/2*(1 + tanh((abs(delta_I_bias) - I_Theta)/omega_I)) *
                sign(delta_I_bias)                : mmolar/second
I_bias                                            : mmolar (constant)

# Ca^2+-induced Ca^2+ release:
dC/dt = J_r + J_l - J_p                : mmolar
# IP3R de-inactivation probability
dh/dt = (h_inf - h_clipped)/tau_h *
        (1 + noise*xi*tau_h**0.5)      : 1
h_clipped = clip(h,0,1)                : 1
J_r = (Omega_C * m_inf**3 * h_clipped**3) *
      (C_T - (1 + rho_A)*C)            : mmolar/second
J_l = Omega_L * (C_T - (1 + rho_A)*C)  : mmolar/second
J_p = O_P * C**2/(C**2 + K_P**2)       : mmolar/second
m_inf = I/(I + d_1) * C/(C + d_5)      : 1
h_inf = Q_2/(Q_2 + C)                  : 1
tau_h = 1/(O_2 * (Q_2 + C))            : second
Q_2 = d_2 * (I + d_1)/(I + d_3)        : mmolar

# Neurotransmitter concentration in the extracellular space
Y_S     : mmolar
# Noise flag
noise   : 1 (constant)
'''
# Milstein integration method for the multiplicative noise
astrocytes = NeuronGroup(2, astro_eqs, method='milstein')