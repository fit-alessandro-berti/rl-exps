root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Structural Audit'),
        Transition(label='Modular Design'),
        Transition(label='Hydroponic Setup'),
        Transition(label='Climate Config'),
        Transition(label='Nutrient Mix'),
        Transition(label='Pest Detect'),
        Transition(label='Lighting Setup'),
        Transition(label='Energy Audit'),
        Transition(label='Automation Install'),
        Transition(label='Staff Training'),
        Transition(label='Market Analysis'),
        Transition(label='Regulation Check'),
        Transition(label='Yield Monitor'),
        Transition(label='Waste Manage'),
        Transition(label='Data Analytics')
    ],
    order=[
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Site Survey'),
            Transition(label='Structural Audit')
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Modular Design'),
            Transition(label='Hydroponic Setup')
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Climate Config'),
            Transition(label='Nutrient Mix')
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Pest Detect'),
            Transition(label='Lighting Setup')
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Energy Audit'),
            Transition(label='Automation Install')
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Staff Training'),
            Transition(label='Market Analysis')
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Regulation Check'),
            Transition(label='Yield Monitor')
        ]),
        OperatorPOWL(operator=Operator.XOR, children=[
            Transition(label='Waste Manage'),
            Transition(label='Data Analytics')
        ])
    ]
)