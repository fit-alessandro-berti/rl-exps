root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Design Layout'),
        Transition(label='Module Build'),
        Transition(label='System Install'),
        Transition(label='Water Prep'),
        Transition(label='Seed Selection'),
        Transition(label='Nutrient Mix'),
        Transition(label='Climate Setup'),
        Transition(label='Sensor Deploy'),
        Transition(label='Pest Scan'),
        Transition(label='Growth Monitor'),
        Transition(label='Data Sync'),
        Transition(label='Energy Manage'),
        Transition(label='Harvest Plan'),
        Transition(label='Community Link')
    ],
    order={
        ('Site Survey', 'Design Layout'): None,
        ('Design Layout', 'Module Build'): None,
        ('Module Build', 'System Install'): None,
        ('System Install', 'Water Prep'): None,
        ('Water Prep', 'Seed Selection'): None,
        ('Seed Selection', 'Nutrient Mix'): None,
        ('Nutrient Mix', 'Climate Setup'): None,
        ('Climate Setup', 'Sensor Deploy'): None,
        ('Sensor Deploy', 'Pest Scan'): None,
        ('Pest Scan', 'Growth Monitor'): None,
        ('Growth Monitor', 'Data Sync'): None,
        ('Data Sync', 'Energy Manage'): None,
        ('Energy Manage', 'Harvest Plan'): None,
        ('Harvest Plan', 'Community Link'): None
    }
)