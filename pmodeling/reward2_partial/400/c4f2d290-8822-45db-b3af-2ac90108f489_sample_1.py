import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define POWL model
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

# Define partial order
root = StrictPartialOrder(nodes=[data_ingest, status_check, forecast_update, risk_assess, scenario_sim, model_run, option_select, team_review, plan_approve, procure_adjust, route_replan, inventory_shift, execute_updates, monitor_kpis, feedback_loop])

# Define order edges
root.order.add_edge(data_ingest, status_check)
root.order.add_edge(status_check, forecast_update)
root.order.add_edge(forecast_update, risk_assess)
root.order.add_edge(risk_assess, scenario_sim)
root.order.add_edge(scenario_sim, model_run)
root.order.add_edge(model_run, option_select)
root.order.add_edge(option_select, team_review)
root.order.add_edge(team_review, plan_approve)
root.order.add_edge(plan_approve, procure_adjust)
root.order.add_edge(procure_adjust, route_replan)
root.order.add_edge(route_replan, inventory_shift)
root.order.add_edge(inventory_shift, execute_updates)
root.order.add_edge(execute_updates, monitor_kpis)
root.order.add_edge(monitor_kpis, feedback_loop)

# Print the POWL model
print(root)