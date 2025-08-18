root = StrictPartialOrder(
    nodes=[
        Transition(label='Load Assess'),
        Transition(label='Permit Review'),
        Transition(label='Site Survey'),
        Transition(label='Design Layout'),
        Transition(label='Soil Mix'),
        Transition(label='Install Beds'),
        Transition(label='Irrigation Set'),
        Transition(label='Climate Test'),
        Transition(label='Sensor Deploy'),
        Transition(label='Energy Setup'),
        Transition(label='Crop Select'),
        Transition(label='Plant Seeding'),
        Transition(label='Community Meet'),
        Transition(label='Compliance Check'),
        Transition(label='Growth Monitor'),
        Transition(label='Harvest Plan'),
        Transition(label='Waste Recycle')
    ],
    order={
        ('Load Assess', 'Permit Review'): None,
        ('Permit Review', 'Site Survey'): None,
        ('Site Survey', 'Design Layout'): None,
        ('Design Layout', 'Soil Mix'): None,
        ('Soil Mix', 'Install Beds'): None,
        ('Install Beds', 'Irrigation Set'): None,
        ('Irrigation Set', 'Climate Test'): None,
        ('Climate Test', 'Sensor Deploy'): None,
        ('Sensor Deploy', 'Energy Setup'): None,
        ('Energy Setup', 'Crop Select'): None,
        ('Crop Select', 'Plant Seeding'): None,
        ('Plant Seeding', 'Community Meet'): None,
        ('Community Meet', 'Compliance Check'): None,
        ('Compliance Check', 'Growth Monitor'): None,
        ('Growth Monitor', 'Harvest Plan'): None,
        ('Harvest Plan', 'Waste Recycle'): None
    }
)