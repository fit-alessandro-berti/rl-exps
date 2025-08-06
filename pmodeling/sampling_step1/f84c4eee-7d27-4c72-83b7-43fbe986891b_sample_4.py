from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Component Sourcing'),
    Transition(label='Frame Assembly'),
    Transition(label='Sensor Mounting'),
    Transition(label='Wiring Harness'),
    Transition(label='Circuit Testing'),
    Transition(label='Firmware Loading'),
    Transition(label='Initial Calibration'),
    Transition(label='Software Integration'),
    Transition(label='Flight Testing'),
    Transition(label='Data Logging'),
    Transition(label='Performance Tuning'),
    Transition(label='Packaging Prep'),
    Transition(label='Custom Labeling'),
    Transition(label='Documentation Print'),
    Transition(label='Quality Review'),
    Transition(label='Client Training'),
    Transition(label='Remote Monitoring'),
    Transition(label='Firmware Update')
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
root.order.add_edge(root.nodes[13], root.nodes[14])
root.order.add_edge(root.nodes[14], root.nodes[15])
root.order.add_edge(root.nodes[15], root.nodes[16])
root.order.add_edge(root.nodes[16], root.nodes[17])
root.order.add_edge(root.nodes[17], root.nodes[18])