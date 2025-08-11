import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Data Collection': Transition(label='Data Collection'),
    'Point Aggregation': Transition(label='Point Aggregation'),
    'Conflict Check': Transition(label='Conflict Check'),
    'Fraud Scan': Transition(label='Fraud Scan'),
    'Reward Adjust': Transition(label='Reward Adjust'),
    'Redemption Verify': Transition(label='Redemption Verify'),
    'Partner Sync': Transition(label='Partner Sync'),
    'Behavior Analyze': Transition(label='Behavior Analyze'),
    'Async Update': Transition(label='Async Update'),
    'Rollback Trigger': Transition(label='Rollback Trigger'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Notification Send': Transition(label='Notification Send'),
    'User Feedback': Transition(label='User Feedback'),
    'Report Generate': Transition(label='Report Generate'),
    'System Audit': Transition(label='System Audit')
}

# Create the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the order of activities
root.order.add_edge(activities['Data Collection'], activities['Point Aggregation'])
root.order.add_edge(activities['Point Aggregation'], activities['Conflict Check'])
root.order.add_edge(activities['Conflict Check'], activities['Fraud Scan'])
root.order.add_edge(activities['Fraud Scan'], activities['Reward Adjust'])
root.order.add_edge(activities['Reward Adjust'], activities['Redemption Verify'])
root.order.add_edge(activities['Redemption Verify'], activities['Partner Sync'])
root.order.add_edge(activities['Partner Sync'], activities['Behavior Analyze'])
root.order.add_edge(activities['Behavior Analyze'], activities['Async Update'])
root.order.add_edge(activities['Async Update'], activities['Rollback Trigger'])
root.order.add_edge(activities['Rollback Trigger'], activities['Compliance Check'])
root.order.add_edge(activities['Compliance Check'], activities['Notification Send'])
root.order.add_edge(activities['Notification Send'], activities['User Feedback'])
root.order.add_edge(activities['User Feedback'], activities['Report Generate'])
root.order.add_edge(activities['Report Generate'], activities['System Audit'])

# Print the POWL model
print(root)