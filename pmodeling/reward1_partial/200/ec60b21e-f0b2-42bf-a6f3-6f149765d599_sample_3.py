root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Modular Design'),
        Transition(label='System Build'),
        Transition(label='Env Control'),
        Transition(label='Seed Selection'),
        Transition(label='Nutrient Mix'),
        Transition(label='Planting Setup'),
        Transition(label='Growth Monitor'),
        Transition(label='Pest Control'),
        Transition(label='Water Cycle'),
        Transition(label='Data Capture'),
        Transition(label='Yield Forecast'),
        Transition(label='Waste Reuse'),
        Transition(label='Stakeholder Meet'),
        Transition(label='Compliance Check'),
        Transition(label='Supply Sync')
    ],
    order=[
        ('Site Survey', 'Modular Design'),
        ('Modular Design', 'System Build'),
        ('System Build', 'Env Control'),
        ('Env Control', 'Seed Selection'),
        ('Seed Selection', 'Nutrient Mix'),
        ('Nutrient Mix', 'Planting Setup'),
        ('Planting Setup', 'Growth Monitor'),
        ('Growth Monitor', 'Pest Control'),
        ('Pest Control', 'Water Cycle'),
        ('Water Cycle', 'Data Capture'),
        ('Data Capture', 'Yield Forecast'),
        ('Yield Forecast', 'Waste Reuse'),
        ('Waste Reuse', 'Stakeholder Meet'),
        ('Stakeholder Meet', 'Compliance Check'),
        ('Compliance Check', 'Supply Sync')
    ]
)