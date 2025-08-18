from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Data_Ingest = Transition(label='Data Ingest')
Status_Check = Transition(label='Status Check')
Forecast_Update = Transition(label='Forecast Update')
Risk_Assess = Transition(label='Risk Assess')
Scenario_Sim = Transition(label='Scenario Sim')
Model_Run = Transition(label='Model Run')
Option_Select = Transition(label='Option Select')
Team_Review = Transition(label='Team Review')
Plan_Approve = Transition(label='Plan Approve')
Procure_Adjust = Transition(label='Procure Adjust')
Route_Replan = Transition(label='Route Replan')
Inventory_Shift = Transition(label='Inventory Shift')
Execute_Updates = Transition(label='Execute Updates')
Monitor_KPIs = Transition(label='Monitor KPIs')
Feedback_Loop = Transition(label='Feedback Loop')

# Define the process using POWL
root = StrictPartialOrder(
    nodes=[
        Data_Ingest,
        Status_Check,
        Forecast_Update,
        Risk_Assess,
        Scenario_Sim,
        Model_Run,
        Option_Select,
        Team_Review,
        Plan_Approve,
        Procure_Adjust,
        Route_Replan,
        Inventory_Shift,
        Execute_Updates,
        Monitor_KPIs,
        Feedback_Loop
    ],
    order={
        (Data_Ingest, Status_Check): None,
        (Data_Ingest, Forecast_Update): None,
        (Status_Check, Risk_Assess): None,
        (Forecast_Update, Risk_Assess): None,
        (Risk_Assess, Scenario_Sim): None,
        (Scenario_Sim, Model_Run): None,
        (Model_Run, Option_Select): None,
        (Option_Select, Team_Review): None,
        (Team_Review, Plan_Approve): None,
        (Plan_Approve, Procure_Adjust): None,
        (Procure_Adjust, Route_Replan): None,
        (Route_Replan, Inventory_Shift): None,
        (Inventory_Shift, Execute_Updates): None,
        (Execute_Updates, Monitor_KPIs): None,
        (Monitor_KPIs, Feedback_Loop): None
    }
)

# Define the loop for the feedback loop
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop])
root.order.add_edge(feedback_loop, Feedback_Loop)

# Define the choice for the risk assessment
risk_assess_choice = OperatorPOWL(operator=Operator.XOR, children=[Scenario_Sim, Model_Run])
root.order.add_edge(Risk_Assess, risk_assess_choice)

# Define the choice for the model run
model_run_choice = OperatorPOWL(operator=Operator.XOR, children=[Option_Select, Plan_Approve])
root.order.add_edge(Scenario_Sim, model_run_choice)
root.order.add_edge(Model_Run, model_run_choice)

# Define the choice for the option select
option_select_choice = OperatorPOWL(operator=Operator.XOR, children=[Procure_Adjust, Route_Replan])
root.order.add_edge(Option_Select, option_select_choice)

# Define the choice for the plan approve
plan_approve_choice = OperatorPOWL(operator=Operator.XOR, children=[Inventory_Shift, Execute_Updates])
root.order.add_edge(Plan_Approve, plan_approve_choice)

# Define the choice for the execute updates
execute_updates_choice = OperatorPOWL(operator=Operator.XOR, children=[Monitor_KPIs, Feedback_Loop])
root.order.add_edge(Execute_Updates, execute_updates_choice)

# Print the root
print(root)