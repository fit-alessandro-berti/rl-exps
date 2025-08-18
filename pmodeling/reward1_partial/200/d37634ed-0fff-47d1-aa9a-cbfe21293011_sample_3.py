root = StrictPartialOrder(
    nodes=[
        Transition(label='Seed Selection'),
        Transition(label='Nutrient Mix'),
        Transition(label='Environment Check'),
        Transition(label='Planting Setup'),
        Transition(label='Growth Monitoring'),
        Transition(label='Pest Control'),
        Transition(label='Automated Harvest'),
        Transition(label='Quality Inspect'),
        Transition(label='Packaging Prep'),
        Transition(label='Order Fulfill'),
        Transition(label='Local Delivery'),
        Transition(label='Waste Collect'),
        Transition(label='Biomass Process'),
        Transition(label='Compost Create'),
        Transition(label='Energy Recover'),
        Transition(label='Regulation Review'),
        Transition(label='Community Engage')
    ],
    order=[
        ('Seed Selection', 'Nutrient Mix'),
        ('Nutrient Mix', 'Environment Check'),
        ('Environment Check', 'Planting Setup'),
        ('Planting Setup', 'Growth Monitoring'),
        ('Growth Monitoring', 'Pest Control'),
        ('Pest Control', 'Automated Harvest'),
        ('Automated Harvest', 'Quality Inspect'),
        ('Quality Inspect', 'Packaging Prep'),
        ('Packaging Prep', 'Order Fulfill'),
        ('Order Fulfill', 'Local Delivery'),
        ('Local Delivery', 'Waste Collect'),
        ('Waste Collect', 'Biomass Process'),
        ('Biomass Process', 'Compost Create'),
        ('Compost Create', 'Energy Recover'),
        ('Energy Recover', 'Regulation Review'),
        ('Regulation Review', 'Community Engage')
    ]
)