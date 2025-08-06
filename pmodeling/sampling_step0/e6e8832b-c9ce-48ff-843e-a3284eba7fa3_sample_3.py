import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
root = StrictPartialOrder(nodes=[
    Transition(label='Asset Listing'),
    Transition(label='Valuation Check'),
    Transition(label='Compliance Scan'),
    Transition(label='Legal Review'),
    Transition(label='Remote Audit'),
    Transition(label='Auction Setup'),
    Transition(label='Bid Monitoring'),
    Transition(label='Fraud Detection'),
    Transition(label='Ownership Transfer'),
    Transition(label='Payment Clearing'),
    Transition(label='Tax Calculation'),
    Transition(label='Fund Allocation'),
    Transition(label='Dispute Handling'),
    Transition(label='Report Generation'),
    Transition(label='Stakeholder Update')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[0], root.nodes[3])
root.order.add_edge(root.nodes[1], root.nodes[4])
root.order.add_edge(root.nodes[1], root.nodes[5])
root.order.add_edge(root.nodes[2], root.nodes[5])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[6])
root.order.add_edge(root.nodes[4], root.nodes[7])
root.order.add_edge(root.nodes[5], root.nodes[8])
root.order.add_edge(root.nodes[5], root.nodes[9])
root.order.add_edge(root.nodes[6], root.nodes[10])
root.order.add_edge(root.nodes[6], root.nodes[11])
root.order.add_edge(root.nodes[7], root.nodes[10])
root.order.add_edge(root.nodes[8], root.nodes[11])
root.order.add_edge(root.nodes[9], root.nodes[11])
root.order.add_edge(root.nodes[10], root.nodes[12])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[12])