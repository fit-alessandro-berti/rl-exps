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
    order=[
        (Transition(label='Site Analysis'), Transition(label='Permit Securing')),
        (Transition(label='Permit Securing'), Transition(label='Unit Designing')),
        (Transition(label='Unit Designing'), Transition(label='LED Sourcing')),
        (Transition(label='LED Sourcing'), Transition(label='Hydroponic Setup')),
        (Transition(label='Hydroponic Setup'), Transition(label='Staff Hiring')),
        (Transition(label='Staff Hiring'), Transition(label='Pilot Cultivation')),
        (Transition(label='Pilot Cultivation'), Transition(label='Data Integration')),
        (Transition(label='Data Integration'), Transition(label='Waste Recycling')),
        (Transition(label='Waste Recycling'), Transition(label='Local Distribution')),
        (Transition(label='Local Distribution'), Transition(label='Subscription Setup')),
        (Transition(label='Subscription Setup'), Transition(label='IoT Deployment')),
        (Transition(label='IoT Deployment'), Transition(label='Sustainability Audit')),
        (Transition(label='Sustainability Audit'), Transition(label='Market Testing')),
        (Transition(label='Market Testing'), Transition(label='Process Refinement'))
    ]
)