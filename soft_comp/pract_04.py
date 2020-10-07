'''
soft comp practical 4
'''
import numpy
from neuron import Neuron, signum #Neuron class written in practical 3

def show_output(gate, gate_inputs_list):
    '''
    helper function to display output
    '''
    for gate_input in gate_inputs_list:
        gate._inputs = numpy.array(gate_input)
        print(f'x1:{g_input[0]} x2:{g_input[1]} O:', gate.calc_out())

gate_inputs = [[0,0],[0,1],[1,0], [1,1]] #inputs to test the gates against

# and gate
print("\nand gate")
and_gate = Neuron(lambda x: sum(x) > 1, weights=[1, 1])
show_output(and_gate, gate_inputs)

#or_gate
print("\nor gate")
or_gate = Neuron(lambda x: sum(x) > 0, weights=[1, 1])
show_output(or_gate, gate_inputs)

# nand gate
print('\nnand')
nand_gate = Neuron(lambda x: sum(x) > -2, weights=[-1, -1])
show_output(nand_gate, gate_inputs)

# nor gate
print('\nnor')
nor_gate = Neuron(lambda x: sum(x) > -1, weights=[-1, -1])
show_output(nor_gate, gate_inputs)

# not
print('\nnot')
not_gate = Neuron(lambda x: sum(x) > -1, weights=[-1])
for g_inputs in [[0], [1]]:
    not_gate._inputs = numpy.array(g_inputs)
    print(f'x:{g_inputs} O:', not_gate.calc_out())


# xor
print('\nxor')
o1 = Neuron(signum,weights=[-2, 1],  bias=-1/2)
o2 = Neuron(signum,weights=[1, -1], bias=-1/2)
xor_gate = Neuron(signum, weights=[1, 1], bias=-1/2)

def sh_xor_output(gate_inputs_list):
    '''helper fuction to display xor output'''
    gate_inputs_array = numpy.array(gate_inputs_list)
    o1._inputs = o2._inputs = gate_inputs_array
    xor_gate._inputs = numpy.array([o1.calc_out(), o2.calc_out()])
    print(f'x1:{gate_inputs[0]} x2:{gate_inputs[1]} O:', xor_gate.calc_out())

for g_input in gate_inputs:
    sh_xor_output(g_input)
