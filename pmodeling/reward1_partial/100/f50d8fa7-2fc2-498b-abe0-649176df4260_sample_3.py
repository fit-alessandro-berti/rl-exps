import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Plan'),
    Transition(label='Permit Acquire'),
    Transition(label='Structural Retrofit'),
    Transition(label='System Install'),
    Transition(label='Lighting Setup'),
    Transition(label='Sensor Deploy'),
    Transition(label='Seed Sourcing'),
    Transition(label='Nutrient Prep'),
    Transition(label='Staff Training'),
    Transition(label='Data Monitor'),
    Transition(label='Yield Analyze'),
    Transition(label='Compliance Check'),
    Transition(label='Community Meet'),
    Transition(label='Market Launch'),
    Transition(label='Logistics Plan')
])

# Add dependencies to the model
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

# Print the POWL model
print(root)