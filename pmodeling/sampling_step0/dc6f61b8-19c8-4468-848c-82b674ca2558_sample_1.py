from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Energy Partner'),
    Transition(label='Permit Filing'),
    Transition(label='Hydro Unit'),
    Transition(label='AI Setup'),
    Transition(label='Nutrient Plan'),
    Transition(label='System Install'),
    Transition(label='Crop Testing'),
    Transition(label='Data Analysis'),
    Transition(label='Community Meet'),
    Transition(label='Yield Adjust'),
    Transition(label='Carbon Audit'),
    Transition(label='Logistics Plan'),
    Transition(label='Quality Check'),
    Transition(label='Scale Review')
])

# Define the dependencies between activities
root.order.add_edge(root.nodes[0], root.nodes[1])  # Site Survey -> Energy Partner
root.order.add_edge(root.nodes[1], root.nodes[2])  # Energy Partner -> Permit Filing
root.order.add_edge(root.nodes[2], root.nodes[3])  # Permit Filing -> Hydro Unit
root.order.add_edge(root.nodes[3], root.nodes[4])  # Hydro Unit -> AI Setup
root.order.add_edge(root.nodes[4], root.nodes[5])  # AI Setup -> Nutrient Plan
root.order.add_edge(root.nodes[5], root.nodes[6])  # Nutrient Plan -> System Install
root.order.add_edge(root.nodes[6], root.nodes[7])  # System Install -> Crop Testing
root.order.add_edge(root.nodes[7], root.nodes[8])  # Crop Testing -> Data Analysis
root.order.add_edge(root.nodes[8], root.nodes[9])  # Data Analysis -> Community Meet
root.order.add_edge(root.nodes[9], root.nodes[10])  # Community Meet -> Yield Adjust
root.order.add_edge(root.nodes[10], root.nodes[11])  # Yield Adjust -> Carbon Audit
root.order.add_edge(root.nodes[11], root.nodes[12])  # Carbon Audit -> Logistics Plan
root.order.add_edge(root.nodes[12], root.nodes[13])  # Logistics Plan -> Quality Check
root.order.add_edge(root.nodes[13], root.nodes[14])  # Quality Check -> Scale Review

print(root)