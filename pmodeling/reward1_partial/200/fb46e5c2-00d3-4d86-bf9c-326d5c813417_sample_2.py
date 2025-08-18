root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Analysis'),
        Transition(label='Impact Review'),
        Transition(label='Modular Design'),
        Transition(label='System Integration'),
        Transition(label='Climate Setup'),
        Transition(label='Nutrient Mix'),
        Transition(label='Light Config'),
        Transition(label='Staff Training'),
        Transition(label='Pest Monitor'),
        Transition(label='Drone Deploy'),
        Transition(label='Health Scan'),
        Transition(label='Data Logging'),
        Transition(label='Supply Sync'),
        Transition(label='Maintenance Plan'),
        Transition(label='Waste Manage')
    ],
    order=[
        ('Site Analysis', 'Impact Review'),
        ('Impact Review', 'Modular Design'),
        ('Modular Design', 'System Integration'),
        ('System Integration', 'Climate Setup'),
        ('Climate Setup', 'Nutrient Mix'),
        ('Nutrient Mix', 'Light Config'),
        ('Light Config', 'Staff Training'),
        ('Staff Training', 'Pest Monitor'),
        ('Pest Monitor', 'Drone Deploy'),
        ('Drone Deploy', 'Health Scan'),
        ('Health Scan', 'Data Logging'),
        ('Data Logging', 'Supply Sync'),
        ('Supply Sync', 'Maintenance Plan'),
        ('Maintenance Plan', 'Waste Manage')
    ]
)