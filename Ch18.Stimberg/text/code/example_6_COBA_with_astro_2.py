synapses_eqs = '''
#  [...]
# which astrocyte covers this synapse ?
astrocyte_index : integer (constant)
'''
#  [...]
exc_syn = Synapses(exc_neurons, neurons, model=synapses_eqs,
                   on_pre=synapses_action+'g_e_post += w_e*r_S',
                   method='linear')