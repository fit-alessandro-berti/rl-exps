root = StrictPartialOrder(
    nodes=[
        Transition(label='Trend Scan'),
        Transition(label='Idea Harvest'),
        Transition(label='Workshop Host'),
        Transition(label='Concept Filter'),
        Transition(label='Prototype Build'),
        Transition(label='Expert Review'),
        Transition(label='Feasibility Check'),
        Transition(label='Risk Assess'),
        Transition(label='Pilot Launch'),
        Transition(label='Data Capture'),
        Transition(label='Performance Review'),
        Transition(label='Scale Plan'),
        Transition(label='Resource Align'),
        Transition(label='Learn Share'),
        Transition(label='Culture Embed')
    ],
    order=[
        ('Trend Scan', 'Idea Harvest'),
        ('Idea Harvest', 'Workshop Host'),
        ('Workshop Host', 'Concept Filter'),
        ('Concept Filter', 'Prototype Build'),
        ('Prototype Build', 'Expert Review'),
        ('Expert Review', 'Feasibility Check'),
        ('Feasibility Check', 'Risk Assess'),
        ('Risk Assess', 'Pilot Launch'),
        ('Pilot Launch', 'Data Capture'),
        ('Data Capture', 'Performance Review'),
        ('Performance Review', 'Scale Plan'),
        ('Scale Plan', 'Resource Align'),
        ('Resource Align', 'Learn Share'),
        ('Learn Share', 'Culture Embed')
    ]
)