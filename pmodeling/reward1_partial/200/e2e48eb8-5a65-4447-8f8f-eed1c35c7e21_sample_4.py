root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Structural Check'),
        Transition(label='Climate Study'),
        Transition(label='Soil Prep'),
        Transition(label='Seed Selection'),
        Transition(label='Irrigation Setup'),
        Transition(label='Nutrient Mix'),
        Transition(label='Sensor Install'),
        Transition(label='Pest Monitor'),
        Transition(label='Data Analysis'),
        Transition(label='Regulation Review'),
        Transition(label='Community Meet'),
        Transition(label='Harvest Plan'),
        Transition(label='Packaging Design'),
        Transition(label='Distribution Map'),
        Transition(label='Feedback Loop'),
        Transition(label='Maintenance Schedule')
    ],
    order=[
        ('Site Survey', 'Structural Check'),
        ('Structural Check', 'Climate Study'),
        ('Climate Study', 'Soil Prep'),
        ('Soil Prep', 'Seed Selection'),
        ('Seed Selection', 'Irrigation Setup'),
        ('Irrigation Setup', 'Nutrient Mix'),
        ('Nutrient Mix', 'Sensor Install'),
        ('Sensor Install', 'Pest Monitor'),
        ('Pest Monitor', 'Data Analysis'),
        ('Data Analysis', 'Regulation Review'),
        ('Regulation Review', 'Community Meet'),
        ('Community Meet', 'Harvest Plan'),
        ('Harvest Plan', 'Packaging Design'),
        ('Packaging Design', 'Distribution Map'),
        ('Distribution Map', 'Feedback Loop'),
        ('Feedback Loop', 'Maintenance Schedule')
    ]
)