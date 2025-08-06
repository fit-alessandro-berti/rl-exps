import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Material Testing'),
    Transition(label='Stylistic Review'),
    Transition(label='Expert Panel'),
    Transition(label='Legal Clearance'),
    Transition(label='Ethics Audit'),
    Transition(label='Insurance Quote'),
    Transition(label='Risk Assess'),
    Transition(label='Digital Archive'),
    Transition(label='Replica Build'),
    Transition(label='Transport Prep'),
    Transition(label='Final Review'),
    Transition(label='Catalog Entry'),
    Transition(label='Public Notice'),
    Transition(label='Condition Report')
])
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