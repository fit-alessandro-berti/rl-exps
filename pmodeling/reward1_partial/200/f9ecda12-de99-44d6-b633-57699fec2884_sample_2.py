root = StrictPartialOrder(
    nodes=[
        Transition(label='Concept Approve'),
        Transition(label='Budget Align'),
        Transition(label='Design Review'),
        Transition(label='Structure Simulate'),
        Transition(label='Material Procure'),
        Transition(label='Vendor Select'),
        Transition(label='Permit Apply'),
        Transition(label='Safety Check'),
        Transition(label='Site Prep'),
        Transition(label='Logistics Plan'),
        Transition(label='Fabricate Parts'),
        Transition(label='Assemble Onsite'),
        Transition(label='Quality Inspect'),
        Transition(label='Weather Monitor'),
        Transition(label='Public Unveil'),
        Transition(label='Maintenance Plan'),
        Transition(label='Stakeholder Meet')
    ],
    order=[
        (Transition(label='Concept Approve'), Transition(label='Budget Align')),
        (Transition(label='Budget Align'), Transition(label='Design Review')),
        (Transition(label='Design Review'), Transition(label='Structure Simulate')),
        (Transition(label='Structure Simulate'), Transition(label='Material Procure')),
        (Transition(label='Material Procure'), Transition(label='Vendor Select')),
        (Transition(label='Vendor Select'), Transition(label='Permit Apply')),
        (Transition(label='Permit Apply'), Transition(label='Safety Check')),
        (Transition(label='Safety Check'), Transition(label='Site Prep')),
        (Transition(label='Site Prep'), Transition(label='Logistics Plan')),
        (Transition(label='Logistics Plan'), Transition(label='Fabricate Parts')),
        (Transition(label='Fabricate Parts'), Transition(label='Assemble Onsite')),
        (Transition(label='Assemble Onsite'), Transition(label='Quality Inspect')),
        (Transition(label='Quality Inspect'), Transition(label='Weather Monitor')),
        (Transition(label='Weather Monitor'), Transition(label='Public Unveil')),
        (Transition(label='Public Unveil'), Transition(label='Maintenance Plan')),
        (Transition(label='Maintenance Plan'), Transition(label='Stakeholder Meet'))
    ]
)