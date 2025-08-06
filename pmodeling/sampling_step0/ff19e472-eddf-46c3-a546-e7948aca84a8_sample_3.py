from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'Install Modules': Transition(label='Install Modules'),
    'Calibrate Climate': Transition(label='Calibrate Climate'),
    'Prepare Nutrients': Transition(label='Prepare Nutrients'),
    'Select Seeds': Transition(label='Select Seeds'),
    'Start Germination': Transition(label='Start Germination'),
    'Deploy Sensors': Transition(label='Deploy Sensors'),
    'Monitor Growth': Transition(label='Monitor Growth'),
    'Manage Pests': Transition(label='Manage Pests'),
    'Schedule Harvest': Transition(label='Schedule Harvest'),
    'Process Waste': Transition(label='Process Waste'),
    'Optimize Energy': Transition(label='Optimize Energy'),
    'Conduct Training': Transition(label='Conduct Training'),
    'Update Records': Transition(label='Update Records'),
    'Review Performance': Transition(label='Review Performance')
}

# Define the transitions
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[activities['Site Survey'], activities['Design Layout']])
xor = OperatorPOWL(operator=Operator.XOR, children=[activities['Install Modules'], skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[activities['Calibrate Climate'], skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[activities['Prepare Nutrients'], skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[activities['Select Seeds'], skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[activities['Start Germination'], skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[activities['Deploy Sensors'], skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[activities['Monitor Growth'], skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[activities['Manage Pests'], skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[activities['Schedule Harvest'], skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[activities['Process Waste'], skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[activities['Optimize Energy'], skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[activities['Conduct Training'], skip])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[activities['Update Records'], skip])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[activities['Review Performance'], skip])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12, xor13, xor14])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor12, xor13)
root.order.add_edge(xor13, xor14)

# Print the root
print(root)