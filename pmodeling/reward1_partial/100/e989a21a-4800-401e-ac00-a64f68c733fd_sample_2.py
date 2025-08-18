import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
root = StrictPartialOrder(nodes=[
    Transition(label='Visual Inspect'),
    Transition(label='Document Gather'),
    Transition(label='Material Test'),
    Transition(label='Pigment Analyze'),
    Transition(label='Style Compare'),
    Transition(label='Provenance Trace'),
    Transition(label='Data Crosscheck'),
    Transition(label='Infrared Scan'),
    Transition(label='Xray Fluoresce'),
    Transition(label='Expert Consult'),
    Transition(label='Forgery Detect'),
    Transition(label='Report Draft'),
    Transition(label='Stakeholder Review'),
    Transition(label='Final Approval'),
    Transition(label='Archive Store')
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

# Print the root POWL model
print(root)