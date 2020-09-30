import Neuron #Neuron class written in prev practical
import numpy

# and gate
print("\nand gate")
and_gate = Neuron.Neuron(2, lambda x: sum(x) > 1, 0)
and_gate._weights = numpy.array([1, 1])

and_gate._inputs = numpy.array([0, 0])
print('x1:0 x2:0 O:', and_gate.calc_out())
and_gate._inputs = numpy.array([0, 1])
print('x1:0 x2:1 O:', and_gate.calc_out())
and_gate._inputs = numpy.array([1, 0])
print('x1:1 x2:0 O:', and_gate.calc_out())
and_gate._inputs = numpy.array([1, 1])
print('x1:1 x2:1 O:', and_gate.calc_out())
print()

#or_gate
print("\nor gate")
or_gate = Neuron.Neuron(2, lambda x: sum(x) > 0, 0)
or_gate._weights = numpy.array([1, 1])

or_gate._inputs = numpy.array([0, 0])
print('x1:0 x2:0 O:', or_gate.calc_out())
or_gate._inputs = numpy.array([0, 1])
print('x1:0 x2:1 O:', or_gate.calc_out())
or_gate._inputs = numpy.array([1, 0])
print('x1:1 x2:0 O:', or_gate.calc_out())
or_gate._inputs = numpy.array([1, 1])
print('x1:1 x2:1 O:', or_gate.calc_out())
print()

# nand gate
print('\nnand')
nand_gate = Neuron.Neuron(2, lambda x: sum(x) > -2, 0)
nand_gate._weights = numpy.array([-1, -1])

nand_gate._inputs = numpy.array([0, 0])
print('x1:0 x2:0 O:', nand_gate.calc_out())
nand_gate._inputs = numpy.array([0, 1])
print('x1:0 x2:1 O:', nand_gate.calc_out())
nand_gate._inputs = numpy.array([1, 0])
print('x1:1 x2:0 O:', nand_gate.calc_out())
nand_gate._inputs = numpy.array([1, 1])
print('x1:1 x2:1 O:', nand_gate.calc_out())
print()

# nor gate
print('\nnor')
nor_gate = Neuron.Neuron(2, lambda x: sum(x) > -1, 0)
nor_gate._weights = numpy.array([-1, -1])

nor_gate._inputs = numpy.array([0, 0])
print('x1:0 x2:0 O:', nor_gate.calc_out())
nor_gate._inputs = numpy.array([0, 1])
print('x1:0 x2:1 O:', nor_gate.calc_out())
nor_gate._inputs = numpy.array([1, 0])
print('x1:1 x2:0 O:', nor_gate.calc_out())
nor_gate._inputs = numpy.array([1, 1])
print('x1:1 x2:1 O:', nor_gate.calc_out())
print()

# not
not_gate = Neuron.Neuron(1, lambda x: x > -1, 0)
not_gate._weights = numpy.array([-1])

not_gate._inputs = numpy.array([0])
print('x: 0 O:', not_gate.calc_out())
not_gate._inputs = numpy.array([1])
print('x: 1 O:', not_gate.calc_out())

# xor
print('\nxor')
o1 = Neuron.Neuron(2, Neuron.signum, -1/2)
o1._weights = numpy.array([-2, 1])

o2 = Neuron.Neuron(2, Neuron.signum, -1/2)
o2._weights = numpy.array([1, -1])

xor_gate = Neuron.Neuron(2, Neuron.signum, -1/2)
xor_gate._weights = numpy.array([1, 1])

inputs = numpy.array([0, 0])
o1._inputs = o2._inputs = inputs
xor_gate._inputs = numpy.array([o1.calc_out(), o2.calc_out()])

print('x1:0 x2:0 O:', xor_gate.calc_out())
inputs = numpy.array([0, 1])
o1._inputs = o2._inputs = inputs
xor_gate._inputs = numpy.array([o1.calc_out(), o2.calc_out()])
print('x1:0 x2:1 O:', xor_gate.calc_out())
inputs = numpy.array([1, 0])
o1._inputs = o2._inputs = inputs
xor_gate._inputs = numpy.array([o1.calc_out(), o2.calc_out()])
print('x1:1 x2:0 O:', xor_gate.calc_out())
inputs = numpy.array([1, 1])
o1._inputs = o2._inputs = inputs
xor_gate._inputs = numpy.array([o1.calc_out(), o2.calc_out()])
print('x1:1 x2:1 O:', xor_gate.calc_out())
print()