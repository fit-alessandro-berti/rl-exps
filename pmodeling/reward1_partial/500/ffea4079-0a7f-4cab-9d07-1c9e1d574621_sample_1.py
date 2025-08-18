import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
setup = Transition(label='Scenario Setup')
mapping = Transition(label='Resource Mapping')
briefing = Transition(label='Team Briefing')
tech = Transition(label='Tech Deployment')
sync = Transition(label='Data Sync')
comm = Transition(label='Comm Setup')
monitor = Transition(label='Live Monitoring')
adjust = Transition(label='Variable Adjust')
inject = Transition(label='Incident Injection')
track = Transition(label='Response Tracking')
check = Transition(label='Interlock Check')
feedback = Transition(label='Real-time Feedback')
debrief = Transition(label='Debrief Session')
outcome = Transition(label='Outcome Analysis')
report = Transition(label='Report Generation')
plan = Transition(label='Improvement Plan')

# Define the POWL model
root = StrictPartialOrder(nodes=[setup, mapping, briefing, tech, sync, comm, monitor, adjust, inject, track, check, feedback, debrief, outcome, report, plan])

# Add dependencies
root.order.add_edge(setup, mapping)
root.order.add_edge(mapping, briefing)
root.order.add_edge(briefing, tech)
root.order.add_edge(tech, sync)
root.order.add_edge(sync, comm)
root.order.add_edge(comm, monitor)
root.order.add_edge(monitor, adjust)
root.order.add_edge(adjust, inject)
root.order.add_edge(inject, track)
root.order.add_edge(track, check)
root.order.add_edge(check, feedback)
root.order.add_edge(feedback, debrief)
root.order.add_edge(debrief, outcome)
root.order.add_edge(outcome, report)
root.order.add_edge(report, plan)

print(root)