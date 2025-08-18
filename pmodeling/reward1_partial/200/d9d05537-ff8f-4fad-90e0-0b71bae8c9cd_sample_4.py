root = StrictPartialOrder(
    nodes=[
        Transition(label='Alert Verify'),
        Transition(label='Impact Assess'),
        Transition(label='Team Assemble'),
        Transition(label='Resource Allocate'),
        Transition(label='Stakeholder Notify'),
        Transition(label='Legal Review'),
        Transition(label='Media Brief'),
        Transition(label='Response Deploy'),
        Transition(label='Situation Monitor'),
        Transition(label='Data Collect'),
        Transition(label='Risk Mitigate'),
        Transition(label='Recovery Plan'),
        Transition(label='External Consult'),
        Transition(label='Status Update'),
        Transition(label='Post Review')
    ],
    order=[
        (Transition(label='Alert Verify'), Transition(label='Impact Assess')),
        (Transition(label='Impact Assess'), Transition(label='Team Assemble')),
        (Transition(label='Team Assemble'), Transition(label='Resource Allocate')),
        (Transition(label='Resource Allocate'), Transition(label='Stakeholder Notify')),
        (Transition(label='Stakeholder Notify'), Transition(label='Legal Review')),
        (Transition(label='Legal Review'), Transition(label='Media Brief')),
        (Transition(label='Media Brief'), Transition(label='Response Deploy')),
        (Transition(label='Response Deploy'), Transition(label='Situation Monitor')),
        (Transition(label='Situation Monitor'), Transition(label='Data Collect')),
        (Transition(label='Data Collect'), Transition(label='Risk Mitigate')),
        (Transition(label='Risk Mitigate'), Transition(label='Recovery Plan')),
        (Transition(label='Recovery Plan'), Transition(label='External Consult')),
        (Transition(label='External Consult'), Transition(label='Status Update')),
        (Transition(label='Status Update'), Transition(label='Post Review'))
    ]
)