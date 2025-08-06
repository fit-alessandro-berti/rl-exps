root = StrictPartialOrder(nodes=[
    Transition(label='Asset ID'),
    Transition(label='Value Assess'),
    Transition(label='Risk Scan'),
    Transition(label='Market Review'),
    Transition(label='Initial Offer'),
    Transition(label='Counter Offer'),
    Transition(label='Negotiation'),
    Transition(label='Contract Draft'),
    Transition(label='Legal Review'),
    Transition(label='Digital Sign'),
    Transition(label='Royalty Setup'),
    Transition(label='Transfer Record'),
    Transition(label='Compliance Check'),
    Transition(label='Audit Schedule'),
    Transition(label='Market Feedback'),
    Transition(label='Strategy Update')
])

# Define operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Initial Offer'),
    Transition(label='Counter Offer')
])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Legal Review'),
    Transition(label='Digital Sign')
])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Royalty Setup'),
    Transition(label='Transfer Record')
])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Compliance Check'),
    Transition(label='Audit Schedule')
])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[
    Transition(label='Market Feedback'),
    Transition(label='Strategy Update')
])

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor1])

# Define the root process
root.order.add_edge(Transition(label='Asset ID'), Transition(label='Value Assess'))
root.order.add_edge(Transition(label='Value Assess'), Transition(label='Risk Scan'))
root.order.add_edge(Transition(label='Risk Scan'), Transition(label='Market Review'))
root.order.add_edge(Transition(label='Market Review'), loop1)
root.order.add_edge(Transition(label='Market Review'), loop2)
root.order.add_edge(Transition(label='Market Review'), loop3)
root.order.add_edge(loop1, Transition(label='Negotiation'))
root.order.add_edge(loop2, Transition(label='Negotiation'))
root.order.add_edge(loop3, Transition(label='Negotiation'))
root.order.add_edge(Transition(label='Negotiation'), Transition(label='Contract Draft'))
root.order.add_edge(Transition(label='Contract Draft'), loop1)
root.order.add_edge(Transition(label='Contract Draft'), loop2)
root.order.add_edge(Transition(label='Contract Draft'), loop3)
root.order.add_edge(Transition(label='Contract Draft'), xor2)
root.order.add_edge(Transition(label='Contract Draft'), xor3)
root.order.add_edge(Transition(label='Contract Draft'), xor4)
root.order.add_edge(Transition(label='Contract Draft'), xor5)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop3, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop3, xor1)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop3, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop2, xor5)
root.order.add_edge(loop3, xor5)
root.order.add_edge(Transition(label='Contract Draft'), Transition(label='Digital Sign'))
root.order.add_edge(Transition(label='Contract Draft'), Transition(label='Royalty Setup'))
root.order.add_edge(Transition(label='Contract Draft'), Transition(label='Transfer Record'))
root.order.add_edge(Transition(label='Contract Draft'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Contract Draft'), Transition(label='Audit Schedule'))
root.order.add_edge(Transition(label='Contract Draft'), Transition(label='Market Feedback'))
root.order.add_edge(Transition(label='Contract Draft'), Transition(label='Strategy Update'))
root.order.add_edge(Transition(label='Digital Sign'), Transition(label='Legal Review'))
root.order.add_edge(Transition(label='Digital Sign'), Transition(label='Royalty Setup'))
root.order.add_edge(Transition(label='Digital Sign'), Transition(label='Transfer Record'))
root.order.add_edge(Transition(label='Digital Sign'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Digital Sign'), Transition(label='Audit Schedule'))
root.order.add_edge(Transition(label='Digital Sign'), Transition(label='Market Feedback'))
root.order.add_edge(Transition(label='Digital Sign'), Transition(label='Strategy Update'))
root.order.add_edge(Transition(label='Royalty Setup'), Transition(label='Transfer Record'))
root.order.add_edge(Transition(label='Royalty Setup'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Royalty Setup'), Transition(label='Audit Schedule'))
root.order.add_edge(Transition(label='Royalty Setup'), Transition(label='Market Feedback'))
root.order.add_edge(Transition(label='Royalty Setup'), Transition(label='Strategy Update'))
root.order.add_edge(Transition(label='Transfer Record'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Transfer Record'), Transition(label='Audit Schedule'))
root.order.add_edge(Transition(label='Transfer Record'), Transition(label='Market Feedback'))
root.order.add_edge(Transition(label='Transfer Record'), Transition(label='Strategy Update'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Audit Schedule'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Market Feedback'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Strategy Update'))
root.order.add_edge(Transition(label='Audit Schedule'), Transition(label='Market Feedback'))
root.order.add_edge(Transition(label='Audit Schedule'), Transition(label='Strategy Update'))
root.order.add_edge(Transition(label='Market Feedback'), Transition(label='Strategy Update'))