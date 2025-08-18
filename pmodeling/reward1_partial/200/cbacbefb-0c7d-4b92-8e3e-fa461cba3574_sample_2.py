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
    order=[
        (Transition(label='Site Analysis'), Transition(label='Design Layout')),
        (Transition(label='Design Layout'), Transition(label='Module Assembly')),
        (Transition(label='Module Assembly'), Transition(label='Climate Setup')),
        (Transition(label='Climate Setup'), Transition(label='Sensor Install')),
        (Transition(label='Sensor Install'), Transition(label='Water Testing')),
        (Transition(label='Water Testing'), Transition(label='Nutrient Mix')),
        (Transition(label='Nutrient Mix'), Transition(label='Seed Selection')),
        (Transition(label='Seed Selection'), Transition(label='Planting Phase')),
        (Transition(label='Planting Phase'), Transition(label='Growth Monitor')),
        (Transition(label='Growth Monitor'), Transition(label='Pest Control')),
        (Transition(label='Pest Control'), Transition(label='Harvest Plan')),
        (Transition(label='Harvest Plan'), Transition(label='Yield Audit')),
        (Transition(label='Yield Audit'), Transition(label='Packaging Prep')),
        (Transition(label='Packaging Prep'), Transition(label='Market Delivery')),
        (Transition(label='Market Delivery'), Transition(label='Waste Recycling'))
    ]
)