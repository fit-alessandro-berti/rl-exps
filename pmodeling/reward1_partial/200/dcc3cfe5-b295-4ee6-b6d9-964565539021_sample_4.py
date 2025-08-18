root = StrictPartialOrder(
    nodes=[
        Transition(label='Demand Forecast'),
        Transition(label='Courier Match'),
        Transition(label='Credential Check'),
        Transition(label='Route Design'),
        Transition(label='Load Assign'),
        Transition(label='Traffic Scan'),
        Transition(label='Package Secure'),
        Transition(label='Dispatch Alert'),
        Transition(label='Real-time Track'),
        Transition(label='Incentive Issue'),
        Transition(label='Dispute Review'),
        Transition(label='Customer Notify'),
        Transition(label='Feedback Collect'),
        Transition(label='Performance Log'),
        Transition(label='Ledger Update'),
        Transition(label='Hub Sync')
    ],
    order=[
        ('Demand Forecast', 'Courier Match'),
        ('Courier Match', 'Credential Check'),
        ('Credential Check', 'Route Design'),
        ('Route Design', 'Load Assign'),
        ('Load Assign', 'Traffic Scan'),
        ('Traffic Scan', 'Package Secure'),
        ('Package Secure', 'Dispatch Alert'),
        ('Dispatch Alert', 'Real-time Track'),
        ('Real-time Track', 'Incentive Issue'),
        ('Incentive Issue', 'Dispute Review'),
        ('Dispute Review', 'Customer Notify'),
        ('Customer Notify', 'Feedback Collect'),
        ('Feedback Collect', 'Performance Log'),
        ('Performance Log', 'Ledger Update'),
        ('Ledger Update', 'Hub Sync')
    ]
)