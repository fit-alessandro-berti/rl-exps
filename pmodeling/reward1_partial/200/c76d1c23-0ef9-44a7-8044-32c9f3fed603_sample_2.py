root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Zoning Check'),
        Transition(label='Design Layout'),
        Transition(label='System Order'),
        Transition(label='Structure Build'),
        Transition(label='Install Hydroponics'),
        Transition(label='Calibrate Sensors'),
        Transition(label='Select Crops'),
        Transition(label='Plant Seeding'),
        Transition(label='Monitor Growth'),
        Transition(label='Manage Pests'),
        Transition(label='Schedule Harvest'),
        Transition(label='Package Produce'),
        Transition(label='Local Delivery'),
        Transition(label='Analyze Data')
    ],
    order=[
        ('Site Survey', 'Zoning Check'),
        ('Zoning Check', 'Design Layout'),
        ('Design Layout', 'System Order'),
        ('System Order', 'Structure Build'),
        ('Structure Build', 'Install Hydroponics'),
        ('Install Hydroponics', 'Calibrate Sensors'),
        ('Calibrate Sensors', 'Select Crops'),
        ('Select Crops', 'Plant Seeding'),
        ('Plant Seeding', 'Monitor Growth'),
        ('Monitor Growth', 'Manage Pests'),
        ('Manage Pests', 'Schedule Harvest'),
        ('Schedule Harvest', 'Package Produce'),
        ('Package Produce', 'Local Delivery'),
        ('Local Delivery', 'Analyze Data')
    ]
)