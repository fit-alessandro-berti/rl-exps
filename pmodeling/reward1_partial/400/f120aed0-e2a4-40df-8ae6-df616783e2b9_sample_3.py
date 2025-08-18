import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Rack Design'),
    Transition(label='System Setup'),
    Transition(label='Climate Calibrate'),
    Transition(label='Nutrient Prep'),
    Transition(label='Crop Select'),
    Transition(label='Seed Germinate'),
    Transition(label='Sensor Deploy'),
    Transition(label='Pest Control'),
    Transition(label='Harvest Automate'),
    Transition(label='Quality Check'),
    Transition(label='Pack Produce'),
    Transition(label='Data Analyze'),
    Transition(label='Engage Community'),
    Transition(label='Logistics Plan')
])

# Define the partial order of execution
root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[5], root.nodes[6])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])

print(root)