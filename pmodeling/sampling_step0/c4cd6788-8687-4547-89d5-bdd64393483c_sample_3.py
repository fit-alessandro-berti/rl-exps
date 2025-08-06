root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Research'),
    Transition(label='Ownership Verify'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Legal Review'),
    Transition(label='Diplomatic Contact'),
    Transition(label='Condition Report'),
    Transition(label='Transport Plan'),
    Transition(label='Insurance Setup'),
    Transition(label='Customs Clear'),
    Transition(label='Secure Packaging'),
    Transition(label='Shipping Monitor'),
    Transition(label='Community Brief'),
    Transition(label='Arrival Inspect'),
    Transition(label='Exhibit Prepare'),
    Transition(label='Public Release')
])

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Artifact Research'),
    Transition(label='Ownership Verify')
])

xor2 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Stakeholder Meet'),
    Transition(label='Legal Review')
])

xor3 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Diplomatic Contact'),
    Transition(label='Condition Report')
])

xor4 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Transport Plan'),
    Transition(label='Insurance Setup')
])

xor5 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Customs Clear'),
    Transition(label='Secure Packaging')
])

xor6 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Shipping Monitor'),
    Transition(label='Community Brief')
])

xor7 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Arrival Inspect'),
    Transition(label='Exhibit Prepare')
])

xor8 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Public Release')
])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[
    xor1,
    xor2
])

loop2 = OperatorPOWL(operator=Operator.LOOP, children=[
    xor3,
    xor4
])

loop3 = OperatorPOWL(operator=Operator.LOOP, children=[
    xor5,
    xor6
])

loop4 = OperatorPOWL(operator=Operator.LOOP, children=[
    xor7,
    xor8
])

# Define the partial order
root.order.add_edge(loop1, xor3)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor5, xor7)
root.order.add_edge(xor7, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor4, xor6)
root.order.add_edge(xor6, xor8)
root.order.add_edge(xor8, xor1)