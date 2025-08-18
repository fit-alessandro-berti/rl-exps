import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
activities = {
    'Scenario Setup': Transition(label='Scenario Setup'),
    'Resource Mapping': Transition(label='Resource Mapping'),
    'Team Briefing': Transition(label='Team Briefing'),
    'Tech Deployment': Transition(label='Tech Deployment'),
    'Data Sync': Transition(label='Data Sync'),
    'Comm Setup': Transition(label='Comm Setup'),
    'Live Monitoring': Transition(label='Live Monitoring'),
    'Variable Adjust': Transition(label='Variable Adjust'),
    'Incident Injection': Transition(label='Incident Injection'),
    'Response Tracking': Transition(label='Response Tracking'),
    'Interlock Check': Transition(label='Interlock Check'),
    'Real-time Feedback': Transition(label='Real-time Feedback'),
    'Debrief Session': Transition(label='Debrief Session'),
    'Outcome Analysis': Transition(label='Outcome Analysis'),
    'Report Generation': Transition(label='Report Generation'),
    'Improvement Plan': Transition(label='Improvement Plan')
}

# Define the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the partial order edges
root.order.add_edge(activities['Scenario Setup'], activities['Resource Mapping'])
root.order.add_edge(activities['Resource Mapping'], activities['Team Briefing'])
root.order.add_edge(activities['Team Briefing'], activities['Tech Deployment'])
root.order.add_edge(activities['Tech Deployment'], activities['Data Sync'])
root.order.add_edge(activities['Data Sync'], activities['Comm Setup'])
root.order.add_edge(activities['Comm Setup'], activities['Live Monitoring'])
root.order.add_edge(activities['Live Monitoring'], activities['Variable Adjust'])
root.order.add_edge(activities['Variable Adjust'], activities['Incident Injection'])
root.order.add_edge(activities['Incident Injection'], activities['Response Tracking'])
root.order.add_edge(activities['Response Tracking'], activities['Interlock Check'])
root.order.add_edge(activities['Interlock Check'], activities['Real-time Feedback'])
root.order.add_edge(activities['Real-time Feedback'], activities['Debrief Session'])
root.order.add_edge(activities['Debrief Session'], activities['Outcome Analysis'])
root.order.add_edge(activities['Outcome Analysis'], activities['Report Generation'])
root.order.add_edge(activities['Report Generation'], activities['Improvement Plan'])

# Print the POWL model
print(root)