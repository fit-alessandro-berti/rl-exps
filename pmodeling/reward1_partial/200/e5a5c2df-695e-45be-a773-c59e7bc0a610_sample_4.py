root = StrictPartialOrder(
    nodes=[
        Transition(label='Alert Trigger'),
        Transition(label='Initial Assess'),
        Transition(label='Stakeholder Notify'),
        Transition(label='Resource Check'),
        Transition(label='Risk Analyze'),
        Transition(label='Command Setup'),
        Transition(label='Deploy Teams'),
        Transition(label='Data Collect'),
        Transition(label='Situation Update'),
        Transition(label='Priority Adjust'),
        Transition(label='External Liaison'),
        Transition(label='Supply Dispatch'),
        Transition(label='Media Brief'),
        Transition(label='Impact Review'),
        Transition(label='Recovery Plan'),
        Transition(label='Process Audit')
    ],
    order=[
        (Transition(label='Alert Trigger'), Transition(label='Initial Assess')),
        (Transition(label='Initial Assess'), Transition(label='Stakeholder Notify')),
        (Transition(label='Initial Assess'), Transition(label='Resource Check')),
        (Transition(label='Initial Assess'), Transition(label='Risk Analyze')),
        (Transition(label='Initial Assess'), Transition(label='Command Setup')),
        (Transition(label='Initial Assess'), Transition(label='Deploy Teams')),
        (Transition(label='Initial Assess'), Transition(label='Data Collect')),
        (Transition(label='Initial Assess'), Transition(label='Situation Update')),
        (Transition(label='Initial Assess'), Transition(label='Priority Adjust')),
        (Transition(label='Initial Assess'), Transition(label='External Liaison')),
        (Transition(label='Initial Assess'), Transition(label='Supply Dispatch')),
        (Transition(label='Initial Assess'), Transition(label='Media Brief')),
        (Transition(label='Initial Assess'), Transition(label='Impact Review')),
        (Transition(label='Initial Assess'), Transition(label='Recovery Plan')),
        (Transition(label='Initial Assess'), Transition(label='Process Audit'))
    ]
)