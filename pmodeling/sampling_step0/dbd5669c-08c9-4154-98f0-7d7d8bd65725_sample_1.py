root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Design Layout'),
        Transition(label='Material Sourcing'),
        Transition(label='Unit Assembly'),
        Transition(label='System Wiring'),
        Transition(label='Sensor Install'),
        Transition(label='Water Testing'),
        Transition(label='Nutrient Mix'),
        Transition(label='Seed Selection'),
        Transition(label='Planting Setup'),
        Transition(label='Climate Control'),
        Transition(label='Pest Management'),
        Transition(label='Data Calibration'),
        Transition(label='Yield Analysis'),
        Transition(label='Community Meet'),
        Transition(label='Compliance Check'),
        Transition(label='Expansion Plan')
    ],
    order={
        ('Site Survey', 'Design Layout'): None,
        ('Design Layout', 'Material Sourcing'): None,
        ('Material Sourcing', 'Unit Assembly'): None,
        ('Unit Assembly', 'System Wiring'): None,
        ('System Wiring', 'Sensor Install'): None,
        ('Sensor Install', 'Water Testing'): None,
        ('Water Testing', 'Nutrient Mix'): None,
        ('Nutrient Mix', 'Seed Selection'): None,
        ('Seed Selection', 'Planting Setup'): None,
        ('Planting Setup', 'Climate Control'): None,
        ('Climate Control', 'Pest Management'): None,
        ('Pest Management', 'Data Calibration'): None,
        ('Data Calibration', 'Yield Analysis'): None,
        ('Yield Analysis', 'Community Meet'): None,
        ('Community Meet', 'Compliance Check'): None,
        ('Compliance Check', 'Expansion Plan'): None
    }
)