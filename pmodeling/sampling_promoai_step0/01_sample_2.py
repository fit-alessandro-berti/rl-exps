import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
A = Transition(label='Receive customer inquiry')
B = Transition(label='Collect customer information')
C = Transition(label='Address customer concerns or questions')
D = Transition(label='Guide customer in selecting product/service')
E = Transition(label='Place order')
F = Transition(label='Provide quote')
G = Transition(label='Record order in system')
H = Transition(label='Send order confirmation to customer')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B, C, D])
xor = OperatorPOWL(operator=Operator.XOR, children=[F, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)