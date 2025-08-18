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
        ('Concept Approve', 'Budget Align'),
        ('Budget Align', 'Design Review'),
        ('Design Review', 'Structure Simulate'),
        ('Structure Simulate', 'Material Procure'),
        ('Material Procure', 'Vendor Select'),
        ('Vendor Select', 'Permit Apply'),
        ('Permit Apply', 'Safety Check'),
        ('Safety Check', 'Site Prep'),
        ('Site Prep', 'Logistics Plan'),
        ('Logistics Plan', 'Fabricate Parts'),
        ('Fabricate Parts', 'Assemble Onsite'),
        ('Assemble Onsite', 'Quality Inspect'),
        ('Quality Inspect', 'Weather Monitor'),
        ('Weather Monitor', 'Public Unveil'),
        ('Public Unveil', 'Maintenance Plan'),
        ('Maintenance Plan', 'Stakeholder Meet')
    ]
)