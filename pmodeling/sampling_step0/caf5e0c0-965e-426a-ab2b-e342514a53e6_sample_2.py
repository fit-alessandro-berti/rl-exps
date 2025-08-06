root = StrictPartialOrder(
    nodes=[
        Transition('Site Survey'),
        Transition('System Design'),
        Transition('Climate Sim'),
        Transition('Seed Select'),
        Transition('Module Setup'),
        Transition('Nutrient Mix'),
        Transition('Water Cycle'),
        Transition('Energy Link'),
        Transition('Sensor Install'),
        Transition('Pest Detect'),
        Transition('Growth Scan'),
        Transition('Data Sync'),
        Transition('Community Meet'),
        Transition('Reg Compliance'),
        Transition('System Test'),
        Transition('Maintenance Plan')
    ],
    order={
        ('Site Survey', 'System Design'): None,
        ('System Design', 'Climate Sim'): None,
        ('Climate Sim', 'Seed Select'): None,
        ('Seed Select', 'Module Setup'): None,
        ('Module Setup', 'Nutrient Mix'): None,
        ('Nutrient Mix', 'Water Cycle'): None,
        ('Water Cycle', 'Energy Link'): None,
        ('Energy Link', 'Sensor Install'): None,
        ('Sensor Install', 'Pest Detect'): None,
        ('Pest Detect', 'Growth Scan'): None,
        ('Growth Scan', 'Data Sync'): None,
        ('Data Sync', 'Community Meet'): None,
        ('Community Meet', 'Reg Compliance'): None,
        ('Reg Compliance', 'System Test'): None,
        ('System Test', 'Maintenance Plan'): None
    }
)