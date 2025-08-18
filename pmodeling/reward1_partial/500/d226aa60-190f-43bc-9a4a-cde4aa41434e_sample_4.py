import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Seed Select'),
    Transition(label='Trend Analyze'),
    Transition(label='Nutrient Mix'),
    Transition(label='Auto Plant'),
    Transition(label='Sensor Check'),
    Transition(label='Data Analyze'),
    Transition(label='Water Adjust'),
    Transition(label='Light Control'),
    Transition(label='Humidity Monitor'),
    Transition(label='Pest Inspect'),
    Transition(label='Growth Forecast'),
    Transition(label='Harvest Plan'),
    Transition(label='Rapid Cool'),
    Transition(label='Quality Grade'),
    Transition(label='Eco Package'),
    Transition(label='Logistics Prep'),
    Transition(label='Feedback Collect'),
    Transition(label='System Maintain')
])

# Define the dependencies between activities
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
root.order.add_edge(root.nodes[16], root.nodes[17])

# Print the final POWL model
print(root)