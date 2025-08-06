import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Climate Scan': Transition(label='Climate Scan'),
    'Module Setup': Transition(label='Module Setup'),
    'Crop Choice': Transition(label='Crop Choice'),
    'Nutrient Feed': Transition(label='Nutrient Feed'),
    'Pest Control': Transition(label='Pest Control'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Waste Cycle': Transition(label='Waste Cycle'),
    'Growth Track': Transition(label='Growth Track'),
    'Demand Plan': Transition(label='Demand Plan'),
    'Community Link': Transition(label='Community Link'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Supply Sync': Transition(label='Supply Sync'),
    'System Upgrade': Transition(label='System Upgrade'),
    'Data Backup': Transition(label='Data Backup')
}

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[activities['Module Setup'], activities['Data Backup']])
loop = OperatorPOWL(operator=Operator.LOOP, children=[activities['Site Survey'], activities['Climate Scan']])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[activities['Crop Choice'], xor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[activities['Nutrient Feed'], activities['Pest Control']])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[activities['Energy Audit'], loop2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[activities['Waste Cycle'], xor3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[activities['Growth Track'], xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[activities['Demand Plan'], xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[activities['Community Link'], xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[activities['Regulation Check'], xor7])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[activities['Supply Sync'], xor8])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[activities['System Upgrade'], xor9])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10])
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)