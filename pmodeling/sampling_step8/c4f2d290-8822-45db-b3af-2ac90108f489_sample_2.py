import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the POWL model
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
    order=[
        (Data_Ingest, Status_Check),
        (Status_Check, Forecast_Update),
        (Forecast_Update, Risk_Assess),
        (Risk_Assess, Scenario_Sim),
        (Scenario_Sim, Model_Run),
        (Model_Run, Option_Select),
        (Option_Select, Team_Review),
        (Team_Review, Plan_Approve),
        (Plan_Approve, Procure_Adjust),
        (Procure_Adjust, Route_Replan),
        (Route_Replan, Inventory_Shift),
        (Inventory_Shift, Execute_Updates),
        (Execute_Updates, Monitor_KPIs),
        (Monitor_KPIs, Feedback_Loop)
    ]
)