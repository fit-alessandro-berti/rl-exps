root = StrictPartialOrder(
    nodes=[
        Transition(label='Client Intake'),
        Transition(label='Needs Analysis'),
        Transition(label='Developer Match'),
        Transition(label='Expert Vetting'),
        Transition(label='Prototype Build'),
        Transition(label='Feedback Loop'),
        Transition(label='Model Refinement'),
        Transition(label='License Draft'),
        Transition(label='IP Negotiation'),
        Transition(label='Contract Sign'),
        Transition(label='Deployment Prep'),
        Transition(label='Go Live'),
        Transition(label='Monitor Model'),
        Transition(label='Optimize AI'),
        Transition(label='Support Handoff'),
        Transition(label='Compliance Check'),
        Transition(label='Final Review')
    ],
    order=[
        ('Client Intake', 'Needs Analysis'),
        ('Needs Analysis', 'Developer Match'),
        ('Developer Match', 'Expert Vetting'),
        ('Expert Vetting', 'Prototype Build'),
        ('Prototype Build', 'Feedback Loop'),
        ('Feedback Loop', 'Model Refinement'),
        ('Model Refinement', 'License Draft'),
        ('License Draft', 'IP Negotiation'),
        ('IP Negotiation', 'Contract Sign'),
        ('Contract Sign', 'Deployment Prep'),
        ('Deployment Prep', 'Go Live'),
        ('Go Live', 'Monitor Model'),
        ('Monitor Model', 'Optimize AI'),
        ('Optimize AI', 'Support Handoff'),
        ('Support Handoff', 'Compliance Check'),
        ('Compliance Check', 'Final Review')
    ]
)