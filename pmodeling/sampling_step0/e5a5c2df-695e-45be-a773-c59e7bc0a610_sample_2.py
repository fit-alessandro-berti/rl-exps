import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Alert_Trigger = Transition(label='Alert Trigger')
Initial_Assess = Transition(label='Initial Assess')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Resource_Check = Transition(label='Resource Check')
Risk_Analyze = Transition(label='Risk Analyze')
Command_Setup = Transition(label='Command Setup')
Deploy_Teams = Transition(label='Deploy Teams')
Data_Collect = Transition(label='Data Collect')
Situation_Update = Transition(label='Situation Update')
Priority_Adjust = Transition(label='Priority Adjust')
External_Liaison = Transition(label='External Liaison')
Supply_Dispatch = Transition(label='Supply Dispatch')
Media_Brief = Transition(label='Media Brief')
Impact_Review = Transition(label='Impact Review')
Recovery_Plan = Transition(label='Recovery Plan')
Process_Audit = Transition(label='Process Audit')

# Define silent transition (skip)
skip = SilentTransition()

# Define sub-processes
initial_assess = OperatorPOWL(operator=Operator.XOR, children=[Initial_Assess, skip])
stakeholder_notify = OperatorPOWL(operator=Operator.XOR, children=[Stakeholder_Notify, skip])
resource_check = OperatorPOWL(operator=Operator.XOR, children=[Resource_Check, skip])
risk_analyze = OperatorPOWL(operator=Operator.XOR, children=[Risk_Analyze, skip])
command_setup = OperatorPOWL(operator=Operator.XOR, children=[Command_Setup, skip])
deploy_teams = OperatorPOWL(operator=Operator.XOR, children=[Deploy_Teams, skip])
data_collect = OperatorPOWL(operator=Operator.XOR, children=[Data_Collect, skip])
situation_update = OperatorPOWL(operator=Operator.XOR, children=[Situation_Update, skip])
priority_adjust = OperatorPOWL(operator=Operator.XOR, children=[Priority_Adjust, skip])
external_liaison = OperatorPOWL(operator=Operator.XOR, children=[External_Liaison, skip])
supply_dispatch = OperatorPOWL(operator=Operator.XOR, children=[Supply_Dispatch, skip])
media_brief = OperatorPOWL(operator=Operator.XOR, children=[Media_Brief, skip])
impact_review = OperatorPOWL(operator=Operator.XOR, children=[Impact_Review, skip])
recovery_plan = OperatorPOWL(operator=Operator.XOR, children=[Recovery_Plan, skip])
process_audit = OperatorPOWL(operator=Operator.XOR, children=[Process_Audit, skip])

# Define loop for continuous monitoring and update
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    initial_assess,
    stakeholder_notify,
    resource_check,
    risk_analyze,
    command_setup,
    deploy_teams,
    data_collect,
    situation_update,
    priority_adjust,
    external_liaison,
    supply_dispatch,
    media_brief,
    impact_review,
    recovery_plan,
    process_audit
])

# Define root
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, initial_assess)
root.order.add_edge(initial_assess, stakeholder_notify)
root.order.add_edge(stakeholder_notify, resource_check)
root.order.add_edge(resource_check, risk_analyze)
root.order.add_edge(risk_analyze, command_setup)
root.order.add_edge(command_setup, deploy_teams)
root.order.add_edge(deploy_teams, data_collect)
root.order.add_edge(data_collect, situation_update)
root.order.add_edge(situation_update, priority_adjust)
root.order.add_edge(priority_adjust, external_liaison)
root.order.add_edge(external_liaison, supply_dispatch)
root.order.add_edge(supply_dispatch, media_brief)
root.order.add_edge(media_brief, impact_review)
root.order.add_edge(impact_review, recovery_plan)
root.order.add_edge(recovery_plan, process_audit)
root.order.add_edge(process_audit, initial_assess)