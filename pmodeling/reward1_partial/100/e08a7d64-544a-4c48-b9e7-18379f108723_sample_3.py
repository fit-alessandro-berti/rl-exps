import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Material Testing'),
    Transition(label='Expert Review'),
    Transition(label='Legal Verify'),
    Transition(label='Risk Assess'),
    Transition(label='Insurance Quote'),
    Transition(label='Catalog Entry'),
    Transition(label='Digital Scan'),
    Transition(label='Condition Report'),
    Transition(label='Transport Plan'),
    Transition(label='Customs Clear'),
    Transition(label='Certification'),
    Transition(label='Exhibit Setup'),
    Transition(label='Owner Notify'),
    Transition(label='Final Audit')
])

# Define dependencies between activities
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

print(root)