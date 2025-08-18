root = StrictPartialOrder(
    nodes=[
        Transition(label='Artifact Intake'),
        Transition(label='Provenance Check'),
        Transition(label='Archive Research'),
        Transition(label='Expert Interview'),
        Transition(label='Material Analysis'),
        Transition(label='Spectroscopy Test'),
        Transition(label='Carbon Dating'),
        Transition(label='Digital Imaging'),
        Transition(label='3D Modeling'),
        Transition(label='Data Review'),
        Transition(label='Consensus Meeting'),
        Transition(label='Conservation Plan'),
        Transition(label='Preservation Setup'),
        Transition(label='Documentation'),
        Transition(label='Exhibition Prep')
    ],
    order=[
        ('Artifact Intake', 'Provenance Check'),
        ('Provenance Check', 'Archive Research'),
        ('Provenance Check', 'Expert Interview'),
        ('Archive Research', 'Data Review'),
        ('Expert Interview', 'Data Review'),
        ('Material Analysis', 'Data Review'),
        ('Spectroscopy Test', 'Data Review'),
        ('Carbon Dating', 'Data Review'),
        ('Digital Imaging', 'Data Review'),
        ('3D Modeling', 'Data Review'),
        ('Data Review', 'Consensus Meeting'),
        ('Consensus Meeting', 'Conservation Plan'),
        ('Conservation Plan', 'Preservation Setup'),
        ('Preservation Setup', 'Documentation'),
        ('Documentation', 'Exhibition Prep')
    ]
)