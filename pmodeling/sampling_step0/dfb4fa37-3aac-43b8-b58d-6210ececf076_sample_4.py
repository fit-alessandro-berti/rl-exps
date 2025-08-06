root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Analysis'),
        Transition(label='Permit Securing'),
        Transition(label='Unit Designing'),
        Transition(label='LED Sourcing'),
        Transition(label='Hydroponic Setup'),
        Transition(label='Staff Hiring'),
        Transition(label='Pilot Cultivation'),
        Transition(label='Data Integration'),
        Transition(label='Waste Recycling'),
        Transition(label='Local Distribution'),
        Transition(label='Subscription Setup'),
        Transition(label='IoT Deployment'),
        Transition(label='Sustainability Audit'),
        Transition(label='Market Testing'),
        Transition(label='Process Refinement')
    ],
    order={
        'Site Analysis': 'Permit Securing',
        'Permit Securing': 'Unit Designing',
        'Unit Designing': 'LED Sourcing',
        'LED Sourcing': 'Hydroponic Setup',
        'Hydroponic Setup': 'Staff Hiring',
        'Staff Hiring': 'Pilot Cultivation',
        'Pilot Cultivation': 'Data Integration',
        'Data Integration': 'Waste Recycling',
        'Waste Recycling': 'Local Distribution',
        'Local Distribution': 'Subscription Setup',
        'Subscription Setup': 'IoT Deployment',
        'IoT Deployment': 'Sustainability Audit',
        'Sustainability Audit': 'Market Testing',
        'Market Testing': 'Process Refinement'
    }
)