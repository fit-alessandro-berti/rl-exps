import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Document Review'),
    Transition(label='Material Testing'),
    Transition(label='Radiocarbon Date'),
    Transition(label='Stylistic Eval'),
    Transition(label='Database Check'),
    Transition(label='Ownership Audit'),
    Transition(label='Export Verify'),
    Transition(label='Expert Arbitration'),
    Transition(label='Conservation Plan'),
    Transition(label='Risk Assessment'),
    Transition(label='Approval Review'),
    Transition(label='Insurance Setup'),
    Transition(label='Secure Transport'),
    Transition(label='Acquisitions Meet'),
    Transition(label='Final Documentation')
])

# Define the dependencies between the activities
root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[0], root.nodes[3])
root.order.add_edge(root.nodes[0], root.nodes[4])
root.order.add_edge(root.nodes[0], root.nodes[5])
root.order.add_edge(root.nodes[0], root.nodes[6])
root.order.add_edge(root.nodes[1], root.nodes[7])
root.order.add_edge(root.nodes[2], root.nodes[7])
root.order.add_edge(root.nodes[3], root.nodes[7])
root.order.add_edge(root.nodes[4], root.nodes[7])
root.order.add_edge(root.nodes[5], root.nodes[7])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[7], root.nodes[9])
root.order.add_edge(root.nodes[7], root.nodes[10])
root.order.add_edge(root.nodes[7], root.nodes[11])
root.order.add_edge(root.nodes[8], root.nodes[12])
root.order.add_edge(root.nodes[8], root.nodes[13])
root.order.add_edge(root.nodes[8], root.nodes[14])
root.order.add_edge(root.nodes[12], root.nodes[15])
root.order.add_edge(root.nodes[13], root.nodes[15])
root.order.add_edge(root.nodes[14], root.nodes[15])
root.order.add_edge(root.nodes[15], root.nodes[16])