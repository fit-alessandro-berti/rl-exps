from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
A1 = Transition(label='Client Onboard')
A2 = Transition(label='Needs Assess')
A3 = Transition(label='Drone Config')
A4 = Transition(label='Route Program')
A5 = Transition(label='Compliance Check')
A6 = Transition(label='Insurance Verify')
A7 = Transition(label='Lease Contract')
A8 = Transition(label='Fleet Deploy')
A9 = Transition(label='Monitor Setup')
A10 = Transition(label='Usage Track')
A11 = Transition(label='Maintenance Plan')
A12 = Transition(label='Incident Manage')
A13 = Transition(label='Billing Process')
A14 = Transition(label='Performance Report')
A15 = Transition(label='Contract Renew')
A16 = Transition(label='Price Adjust')
A17 = Transition(label='Feedback Collect')

# Define the partial order
root = StrictPartialOrder(nodes=[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17])

# Add the order constraints
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
root.order.add_edge(A15, A16)
root.order.add_edge(A16, A17)

# Return the root
return root