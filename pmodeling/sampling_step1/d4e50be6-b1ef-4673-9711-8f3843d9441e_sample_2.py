from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Patent Scouting'),
        Transition(label='Technical Review'),
        Transition(label='Legal Audit'),
        Transition(label='Market Analysis'),
        Transition(label='Valuation Modeling'),
        Transition(label='Risk Assessment'),
        Transition(label='License Targeting'),
        Transition(label='Buyer Outreach'),
        Transition(label='Negotiation Phase'),
        Transition(label='Contract Drafting'),
        Transition(label='Approval Process'),
        Transition(label='Portfolio Tracking'),
        Transition(label='Revenue Monitoring'),
        Transition(label='Compliance Check'),
        Transition(label='Innovation Scan'),
        Transition(label='Renewal Management')
    ],
    order=[]
)

# Add dependencies between nodes
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

# Print the root POWL model
print(root)