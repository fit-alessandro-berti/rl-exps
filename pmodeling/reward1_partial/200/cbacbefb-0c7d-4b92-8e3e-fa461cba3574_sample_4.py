root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Analysis'),
        Transition(label='Design Layout'),
        Transition(label='Module Assembly'),
        Transition(label='Climate Setup'),
        Transition(label='Sensor Install'),
        Transition(label='Water Testing'),
        Transition(label='Nutrient Mix'),
        Transition(label='Seed Selection'),
        Transition(label='Planting Phase'),
        Transition(label='Growth Monitor'),
        Transition(label='Pest Control'),
        Transition(label='Harvest Plan'),
        Transition(label='Yield Audit'),
        Transition(label='Packaging Prep'),
        Transition(label='Market Delivery'),
        Transition(label='Waste Recycling')
    ],
    order={
        ('Site Analysis', 'Design Layout'): None,
        ('Design Layout', 'Module Assembly'): None,
        ('Module Assembly', 'Climate Setup'): None,
        ('Climate Setup', 'Sensor Install'): None,
        ('Sensor Install', 'Water Testing'): None,
        ('Water Testing', 'Nutrient Mix'): None,
        ('Nutrient Mix', 'Seed Selection'): None,
        ('Seed Selection', 'Planting Phase'): None,
        ('Planting Phase', 'Growth Monitor'): None,
        ('Growth Monitor', 'Pest Control'): None,
        ('Pest Control', 'Harvest Plan'): None,
        ('Harvest Plan', 'Yield Audit'): None,
        ('Yield Audit', 'Packaging Prep'): None,
        ('Packaging Prep', 'Market Delivery'): None,
        ('Market Delivery', 'Waste Recycling'): None
    }
)