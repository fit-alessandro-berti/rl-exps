import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

FarmSelect = Transition(label='Farm Select')
MilkTest = Transition(label='Milk Test')
MilkPasteurize = Transition(label='Milk Pasteurize')
CurdForm = Transition(label='Curd Form')
WheyDrain = Transition(label='Whey Drain')
CheesePress = Transition(label='Cheese Press')
SaltRub = Transition(label='Salt Rub')
AgingSet = Transition(label='Aging Set')
FlavorCheck = Transition(label='Flavor Check')
TextureScan = Transition(label='Texture Scan')
QualityApprove = Transition(label='Quality Approve')
CustomPack = Transition(label='Custom Pack')
ColdShip = Transition(label='Cold Ship')
RetailTrain = Transition(label='Retail Train')
FeedbackLog = Transition(label='Feedback Log')
BatchAdjust = Transition(label='Batch Adjust')

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[AgingSet, BatchAdjust])
xor = OperatorPOWL(operator=Operator.XOR, children=[TextureScan, FlavorCheck])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[CustomPack, RetailTrain])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[QualityApprove, FeedbackLog])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ColdShip, RetailTrain])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)

print(root)