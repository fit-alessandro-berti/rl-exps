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
    order={
        ('Initial Review', 'Provenance Check'): None,
        ('Provenance Check', 'Material Test'): None,
        ('Material Test', 'Expert Consult'): None,
        ('Expert Consult', 'Database Search'): None,
        ('Database Search', 'Condition Report'): None,
        ('Condition Report', 'Risk Assess'): None,
        ('Risk Assess', 'Market Analysis'): None,
        ('Market Analysis', 'Stakeholder Meet'): None,
        ('Stakeholder Meet', 'Legal Review'): None,
        ('Legal Review', 'Insurance Quote'): None,
        ('Insurance Quote', 'Price Negotiation'): None,
        ('Price Negotiation', 'Contract Draft'): None,
        ('Contract Draft', 'Final Approval'): None,
        ('Final Approval', 'Asset Registration'): None
    }
)