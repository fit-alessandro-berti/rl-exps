import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Scenario Setup'),
    Transition(label='Resource Mapping'),
    Transition(label='Team Briefing'),
    Transition(label='Tech Deployment'),
    Transition(label='Data Sync'),
    Transition(label='Comm Setup'),
    Transition(label='Live Monitoring'),
    Transition(label='Variable Adjust'),
    Transition(label='Incident Injection'),
    Transition(label='Response Tracking'),
    Transition(label='Interlock Check'),
    Transition(label='Real-time Feedback'),
    Transition(label='Debrief Session'),
    Transition(label='Outcome Analysis'),
    Transition(label='Report Generation'),
    Transition(label='Improvement Plan')
])

# Add dependencies between activities
root.order.add_edge(Transition(label='Scenario Setup'), Transition(label='Resource Mapping'))
root.order.add_edge(Transition(label='Resource Mapping'), Transition(label='Team Briefing'))
root.order.add_edge(Transition(label='Team Briefing'), Transition(label='Tech Deployment'))
root.order.add_edge(Transition(label='Tech Deployment'), Transition(label='Data Sync'))
root.order.add_edge(Transition(label='Data Sync'), Transition(label='Comm Setup'))
root.order.add_edge(Transition(label='Comm Setup'), Transition(label='Live Monitoring'))
root.order.add_edge(Transition(label='Live Monitoring'), Transition(label='Variable Adjust'))
root.order.add_edge(Transition(label='Variable Adjust'), Transition(label='Incident Injection'))
root.order.add_edge(Transition(label='Incident Injection'), Transition(label='Response Tracking'))
root.order.add_edge(Transition(label='Response Tracking'), Transition(label='Interlock Check'))
root.order.add_edge(Transition(label='Interlock Check'), Transition(label='Real-time Feedback'))
root.order.add_edge(Transition(label='Real-time Feedback'), Transition(label='Debrief Session'))
root.order.add_edge(Transition(label='Debrief Session'), Transition(label='Outcome Analysis'))
root.order.add_edge(Transition(label='Outcome Analysis'), Transition(label='Report Generation'))
root.order.add_edge(Transition(label='Report Generation'), Transition(label='Improvement Plan'))

# Print the final POWL model
print(root)