from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
A1 = Transition(label='Requirement Analysis')
A2 = Transition(label='Component Sourcing')
A3 = Transition(label='Quality Check')
A4 = Transition(label='Frame Assembly')
A5 = Transition(label='Motor Installation')
A6 = Transition(label='Sensor Setup')
A7 = Transition(label='Control Unit')
A8 = Transition(label='Firmware Upload')
A9 = Transition(label='System Calibration')
A10 = Transition(label='Flight Testing')
A11 = Transition(label='Error Correction')
A12 = Transition(label='Cosmetic Finish')
A13 = Transition(label='Packaging Prep')
A14 = Transition(label='User Manual')
A15 = Transition(label='Client Training')
A16 = Transition(label='Support Scheduling')

# Define the workflow model
root = StrictPartialOrder(nodes=[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16])

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
root.order.add_edge(A15, A16)

# Print the root
print(root)