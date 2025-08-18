root = StrictPartialOrder(
    nodes=[
        Transition(label='Initial Review'),
        Transition(label='Provenance Check'),
        Transition(label='Material Test'),
        Transition(label='Expert Consult'),
        Transition(label='Database Search'),
        Transition(label='Condition Report'),
        Transition(label='Risk Assess'),
        Transition(label='Market Analysis'),
        Transition(label='Stakeholder Meet'),
        Transition(label='Legal Review'),
        Transition(label='Insurance Quote'),
        Transition(label='Price Negotiation'),
        Transition(label='Contract Draft'),
        Transition(label='Final Approval'),
        Transition(label='Asset Registration')
    ],
    order=[
        ('Initial Review', 'Provenance Check'),
        ('Provenance Check', 'Material Test'),
        ('Material Test', 'Expert Consult'),
        ('Expert Consult', 'Database Search'),
        ('Database Search', 'Condition Report'),
        ('Condition Report', 'Risk Assess'),
        ('Risk Assess', 'Market Analysis'),
        ('Market Analysis', 'Stakeholder Meet'),
        ('Stakeholder Meet', 'Legal Review'),
        ('Legal Review', 'Insurance Quote'),
        ('Insurance Quote', 'Price Negotiation'),
        ('Price Negotiation', 'Contract Draft'),
        ('Contract Draft', 'Final Approval'),
        ('Final Approval', 'Asset Registration')
    ]
)