import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
alert_trigger   = Transition(label='Alert Trigger')
initial_assess  = Transition(label='Initial Assess')
stakeholder_n   = Transition(label='Stakeholder Notify')
resource_check  = Transition(label='Resource Check')
risk_analyze    = Transition(label='Risk Analyze')
command_setup   = Transition(label='Command Setup')
deploy_teams    = Transition(label='Deploy Teams')
data_collect    = Transition(label='Data Collect')
situation_update= Transition(label='Situation Update')
priority_adjust = Transition(label='Priority Adjust')
external_liaison= Transition(label='External Liaison')
supply_dispatch = Transition(label='Supply Dispatch')
media_brief     = Transition(label='Media Brief')
impact_review   = Transition(label='Impact Review')
recovery_plan   = Transition(label='Recovery Plan')
process_audit   = Transition(label='Process Audit')

# Phase 1: Alert trigger and initial assessment
phase1 = StrictPartialOrder(nodes=[alert_trigger, initial_assess, stakeholder_n, resource_check, risk_analyze])
phase1.order.add_edge(alert_trigger, initial_assess)
phase1.order.add_edge(initial_assess, stakeholder_n)
phase1.order.add_edge(initial_assess, resource_check)
phase1.order.add_edge(stakeholder_n, risk_analyze)
phase1.order.add_edge(resource_check, risk_analyze)

# Phase 2: Command setup and resource deployment
phase2 = StrictPartialOrder(nodes=[command_setup, deploy_teams, data_collect, situation_update, priority_adjust])
phase2.order.add_edge(command_setup, deploy_teams)
phase2.order.add_edge(command_setup, data_collect)
phase2.order.add_edge(data_collect, situation_update)
phase2.order.add_edge(situation_update, priority_adjust)

# Phase 3: External liaison and supply dispatch
phase3 = StrictPartialOrder(nodes=[external_liaison, supply_dispatch, media_brief, impact_review])
phase3.order.add_edge(external_liaison, supply_dispatch)
phase3.order.add_edge(external_liaison, media_brief)
phase3.order.add_edge(supply_dispatch, impact_review)
phase3.order.add_edge(media_brief, impact_review)

# Phase 4: Recovery plan and process audit
phase4 = StrictPartialOrder(nodes=[recovery_plan, process_audit])
phase4.order.add_edge(recovery_plan, process_audit)

# Loop: continuously update and adjust priorities until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[phase3, phase4])

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    phase1,
    phase2,
    loop
])
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, loop)