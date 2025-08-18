root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Structural Check'),
        Transition(label='Modular Install'),
        Transition(label='Hydroponic Setup'),
        Transition(label='Nutrient Mix'),
        Transition(label='Sensor Setup'),
        Transition(label='AI Training'),
        Transition(label='Data Capture'),
        Transition(label='Maintenance Plan'),
        Transition(label='Pest Scan'),
        Transition(label='Growth Monitor'),
        Transition(label='Harvest Sync'),
        Transition(label='Quality Test'),
        Transition(label='Package Prep'),
        Transition(label='Logistics Plan')
    ],
    order={
        'Site Survey': 'Structural Check',
        'Structural Check': 'Modular Install',
        'Modular Install': 'Hydroponic Setup',
        'Hydroponic Setup': 'Nutrient Mix',
        'Nutrient Mix': 'Sensor Setup',
        'Sensor Setup': 'AI Training',
        'AI Training': 'Data Capture',
        'Data Capture': 'Maintenance Plan',
        'Maintenance Plan': 'Pest Scan',
        'Pest Scan': 'Growth Monitor',
        'Growth Monitor': 'Harvest Sync',
        'Harvest Sync': 'Quality Test',
        'Quality Test': 'Package Prep',
        'Package Prep': 'Logistics Plan'
    }
)