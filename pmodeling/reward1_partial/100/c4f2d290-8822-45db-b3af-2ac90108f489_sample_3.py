import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
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

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
        data_ingest,
        status_check,
        forecast_update,
        risk_assess,
        scenario_sim,
        model_run,
        option_select,
        team_review,
        plan_approve,
        procure_adjust,
        route_replan,
        inventory_shift,
        execute_updates,
        monitor_kpis,
        feedback_loop
    ],
    order=[
        (data_ingest, status_check),
        (data_ingest, forecast_update),
        (status_check, risk_assess),
        (forecast_update, risk_assess),
        (risk_assess, scenario_sim),
        (scenario_sim, model_run),
        (model_run, option_select),
        (option_select, team_review),
        (team_review, plan_approve),
        (plan_approve, procure_adjust),
        (plan_approve, route_replan),
        (plan_approve, inventory_shift),
        (procure_adjust, execute_updates),
        (route_replan, execute_updates),
        (inventory_shift, execute_updates),
        (execute_updates, monitor_kpis),
        (monitor_kpis, feedback_loop),
        (feedback_loop, data_ingest)
    ]
)

print(root)