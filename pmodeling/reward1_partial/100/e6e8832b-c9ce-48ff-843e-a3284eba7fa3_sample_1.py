from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
A1 = Transition(label='Asset Listing')
A2 = Transition(label='Valuation Check')
A3 = Transition(label='Compliance Scan')
A4 = Transition(label='Legal Review')
A5 = Transition(label='Remote Audit')
A6 = Transition(label='Auction Setup')
A7 = Transition(label='Bid Monitoring')
A8 = Transition(label='Fraud Detection')
A9 = Transition(label='Ownership Transfer')
A10 = Transition(label='Payment Clearing')
A11 = Transition(label='Tax Calculation')
A12 = Transition(label='Fund Allocation')
A13 = Transition(label='Dispute Handling')
A14 = Transition(label='Report Generation')
A15 = Transition(label='Stakeholder Update')

# Define the partial order
root = StrictPartialOrder(nodes=[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15])

# Add dependencies
root.order.add_edge(A1, A2)
root.order.add_edge(A2, A3)
root.order.add_edge(A3, A4)
root.order.add_edge(A4, A5)
root.order.add_edge(A5, A6)
root.order.add_edge(A6, A7)
root.order.add_edge(A7, A8)
root.order.add_edge(A8, A9)
root.order.add_edge(A9, A10)
root.order.add_edge(A10, A11)
root.order.add_edge(A11, A12)
root.order.add_edge(A12, A13)
root.order.add_edge(A13, A14)
root.order.add_edge(A14, A15)

print(root)