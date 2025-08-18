root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Analysis'),
        Transition(label='Structure Check'),
        Transition(label='Modify Layout'),
        Transition(label='Install HVAC'),
        Transition(label='Setup Hydroponics'),
        Transition(label='Prepare Nutrients'),
        Transition(label='Select Seeds'),
        Transition(label='Automate Planting'),
        Transition(label='Deploy Sensors'),
        Transition(label='Pest Control'),
        Transition(label='Optimize Energy'),
        Transition(label='Recycle Water'),
        Transition(label='Automate Harvest'),
        Transition(label='Package Crops'),
        Transition(label='Coordinate Delivery'),
        Transition(label='Analyze Data')
    ],
    order=[
        ('Site Analysis', 'Structure Check'),
        ('Structure Check', 'Modify Layout'),
        ('Modify Layout', 'Install HVAC'),
        ('Install HVAC', 'Setup Hydroponics'),
        ('Setup Hydroponics', 'Prepare Nutrients'),
        ('Prepare Nutrients', 'Select Seeds'),
        ('Select Seeds', 'Automate Planting'),
        ('Automate Planting', 'Deploy Sensors'),
        ('Deploy Sensors', 'Pest Control'),
        ('Pest Control', 'Optimize Energy'),
        ('Optimize Energy', 'Recycle Water'),
        ('Recycle Water', 'Automate Harvest'),
        ('Automate Harvest', 'Package Crops'),
        ('Package Crops', 'Coordinate Delivery'),
        ('Coordinate Delivery', 'Analyze Data')
    ]
)