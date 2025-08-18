root = StrictPartialOrder(
    nodes=[
        Transition(label='Artifact Intake'),
        Transition(label='Provenance Check'),
        Transition(label='Archive Search'),
        Transition(label='Expert Consult'),
        Transition(label='Material Scan'),
        Transition(label='3D Imaging'),
        Transition(label='Stylistic Match'),
        Transition(label='Database Query'),
        Transition(label='Panel Review'),
        Transition(label='Certify Report'),
        Transition(label='Condition Assess'),
        Transition(label='Storage Plan'),
        Transition(label='Catalog Entry'),
        Transition(label='Display Prep'),
        Transition(label='Loan Arrange'),
        Transition(label='Monitor Setup')
    ],
    order=[
        ('Artifact Intake', 'Provenance Check'),
        ('Artifact Intake', 'Archive Search'),
        ('Archive Search', 'Expert Consult'),
        ('Archive Search', 'Material Scan'),
        ('Material Scan', '3D Imaging'),
        ('3D Imaging', 'Stylistic Match'),
        ('Stylistic Match', 'Database Query'),
        ('Database Query', 'Panel Review'),
        ('Panel Review', 'Certify Report'),
        ('Certify Report', 'Condition Assess'),
        ('Condition Assess', 'Storage Plan'),
        ('Storage Plan', 'Catalog Entry'),
        ('Catalog Entry', 'Display Prep'),
        ('Display Prep', 'Loan Arrange'),
        ('Loan Arrange', 'Monitor Setup')
    ]
)