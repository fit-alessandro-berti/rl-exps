import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
root = StrictPartialOrder(nodes=[
    Transition(label='Seed Select'),
    Transition(label='Germinate Seeds'),
    Transition(label='Transplant Seedlings'),
    Transition(label='Mix Nutrients'),
    Transition(label='Adjust pH'),
    Transition(label='Monitor Climate'),
    Transition(label='Control Humidity'),
    Transition(label='CO2 Regulation'),
    Transition(label='Detect Pests'),
    Transition(label='Deploy Biocontrols'),
    Transition(label='Schedule Harvest'),
    Transition(label='Automate Picking'),
    Transition(label='Package Produce'),
    Transition(label='Compost Waste'),
    Transition(label='Recycle Water'),
    Transition(label='Data Logging'),
    Transition(label='System Maintenance')
])

# Define the dependencies between the activities
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
root.order.add_edge(root.nodes[12], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])
root.order.add_edge(root.nodes[14], root.nodes[15])
root.order.add_edge(root.nodes[15], root.nodes[16])

print(root)