root = StrictPartialOrder(nodes=[
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
])

root.order.add_edge(Transition(label='Data Collection'), Transition(label='Point Aggregation'))
root.order.add_edge(Transition(label='Point Aggregation'), Transition(label='Conflict Check'))
root.order.add_edge(Transition(label='Conflict Check'), Transition(label='Fraud Scan'))
root.order.add_edge(Transition(label='Fraud Scan'), Transition(label='Reward Adjust'))
root.order.add_edge(Transition(label='Reward Adjust'), Transition(label='Redemption Verify'))
root.order.add_edge(Transition(label='Redemption Verify'), Transition(label='Partner Sync'))
root.order.add_edge(Transition(label='Partner Sync'), Transition(label='Behavior Analyze'))
root.order.add_edge(Transition(label='Behavior Analyze'), Transition(label='Async Update'))
root.order.add_edge(Transition(label='Async Update'), Transition(label='Rollback Trigger'))
root.order.add_edge(Transition(label='Rollback Trigger'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Notification Send'))
root.order.add_edge(Transition(label='Notification Send'), Transition(label='User Feedback'))
root.order.add_edge(Transition(label='User Feedback'), Transition(label='Report Generate'))
root.order.add_edge(Transition(label='Report Generate'), Transition(label='System Audit'))