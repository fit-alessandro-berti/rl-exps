import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = {
    'Demand Forecast': Transition(label='Demand Forecast'),
    'Courier Match': Transition(label='Courier Match'),
    'Credential Check': Transition(label='Credential Check'),
    'Route Design': Transition(label='Route Design'),
    'Load Assign': Transition(label='Load Assign'),
    'Traffic Scan': Transition(label='Traffic Scan'),
    'Package Secure': Transition(label='Package Secure'),
    'Dispatch Alert': Transition(label='Dispatch Alert'),
    'Real-time Track': Transition(label='Real-time Track'),
    'Incentive Issue': Transition(label='Incentive Issue'),
    'Dispute Review': Transition(label='Dispute Review'),
    'Customer Notify': Transition(label='Customer Notify'),
    'Feedback Collect': Transition(label='Feedback Collect'),
    'Performance Log': Transition(label='Performance Log'),
    'Ledger Update': Transition(label='Ledger Update'),
    'Hub Sync': Transition(label='Hub Sync')
}

# Define the POWL model
root = StrictPartialOrder(nodes=[
    activities['Demand Forecast'],
    activities['Courier Match'],
    activities['Credential Check'],
    activities['Route Design'],
    activities['Load Assign'],
    activities['Traffic Scan'],
    activities['Package Secure'],
    activities['Dispatch Alert'],
    activities['Real-time Track'],
    activities['Incentive Issue'],
    activities['Dispute Review'],
    activities['Customer Notify'],
    activities['Feedback Collect'],
    activities['Performance Log'],
    activities['Ledger Update'],
    activities['Hub Sync']
])

# Define the dependencies between the activities
root.order.add_edge(activities['Demand Forecast'], activities['Courier Match'])
root.order.add_edge(activities['Demand Forecast'], activities['Credential Check'])
root.order.add_edge(activities['Demand Forecast'], activities['Route Design'])
root.order.add_edge(activities['Demand Forecast'], activities['Load Assign'])
root.order.add_edge(activities['Demand Forecast'], activities['Traffic Scan'])
root.order.add_edge(activities['Demand Forecast'], activities['Package Secure'])
root.order.add_edge(activities['Demand Forecast'], activities['Dispatch Alert'])
root.order.add_edge(activities['Demand Forecast'], activities['Real-time Track'])
root.order.add_edge(activities['Demand Forecast'], activities['Incentive Issue'])
root.order.add_edge(activities['Demand Forecast'], activities['Dispute Review'])
root.order.add_edge(activities['Demand Forecast'], activities['Customer Notify'])
root.order.add_edge(activities['Demand Forecast'], activities['Feedback Collect'])
root.order.add_edge(activities['Demand Forecast'], activities['Performance Log'])
root.order.add_edge(activities['Demand Forecast'], activities['Ledger Update'])
root.order.add_edge(activities['Demand Forecast'], activities['Hub Sync'])

root.order.add_edge(activities['Courier Match'], activities['Credential Check'])
root.order.add_edge(activities['Courier Match'], activities['Route Design'])
root.order.add_edge(activities['Courier Match'], activities['Load Assign'])
root.order.add_edge(activities['Courier Match'], activities['Traffic Scan'])
root.order.add_edge(activities['Courier Match'], activities['Package Secure'])
root.order.add_edge(activities['Courier Match'], activities['Dispatch Alert'])
root.order.add_edge(activities['Courier Match'], activities['Real-time Track'])
root.order.add_edge(activities['Courier Match'], activities['Incentive Issue'])
root.order.add_edge(activities['Courier Match'], activities['Dispute Review'])
root.order.add_edge(activities['Courier Match'], activities['Customer Notify'])
root.order.add_edge(activities['Courier Match'], activities['Feedback Collect'])
root.order.add_edge(activities['Courier Match'], activities['Performance Log'])
root.order.add_edge(activities['Courier Match'], activities['Ledger Update'])
root.order.add_edge(activities['Courier Match'], activities['Hub Sync'])

root.order.add_edge(activities['Credential Check'], activities['Route Design'])
root.order.add_edge(activities['Credential Check'], activities['Load Assign'])
root.order.add_edge(activities['Credential Check'], activities['Traffic Scan'])
root.order.add_edge(activities['Credential Check'], activities['Package Secure'])
root.order.add_edge(activities['Credential Check'], activities['Dispatch Alert'])
root.order.add_edge(activities['Credential Check'], activities['Real-time Track'])
root.order.add_edge(activities['Credential Check'], activities['Incentive Issue'])
root.order.add_edge(activities['Credential Check'], activities['Dispute Review'])
root.order.add_edge(activities['Credential Check'], activities['Customer Notify'])
root.order.add_edge(activities['Credential Check'], activities['Feedback Collect'])
root.order.add_edge(activities['Credential Check'], activities['Performance Log'])
root.order.add_edge(activities['Credential Check'], activities['Ledger Update'])
root.order.add_edge(activities['Credential Check'], activities['Hub Sync'])

root.order.add_edge(activities['Route Design'], activities['Load Assign'])
root.order.add_edge(activities['Route Design'], activities['Traffic Scan'])
root.order.add_edge(activities['Route Design'], activities['Package Secure'])
root.order.add_edge(activities['Route Design'], activities['Dispatch Alert'])
root.order.add_edge(activities['Route Design'], activities['Real-time Track'])
root.order.add_edge(activities['Route Design'], activities['Incentive Issue'])
root.order.add_edge(activities['Route Design'], activities['Dispute Review'])
root.order.add_edge(activities['Route Design'], activities['Customer Notify'])
root.order.add_edge(activities['Route Design'], activities['Feedback Collect'])
root.order.add_edge(activities['Route Design'], activities['Performance Log'])
root.order.add_edge(activities['Route Design'], activities['Ledger Update'])
root.order.add_edge(activities['Route Design'], activities['Hub Sync'])

root.order.add_edge(activities['Load Assign'], activities['Traffic Scan'])
root.order.add_edge(activities['Load Assign'], activities['Package Secure'])
root.order.add_edge(activities['Load Assign'], activities['Dispatch Alert'])
root.order.add_edge(activities['Load Assign'], activities['Real-time Track'])
root.order.add_edge(activities['Load Assign'], activities['Incentive Issue'])
root.order.add_edge(activities['Load Assign'], activities['Dispute Review'])
root.order.add_edge(activities['Load Assign'], activities['Customer Notify'])
root.order.add_edge(activities['Load Assign'], activities['Feedback Collect'])
root.order.add_edge(activities['Load Assign'], activities['Performance Log'])
root.order.add_edge(activities['Load Assign'], activities['Ledger Update'])
root.order.add_edge(activities['Load Assign'], activities['Hub Sync'])

root.order.add_edge(activities['Traffic Scan'], activities['Package Secure'])
root.order.add_edge(activities['Traffic Scan'], activities['Dispatch Alert'])
root.order.add_edge(activities['Traffic Scan'], activities['Real-time Track'])
root.order.add_edge(activities['Traffic Scan'], activities['Incentive Issue'])
root.order.add_edge(activities['Traffic Scan'], activities['Dispute Review'])
root.order.add_edge(activities['Traffic Scan'], activities['Customer Notify'])
root.order.add_edge(activities['Traffic Scan'], activities['Feedback Collect'])
root.order.add_edge(activities['Traffic Scan'], activities['Performance Log'])
root.order.add_edge(activities['Traffic Scan'], activities['Ledger Update'])
root.order.add_edge(activities['Traffic Scan'], activities['Hub Sync'])

root.order.add_edge(activities['Package Secure'], activities['Dispatch Alert'])
root.order.add_edge(activities['Package Secure'], activities['Real-time Track'])
root.order.add_edge(activities['Package Secure'], activities['Incentive Issue'])
root.order.add_edge(activities['Package Secure'], activities['Dispute Review'])
root.order.add_edge(activities['Package Secure'], activities['Customer Notify'])
root.order.add_edge(activities['Package Secure'], activities['Feedback Collect'])
root.order.add_edge(activities['Package Secure'], activities['Performance Log'])
root.order.add_edge(activities['Package Secure'], activities['Ledger Update'])
root.order.add_edge(activities['Package Secure'], activities['Hub Sync'])

root.order.add_edge(activities['Dispatch Alert'], activities['Real-time Track'])
root.order.add_edge(activities['Dispatch Alert'], activities['Incentive Issue'])
root.order.add_edge(activities['Dispatch Alert'], activities['Dispute Review'])
root.order.add_edge(activities['Dispatch Alert'], activities['Customer Notify'])
root.order.add_edge(activities['Dispatch Alert'], activities['Feedback Collect'])
root.order.add_edge(activities['Dispatch Alert'], activities['Performance Log'])
root.order.add_edge(activities['Dispatch Alert'], activities['Ledger Update'])
root.order.add_edge(activities['Dispatch Alert'], activities['Hub Sync'])

root.order.add_edge(activities['Real-time Track'], activities['Incentive Issue'])
root.order.add_edge(activities['Real-time Track'], activities['Dispute Review'])
root.order.add_edge(activities['Real-time Track'], activities['Customer Notify'])
root.order.add_edge(activities['Real-time Track'], activities['Feedback Collect'])
root.order.add_edge(activities['Real-time Track'], activities['Performance Log'])
root.order.add_edge(activities['Real-time Track'], activities['Ledger Update'])
root.order.add_edge(activities['Real-time Track'], activities['Hub Sync'])

root.order.add_edge(activities['Incentive Issue'], activities['Dispute Review'])
root.order.add_edge(activities['Incentive Issue'], activities['Customer Notify'])
root.order.add_edge(activities['Incentive Issue'], activities['Feedback Collect'])
root.order.add_edge(activities['Incentive Issue'], activities['Performance Log'])
root.order.add_edge(activities['Incentive Issue'], activities['Ledger Update'])
root.order.add_edge(activities['Incentive Issue'], activities['Hub Sync'])

root.order.add_edge(activities['Dispute Review'], activities['Customer Notify'])
root.order.add_edge(activities['Dispute Review'], activities['Feedback Collect'])
root.order.add_edge(activities['Dispute Review'], activities['Performance Log'])
root.order.add_edge(activities['Dispute Review'], activities['Ledger Update'])
root.order.add_edge(activities['Dispute Review'], activities['Hub Sync'])

root.order.add_edge(activities['Customer Notify'], activities['Feedback Collect'])
root.order.add_edge(activities['Customer Notify'], activities['Performance Log'])
root.order.add_edge(activities['Customer Notify'], activities['Ledger Update'])
root.order.add_edge(activities['Customer Notify'], activities['Hub Sync'])

root.order.add_edge(activities['Feedback Collect'], activities['Performance Log'])
root.order.add_edge(activities['Feedback Collect'], activities['Ledger Update'])
root.order.add_edge(activities['Feedback Collect'], activities['Hub Sync'])

root.order.add_edge(activities['Performance Log'], activities['Ledger Update'])
root.order.add_edge(activities['Performance Log'], activities['Hub Sync'])

root.order.add_edge(activities['Ledger Update'], activities['Hub Sync'])

# Print the root POWL model
print(root)