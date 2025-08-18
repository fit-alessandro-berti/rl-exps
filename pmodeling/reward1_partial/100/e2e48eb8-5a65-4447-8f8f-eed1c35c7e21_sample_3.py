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
    order={
        ('Site Survey', 'Structural Check'): None,
        ('Structural Check', 'Climate Study'): None,
        ('Climate Study', 'Soil Prep'): None,
        ('Soil Prep', 'Seed Selection'): None,
        ('Seed Selection', 'Irrigation Setup'): None,
        ('Irrigation Setup', 'Nutrient Mix'): None,
        ('Nutrient Mix', 'Sensor Install'): None,
        ('Sensor Install', 'Pest Monitor'): None,
        ('Pest Monitor', 'Data Analysis'): None,
        ('Data Analysis', 'Regulation Review'): None,
        ('Regulation Review', 'Community Meet'): None,
        ('Community Meet', 'Harvest Plan'): None,
        ('Harvest Plan', 'Packaging Design'): None,
        ('Packaging Design', 'Distribution Map'): None,
        ('Distribution Map', 'Feedback Loop'): None,
        ('Feedback Loop', 'Maintenance Schedule'): None
    }
)