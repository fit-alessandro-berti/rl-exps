root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Structural Audit'),
    Transition(label='System Design'),
    Transition(label='Permit Filing'),
    Transition(label='Foundation Prep'),
    Transition(label='Frame Build'),
    Transition(label='Irrigation Setup'),
    Transition(label='Lighting Install'),
    Transition(label='Climate Control'),
    Transition(label='Nutrient Mix'),
    Transition(label='Crop Planting'),
    Transition(label='Pest Scouting'),
    Transition(label='Data Monitoring'),
    Transition(label='Waste Sorting'),
    Transition(label='Energy Audit'),
    Transition(label='Community Meet'),
    Transition(label='Yield Analysis')
])

xor = OperatorPOWL(operator=Operator.XOR, children=[
    OperatorPOWL(operator=Operator.XOR, children=[
        Transition(label='Site Survey'),
        Transition(label='Structural Audit'),
        Transition(label='System Design'),
        Transition(label='Permit Filing')
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        Transition(label='Foundation Prep'),
        Transition(label='Frame Build'),
        Transition(label='Irrigation Setup'),
        Transition(label='Lighting Install')
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        Transition(label='Climate Control'),
        Transition(label='Nutrient Mix'),
        Transition(label='Crop Planting'),
        Transition(label='Pest Scouting')
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        Transition(label='Data Monitoring'),
        Transition(label='Waste Sorting'),
        Transition(label='Energy Audit'),
        Transition(label='Community Meet')
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        Transition(label='Yield Analysis')
    ])
])

loop = OperatorPOWL(operator=Operator.LOOP, children=[xor])

root.order.add_edge(loop, xor)