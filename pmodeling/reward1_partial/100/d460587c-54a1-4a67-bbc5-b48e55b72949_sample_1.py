root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Permit Filing'),
        Transition(label='Load Testing'),
        Transition(label='Soil Sampling'),
        Transition(label='Water Testing'),
        Transition(label='System Design'),
        Transition(label='Solar Setup'),
        Transition(label='Crop Planning'),
        Transition(label='Stakeholder Meet'),
        Transition(label='Material Order'),
        Transition(label='System Install'),
        Transition(label='Environmental Audit'),
        Transition(label='Growth Monitoring'),
        Transition(label='Pest Control'),
        Transition(label='Market Launch')
    ],
    order=[
        ('Site Survey', 'Permit Filing'),
        ('Permit Filing', 'Load Testing'),
        ('Load Testing', 'Soil Sampling'),
        ('Soil Sampling', 'Water Testing'),
        ('Water Testing', 'System Design'),
        ('System Design', 'Solar Setup'),
        ('Solar Setup', 'Crop Planning'),
        ('Crop Planning', 'Stakeholder Meet'),
        ('Stakeholder Meet', 'Material Order'),
        ('Material Order', 'System Install'),
        ('System Install', 'Environmental Audit'),
        ('Environmental Audit', 'Growth Monitoring'),
        ('Growth Monitoring', 'Pest Control'),
        ('Pest Control', 'Market Launch')
    ]
)