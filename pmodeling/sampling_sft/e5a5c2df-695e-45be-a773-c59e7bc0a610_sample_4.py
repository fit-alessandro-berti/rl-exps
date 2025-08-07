import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
alert_trigger    = Transition(label='Alert Trigger')
initial_assess   = Transition(label='Initial Assess')
stakeholder_notify = Transition(label='Stakeholder Notify')
resource_check   = Transition(label='Resource Check')
risk_analyze     = Transition(label='Risk Analyze')
command_setup    = Transition(label='Command Setup')
deploy_teams     = Transition(label='Deploy Teams')
data_collect     = Transition(label='Data Collect')
situation_update = Transition(label='Situation Update')
priority_adjust  = Transition(label='Priority Adjust')
external_liaison = Transition(label='External Liaison')
supply_dispatch  = Transition(label='Supply Dispatch')
media_brief      = Transition(label='Media Brief')
impact_review    = Transition(label='Impact Review')
recovery_plan    = Transition(label='Recovery Plan')
process_audit    = Transition(label='Process Audit')

# Loop for continuous monitoring: Situation Update, then optionally adjust priority and update data, then repeat
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[situation_update, OperatorPOWL(operator=Operator.XOR, children=[priority_adjust, data_collect])]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    alert_trigger,
    initial_assess,
    stakeholder_notify,
    resource_check,
    risk_analyze,
    command_setup,
    deploy_teams,
    monitor_loop,
    external_liaison,
    supply_dispatch,
    media_brief,
    impact_review,
    recovery_plan,
    process_audit
])

# Define the control-flow dependencies
root.order.add_edge(alert_trigger, initial_assess)
root.order.add_edge(initial_assess, stakeholder_notify)
root.order.add_edge(stakeholder_notify, resource_check)
root.order.add_edge(resource_check, risk_analyze)
root.order.add_edge(risk_analyze, command_setup)
root.order.add_edge(command_setup, deploy_teams)
root.order.add_edge(deploy_teams, monitor_loop)
root.order.add_edge(monitor_loop, external_liaison)
root.order.add_edge(external_liaison, supply_dispatch)
root.order.add_edge(supply_dispatch, media_brief)
root.order.add_edge(media_brief, impact_review)
root.order.add_edge(impact_review, recovery_plan)
root.order.add_edge(recovery_plan, process_audit)

print(root)