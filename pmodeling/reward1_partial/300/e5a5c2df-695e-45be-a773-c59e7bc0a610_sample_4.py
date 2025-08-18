import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[initial_assess, resource_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, risk_analyze])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[command_setup, deploy_teams])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[data_collect, situation_update])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[priority_adjust, external_liaison])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[supply_dispatch, media_brief])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[impact_review, recovery_plan])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[process_audit, alert_trigger])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor)