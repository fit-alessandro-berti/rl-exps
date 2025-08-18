root = StrictPartialOrder(
    nodes=[
        Transition(label='Trend Scan'),
        Transition(label='Idea Harvest'),
        Transition(label='Sector Match'),
        Transition(label='Brainstorm Hub'),
        Transition(label='Concept Filter'),
        Transition(label='Prototype Build'),
        Transition(label='Hybrid Testing'),
        Transition(label='Stakeholder Sync'),
        Transition(label='Risk Assess'),
        Transition(label='Scenario Map'),
        Transition(label='Strategy Align'),
        Transition(label='Pilot Launch'),
        Transition(label='Data Capture'),
        Transition(label='Market Sense'),
        Transition(label='Scale Plan')
    ],
    order=[
        ('Trend Scan', 'Idea Harvest'),
        ('Idea Harvest', 'Sector Match'),
        ('Sector Match', 'Brainstorm Hub'),
        ('Brainstorm Hub', 'Concept Filter'),
        ('Concept Filter', 'Prototype Build'),
        ('Prototype Build', 'Hybrid Testing'),
        ('Hybrid Testing', 'Stakeholder Sync'),
        ('Stakeholder Sync', 'Risk Assess'),
        ('Risk Assess', 'Scenario Map'),
        ('Scenario Map', 'Strategy Align'),
        ('Strategy Align', 'Pilot Launch'),
        ('Pilot Launch', 'Data Capture'),
        ('Data Capture', 'Market Sense'),
        ('Market Sense', 'Scale Plan')
    ]
)