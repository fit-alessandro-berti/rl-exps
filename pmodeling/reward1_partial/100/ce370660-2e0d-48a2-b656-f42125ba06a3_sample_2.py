root = StrictPartialOrder(
    nodes=[
        Transition(label='Structural Check'),
        Transition(label='Permit Apply'),
        Transition(label='Design Layout'),
        Transition(label='Soil Prep'),
        Transition(label='Bed Install'),
        Transition(label='Irrigation Setup'),
        Transition(label='Sensor Mount'),
        Transition(label='Solar Connect'),
        Transition(label='Seed Order'),
        Transition(label='Nutrient Mix'),
        Transition(label='Community Meet'),
        Transition(label='Staff Train'),
        Transition(label='Plant Crop'),
        Transition(label='Maintenance Plan'),
        Transition(label='Harvest Schedule'),
        Transition(label='Waste Manage')
    ],
    order=[
        ('Structural Check', 'Permit Apply'),
        ('Permit Apply', 'Design Layout'),
        ('Design Layout', 'Soil Prep'),
        ('Soil Prep', 'Bed Install'),
        ('Bed Install', 'Irrigation Setup'),
        ('Irrigation Setup', 'Sensor Mount'),
        ('Sensor Mount', 'Solar Connect'),
        ('Solar Connect', 'Seed Order'),
        ('Seed Order', 'Nutrient Mix'),
        ('Nutrient Mix', 'Community Meet'),
        ('Community Meet', 'Staff Train'),
        ('Staff Train', 'Plant Crop'),
        ('Plant Crop', 'Maintenance Plan'),
        ('Maintenance Plan', 'Harvest Schedule'),
        ('Harvest Schedule', 'Waste Manage')
    ]
)