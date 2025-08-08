from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Module Build'),
    Transition(label='System Install'),
    Transition(label='Water Prep'),
    Transition(label='Seed Selection'),
    Transition(label='Nutrient Mix'),
    Transition(label='Climate Setup'),
    Transition(label='Sensor Deploy'),
    Transition(label='Pest Scan'),
    Transition(label='Growth Monitor'),
    Transition(label='Data Sync'),
    Transition(label='Energy Manage'),
    Transition(label='Harvest Plan'),
    Transition(label='Community Link')
])

# Define the partial order dependencies
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