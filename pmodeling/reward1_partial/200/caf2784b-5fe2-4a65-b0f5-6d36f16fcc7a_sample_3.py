root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Audit'),
        Transition(label='Impact Study'),
        Transition(label='Design Modules'),
        Transition(label='Sensor Setup'),
        Transition(label='Hydroponics Install'),
        Transition(label='Nutrient Test'),
        Transition(label='Lighting Config'),
        Transition(label='Staff Training'),
        Transition(label='Data Collection'),
        Transition(label='Yield Analysis'),
        Transition(label='Pest Control'),
        Transition(label='Harvest Plan'),
        Transition(label='Packaging Prep'),
        Transition(label='Market Delivery'),
        Transition(label='Feedback Loop')
    ],
    order={
        'Site Audit': 'Impact Study',
        'Impact Study': 'Design Modules',
        'Design Modules': 'Sensor Setup',
        'Sensor Setup': 'Hydroponics Install',
        'Hydroponics Install': 'Nutrient Test',
        'Nutrient Test': 'Lighting Config',
        'Lighting Config': 'Staff Training',
        'Staff Training': 'Data Collection',
        'Data Collection': 'Yield Analysis',
        'Yield Analysis': 'Pest Control',
        'Pest Control': 'Harvest Plan',
        'Harvest Plan': 'Packaging Prep',
        'Packaging Prep': 'Market Delivery',
        'Market Delivery': 'Feedback Loop'
    }
)