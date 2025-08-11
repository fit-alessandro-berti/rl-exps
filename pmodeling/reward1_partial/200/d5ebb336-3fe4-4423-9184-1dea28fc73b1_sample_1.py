root = StrictPartialOrder(
    nodes=[
        Transition(label='Data Collection'),
        Transition(label='Point Aggregation'),
        Transition(label='Conflict Check'),
        Transition(label='Fraud Scan'),
        Transition(label='Reward Adjust'),
        Transition(label='Redemption Verify'),
        Transition(label='Partner Sync'),
        Transition(label='Behavior Analyze'),
        Transition(label='Async Update'),
        Transition(label='Rollback Trigger'),
        Transition(label='Compliance Check'),
        Transition(label='Notification Send'),
        Transition(label='User Feedback'),
        Transition(label='Report Generate'),
        Transition(label='System Audit')
    ],
    order=[
        (Transition(label='Data Collection'), Transition(label='Point Aggregation')),
        (Transition(label='Point Aggregation'), Transition(label='Conflict Check')),
        (Transition(label='Point Aggregation'), Transition(label='Fraud Scan')),
        (Transition(label='Conflict Check'), Transition(label='Reward Adjust')),
        (Transition(label='Fraud Scan'), Transition(label='Redemption Verify')),
        (Transition(label='Redemption Verify'), Transition(label='Partner Sync')),
        (Transition(label='Partner Sync'), Transition(label='Behavior Analyze')),
        (Transition(label='Behavior Analyze'), Transition(label='Async Update')),
        (Transition(label='Async Update'), Transition(label='Rollback Trigger')),
        (Transition(label='Rollback Trigger'), Transition(label='Compliance Check')),
        (Transition(label='Compliance Check'), Transition(label='Notification Send')),
        (Transition(label='Notification Send'), Transition(label='User Feedback')),
        (Transition(label='User Feedback'), Transition(label='Report Generate')),
        (Transition(label='Report Generate'), Transition(label='System Audit'))
    ]
)