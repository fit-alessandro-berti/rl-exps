from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
A1 = Transition(label='Site Survey')
A2 = Transition(label='Structural Audit')
A3 = Transition(label='Layout Design')
A4 = Transition(label='System Install')
A5 = Transition(label='Climate Setup')
A6 = Transition(label='Water Testing')
A7 = Transition(label='Nutrient Mix')
A8 = Transition(label='Seed Selection')
A9 = Transition(label='Planting Prep')
A10 = Transition(label='Growth Monitor')
A11 = Transition(label='Pest Inspect')
A12 = Transition(label='Harvest Plan')
A13 = Transition(label='Packaging Prep')
A14 = Transition(label='Distribution')
A15 = Transition(label='Sustainability')

# Define the partial order
root = StrictPartialOrder(nodes=[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15])

# Define the dependencies
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

# Print the root variable
print(root)