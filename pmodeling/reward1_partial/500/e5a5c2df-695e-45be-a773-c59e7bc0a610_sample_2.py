from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for the POWL model
alert_trigger = Transition(label='Alert Trigger')
initial_assess = Transition(label='Initial Assess')
stakeholder_notify = Transition(label='Stakeholder Notify')
resource_check = Transition(label='Resource Check')
risk_analyze = Transition(label='Risk Analyze')
command_setup = Transition(label='Command Setup')
deploy_teams = Transition(label='Deploy Teams')
data_collect = Transition(label='Data Collect')
situation_update = Transition(label='Situation Update')
priority_adjust = Transition(label='Priority Adjust')
external_liaison = Transition(label='External Liaison')
supply_dispatch = Transition(label='Supply Dispatch')
media_brief = Transition(label='Media Brief')
impact_review = Transition(label='Impact Review')
recovery_plan = Transition(label='Recovery Plan')
process_audit = Transition(label='Process Audit')

# Define the loop node for the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_assess, resource_check, risk_analyze, command_setup, deploy_teams, data_collect, situation_update, priority_adjust, external_liaison, supply_dispatch, media_brief, impact_review, recovery_plan, process_audit])

# Define the XOR node for the POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[alert_trigger, stakeholder_notify])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor, loop])
root.order.add_edge(xor, loop)

# Print the final POWL model
print(root)