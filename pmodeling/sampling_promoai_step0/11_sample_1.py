root = StrictPartialOrder(nodes=[
    Transition(label='Customer signs up'),
    Transition(label='Generate account'),
    Transition(label='Assign access'),
    Transition(label='Set automatic triggers for billing cycles'),
    Transition(label='Settle final account balance'),
    Transition(label='Send regular updates'),
    Transition(label='Send product enhancements'),
    Transition(label='Send renewal notifications'),
    Transition(label='Customer submits cancellation request'),
    Transition(label='Deactivate subscription'),
    Transition(label='apply charges'),
    Transition(label='apply refund'),
    OperatorPOWL(operator=Operator.LOOP, children=[
        Transition(label='Send product enhancements'),
        Transition(label='Send regular updates'),
        Transition(label='Send renewal notifications'),
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        Transition(label='Customer submits cancellation request'),
        OperatorPOWL(operator=Operator.LOOP, children=[
            Transition(label='apply charges'),
            Transition(label='apply refund'),
        ]),
    ]),
    OperatorPOWL(operator=Operator.LOOP, children=[
        Transition(label='Settle final account balance'),
    ]),
])