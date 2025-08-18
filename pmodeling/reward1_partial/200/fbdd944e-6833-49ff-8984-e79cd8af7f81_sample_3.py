root = StrictPartialOrder(
    nodes=[
        Transition(label='Client Onboard'),
        Transition(label='Needs Assess'),
        Transition(label='Drone Config'),
        Transition(label='Route Program'),
        Transition(label='Compliance Check'),
        Transition(label='Insurance Verify'),
        Transition(label='Lease Contract'),
        Transition(label='Fleet Deploy'),
        Transition(label='Monitor Setup'),
        Transition(label='Usage Track'),
        Transition(label='Maintenance Plan'),
        Transition(label='Incident Manage'),
        Transition(label='Billing Process'),
        Transition(label='Performance Report'),
        Transition(label='Contract Renew'),
        Transition(label='Price Adjust'),
        Transition(label='Feedback Collect')
    ],
    order=[
        ('Client Onboard', 'Needs Assess'),
        ('Needs Assess', 'Drone Config'),
        ('Drone Config', 'Route Program'),
        ('Route Program', 'Compliance Check'),
        ('Compliance Check', 'Insurance Verify'),
        ('Insurance Verify', 'Lease Contract'),
        ('Lease Contract', 'Fleet Deploy'),
        ('Fleet Deploy', 'Monitor Setup'),
        ('Monitor Setup', 'Usage Track'),
        ('Usage Track', 'Maintenance Plan'),
        ('Maintenance Plan', 'Incident Manage'),
        ('Incident Manage', 'Billing Process'),
        ('Billing Process', 'Performance Report'),
        ('Performance Report', 'Contract Renew'),
        ('Contract Renew', 'Price Adjust'),
        ('Price Adjust', 'Feedback Collect')
    ]
)