import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
data_ingest     = Transition(label='Data Ingest')
status_check    = Transition(label='Status Check')
forecast_update = Transition(label='Forecast Update')
risk_assess     = Transition(label='Risk Assess')
scenario_sim    = Transition(label='Scenario Sim')
model_run       = Transition(label='Model Run')
option_select   = Transition(label='Option Select')
team_review     = Transition(label='Team Review')
plan_approve    = Transition(label='Plan Approve')
procure_adjust  = Transition(label='Procure Adjust')
route_replan    = Transition(label='Route Replan')
inventory_shift = Transition(label='Inventory Shift')
execute_updates = Transition(label='Execute Updates')
monitor_kpis    = Transition(label='Monitor KPIs')
feedback_loop   = Transition(label='Feedback Loop')

# Loop body for the adaptive decision-making cycle
loop_body = StrictPartialOrder(nodes=[
    procure_adjust, route_replan, inventory_shift, execute_updates
])
loop_body.order.add_edge(procure_adjust, route_replan)
loop_body.order.add_edge(route_replan, inventory_shift)
loop_body.order.add_edge(inventory_shift, execute_updates)

# LOOP operator: execute the loop_body once, then optionally repeat
adaptive_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_kpis, loop_body]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    data_ingest, status_check, forecast_update, risk_assess,
    scenario_sim, model_run, option_select, team_review,
    plan_approve, adaptive_loop, feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(data_ingest, status_check)
root.order.add_edge(status_check, forecast_update)
root.order.add_edge(forecast_update, risk_assess)
root.order.add_edge(risk_assess, scenario_sim)
root.order.add_edge(scenario_sim, model_run)
root.order.add_edge(model_run, option_select)
root.order.add_edge(option_select, team_review)
root.order.add_edge(team_review, plan_approve)
root.order.add_edge(plan_approve, adaptive_loop)
root.order.add_edge(adaptive_loop, feedback_loop)