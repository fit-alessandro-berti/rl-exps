import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
alert = Transition(label='Alert Trigger')
initial = Transition(label='Initial Assess')
stakeholder = Transition(label='Stakeholder Notify')
resource = Transition(label='Resource Check')
risk = Transition(label='Risk Analyze')
command = Transition(label='Command Setup')
deploy = Transition(label='Deploy Teams')
data = Transition(label='Data Collect')
update = Transition(label='Situation Update')
priority = Transition(label='Priority Adjust')
liaison = Transition(label='External Liaison')
supply = Transition(label='Supply Dispatch')
media = Transition(label='Media Brief')
impact = Transition(label='Impact Review')
recovery = Transition(label='Recovery Plan')
audit = Transition(label='Process Audit')

# Loop for continuous monitoring and adjustment
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[update, priority]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    alert,
    initial,
    stakeholder,
    resource,
    risk,
    command,
    deploy,
    data,
    monitor_loop,
    liaison,
    supply,
    media,
    impact,
    recovery,
    audit
])

# Initial assessment precedes stakeholder notification
root.order.add_edge(initial, stakeholder)

# Stakeholder notify precedes resource check
root.order.add_edge(stakeholder, resource)

# Resource check precedes risk analysis
root.order.add_edge(resource, risk)

# Risk analysis precedes command setup
root.order.add_edge(risk, command)

# Command setup precedes team deployment
root.order.add_edge(command, deploy)

# Deployment precedes data collection
root.order.add_edge(deploy, data)

# Data collection feeds into the monitoring loop
root.order.add_edge(data, monitor_loop)

# Monitoring loop feeds back into itself for continuous adjustment
root.order.add_edge(monitor_loop, monitor_loop)

# Monitor loop precedes liaison
root.order.add_edge(monitor_loop, liaison)

# Liaison precedes supply dispatch
root.order.add_edge(liaison, supply)

# Supply dispatch precedes media brief
root.order.add_edge(supply, media)

# Media brief precedes impact review
root.order.add_edge(media, impact)

# Impact review precedes recovery plan
root.order.add_edge(impact, recovery)

# Recovery plan precedes process audit
root.order.add_edge(recovery, audit)

# Alert trigger is the root activity
root.order.add_edge(alert, initial)