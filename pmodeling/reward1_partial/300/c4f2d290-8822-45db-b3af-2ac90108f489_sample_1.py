import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

loop_data_ingest = OperatorPOWL(operator=Operator.LOOP, children=[data_ingest, status_check, forecast_update, risk_assess, scenario_sim, model_run, option_select, team_review, plan_approve, procure_adjust, route_replan, inventory_shift, execute_updates, monitor_kpis])
loop_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop])

root = StrictPartialOrder(nodes=[loop_data_ingest, loop_feedback_loop])
root.order.add_edge(loop_data_ingest, loop_feedback_loop)

print(root)