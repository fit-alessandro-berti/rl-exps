root = StrictPartialOrder(
    nodes=[
        Transition(label='Initial Assess'),
        Transition(label='Artifact Scan'),
        Transition(label='Condition Map'),
        Transition(label='Material Test'),
        Transition(label='Cleaning Phase'),
        Transition(label='Stability Check'),
        Transition(label='Minor Repair'),
        Transition(label='Structural Reinforce'),
        Transition(label='Surface Restore'),
        Transition(label='Coating Apply'),
        Transition(label='Ethics Review'),
        Transition(label='Provenance Verify'),
        Transition(label='Client Update'),
        Transition(label='Final Report'),
        Transition(label='Archive Store')
    ],
    order=[
        ('Initial Assess', 'Artifact Scan'),
        ('Artifact Scan', 'Condition Map'),
        ('Condition Map', 'Material Test'),
        ('Material Test', 'Cleaning Phase'),
        ('Cleaning Phase', 'Stability Check'),
        ('Stability Check', 'Minor Repair'),
        ('Minor Repair', 'Structural Reinforce'),
        ('Structural Reinforce', 'Surface Restore'),
        ('Surface Restore', 'Coating Apply'),
        ('Coating Apply', 'Ethics Review'),
        ('Ethics Review', 'Provenance Verify'),
        ('Provenance Verify', 'Client Update'),
        ('Client Update', 'Final Report'),
        ('Final Report', 'Archive Store')
    ]
)