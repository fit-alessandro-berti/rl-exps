root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Assess'),
        Transition(label='Structure Check'),
        Transition(label='Soil Test'),
        Transition(label='Climate Eval'),
        Transition(label='Permit Obtain'),
        Transition(label='Design Layout'),
        Transition(label='Seed Sourcing'),
        Transition(label='Irrigation Set'),
        Transition(label='Nutrient Mix'),
        Transition(label='Pest Control'),
        Transition(label='Sensor Install'),
        Transition(label='Staff Train'),
        Transition(label='Crop Planting'),
        Transition(label='Yield Monitor'),
        Transition(label='Market Setup'),
        Transition(label='Maintenance'),
        Transition(label='Waste Manage')
    ],
    order=[
        ('Site Assess', 'Structure Check'),
        ('Structure Check', 'Soil Test'),
        ('Soil Test', 'Climate Eval'),
        ('Climate Eval', 'Permit Obtain'),
        ('Permit Obtain', 'Design Layout'),
        ('Design Layout', 'Seed Sourcing'),
        ('Seed Sourcing', 'Irrigation Set'),
        ('Irrigation Set', 'Nutrient Mix'),
        ('Nutrient Mix', 'Pest Control'),
        ('Pest Control', 'Sensor Install'),
        ('Sensor Install', 'Staff Train'),
        ('Staff Train', 'Crop Planting'),
        ('Crop Planting', 'Yield Monitor'),
        ('Yield Monitor', 'Market Setup'),
        ('Market Setup', 'Maintenance'),
        ('Maintenance', 'Waste Manage')
    ]
)