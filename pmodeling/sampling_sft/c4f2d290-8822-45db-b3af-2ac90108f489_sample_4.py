import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Loop for iterative scenario evaluation and approval
loop_body = StrictPartialOrder(nodes=[model_run, option_select, team_review, plan_approve])
loop_body.order.add_edge(model_run, option_select)
loop_body.order.add_edge(option_select, team_review)
loop_body.order.add_edge(team_review, plan_approve)

loop = OperatorPOWL(operator=Operator.LOOP, children=[scenario_sim, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    data_ingest,
    status_check,
    forecast_update,
    risk_assess,
    loop,
    procure_adjust,
    route_replan,
    inventory_shift,
    execute_updates,
    monitor_kpis,
    feedback_loop
])

# Define control-flow dependencies
root.order.add_edge(data_ingest, status_check)
root.order.add_edge(status_check, forecast_update)
root.order.add_edge(forecast_update, risk_assess)
root.order.add_edge(risk_assess, loop)
root.order.add_edge(loop, procure_adjust)
root.order.add_edge(loop, route_replan)
root.order.add_edge(loop, inventory_shift)
root.order.add_edge(loop, execute_updates)
root.order.add_edge(procur_adjust, monitor_kpis)
root.order.add_edge(route_replan, monitor_kpis)
root.order.add_edge(inventory_shift, monitor_kpis)
root.order.add_edge(execute_updates, monitor_kpis)
root.order.add_edge(monitor_kpis, feedback_loop)