import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the exclusive choice operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[initial_assess, stakeholder_notify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[risk_analyze, command_setup])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[deploy_teams, data_collect])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[situation_update, priority_adjust])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[external_liaison, supply_dispatch])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[media_brief, impact_review])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, process_audit])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor4])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor5])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[xor6])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[xor7])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, xor5)
root.order.add_edge(loop6, xor6)
root.order.add_edge(loop7, xor7)
root.order.add_edge(xor1, loop1)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, loop3)
root.order.add_edge(xor4, loop4)
root.order.add_edge(xor5, loop5)
root.order.add_edge(xor6, loop6)
root.order.add_edge(xor7, loop7)