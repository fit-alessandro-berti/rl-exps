root = StrictPartialOrder(
    nodes=[
        Transition(label='Client Brief'),
        Transition(label='Concept Sketch'),
        Transition(label='Design Review'),
        Transition(label='Material Sourcing'),
        Transition(label='Prototype Build'),
        Transition(label='Vendor Coordination'),
        Transition(label='Quality Check'),
        Transition(label='Client Approval'),
        Transition(label='Packaging Prep'),
        Transition(label='Shipping Arrange'),
        Transition(label='Feedback Collect'),
        Transition(label='Portfolio Update'),
        Transition(label='Contract Sign'),
        Transition(label='IP Management'),
        Transition(label='Future Schedule'),
        Transition(label='Maintenance Plan')
    ],
    order=[
        ('Client Brief', 'Concept Sketch'),
        ('Concept Sketch', 'Design Review'),
        ('Design Review', 'Material Sourcing'),
        ('Material Sourcing', 'Prototype Build'),
        ('Prototype Build', 'Vendor Coordination'),
        ('Vendor Coordination', 'Quality Check'),
        ('Quality Check', 'Client Approval'),
        ('Client Approval', 'Packaging Prep'),
        ('Packaging Prep', 'Shipping Arrange'),
        ('Shipping Arrange', 'Feedback Collect'),
        ('Feedback Collect', 'Portfolio Update'),
        ('Portfolio Update', 'Contract Sign'),
        ('Contract Sign', 'IP Management'),
        ('IP Management', 'Future Schedule'),
        ('Future Schedule', 'Maintenance Plan')
    ]
)