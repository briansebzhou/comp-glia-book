astro_eqs = '''
#  [...]
# The astrocyte position in space
x : meter (constant)
y : meter (constant)
'''
#  [...]
# Arrange astrocytes in a grid
astrocytes.x = '(i / N_rows_a)*grid_dist - N_rows_a/2.0*grid_dist'
astrocytes.y = '(i % N_rows_a)*grid_dist - N_cols_a/2.0*grid_dist'