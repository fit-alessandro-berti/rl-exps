import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
data_ingest = Transition(label='Data Ingest')
status_check = Transition(label='Status Check')
forecast_update = Transition(label='Forecast Update')
risk_assess = Transition(label='Risk Assess')
scenario_sim = Transition(label='Scenario Sim')
model_run = Transition(label='Model Run')
option_select = Transition(label='Option Select')
team_review = Transition(label='Team Review')
plan_approve = Transition(label='Plan Approve')
procure_adjust = Transition(label='Procure Adjust')
route_replan = Transition(label='Route Replan')
inventory_shift = Transition(label='Inventory Shift')
execute_updates = Transition(label='Execute Updates')
monitor_kpis = Transition(label='Monitor KPIs')
feedback_loop = Transition(label='Feedback Loop')

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[data_ingest, status_check, forecast_update])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, scenario_sim, model_run])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[option_select, team_review, plan_approve])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[procure_adjust, route_replan, inventory_shift])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[execute_updates, monitor_kpis, feedback_loop])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)

# Print the root POWL model
print(root)