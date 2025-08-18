root = StrictPartialOrder(
    nodes=[
        Transition(label='Colony Sourcing'),
        Transition(label='Hive Design'),
        Transition(label='Site Survey'),
        Transition(label='Installation Prep'),
        Transition(label='Hive Setup'),
        Transition(label='Sensor Install'),
        Transition(label='Health Monitor'),
        Transition(label='Pest Control'),
        Transition(label='Honey Harvest'),
        Transition(label='Wax Processing'),
        Transition(label='Product Packaging'),
        Transition(label='Order Dispatch'),
        Transition(label='Workshop Setup'),
        Transition(label='Community Outreach'),
        Transition(label='Regulation Check'),
        Transition(label='Data Analysis'),
        Transition(label='Maintenance Plan')
    ],
    order=[
        ('Colony Sourcing', 'Hive Design'),
        ('Hive Design', 'Site Survey'),
        ('Site Survey', 'Installation Prep'),
        ('Installation Prep', 'Hive Setup'),
        ('Hive Setup', 'Sensor Install'),
        ('Sensor Install', 'Health Monitor'),
        ('Health Monitor', 'Pest Control'),
        ('Pest Control', 'Honey Harvest'),
        ('Honey Harvest', 'Wax Processing'),
        ('Wax Processing', 'Product Packaging'),
        ('Product Packaging', 'Order Dispatch'),
        ('Order Dispatch', 'Workshop Setup'),
        ('Workshop Setup', 'Community Outreach'),
        ('Community Outreach', 'Regulation Check'),
        ('Regulation Check', 'Data Analysis'),
        ('Data Analysis', 'Maintenance Plan')
    ]
)