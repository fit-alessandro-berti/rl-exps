import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the workflow
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
    ]
)

# Define the order of the nodes
root.order.add_edge(Data_Ingest, Status_Check)
root.order.add_edge(Status_Check, Forecast_Update)
root.order.add_edge(Forecast_Update, Risk_Assess)
root.order.add_edge(Risk_Assess, Scenario_Sim)
root.order.add_edge(Scenario_Sim, Model_Run)
root.order.add_edge(Model_Run, Option_Select)
root.order.add_edge(Option_Select, Team_Review)
root.order.add_edge(Team_Review, Plan_Approve)
root.order.add_edge(Plan_Approve, Procure_Adjust)
root.order.add_edge(Procure_Adjust, Route_Replan)
root.order.add_edge(Route_Replan, Inventory_Shift)
root.order.add_edge(Inventory_Shift, Execute_Updates)
root.order.add_edge(Execute_Updates, Monitor_KPIs)
root.order.add_edge(Monitor_KPIs, Feedback_Loop)

print(root)