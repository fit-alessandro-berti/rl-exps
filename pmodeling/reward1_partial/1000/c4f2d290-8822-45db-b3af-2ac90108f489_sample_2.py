import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
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

# Define the structure of the process using POWL operators
data_ingestion = OperatorPOWL(operator=Operator.LOOP, children=[Data_Ingest, Status_Check, Forecast_Update])
risk_assessment = OperatorPOWL(operator=Operator.LOOP, children=[Risk_Assess, Scenario_Sim, Model_Run])
option_selection = OperatorPOWL(operator=Operator.XOR, children=[Option_Select, Team_Review])
decision_making = OperatorPOWL(operator=Operator.XOR, children=[Plan_Approve, Procure_Adjust, Route_Replan, Inventory_Shift])
implementation = OperatorPOWL(operator=Operator.LOOP, children=[Execute_Updates, Monitor_KPIs, Feedback_Loop])

# Create the root node of the process
root = StrictPartialOrder(nodes=[data_ingestion, risk_assessment, option_selection, decision_making, implementation])
root.order.add_edge(data_ingestion, risk_assessment)
root.order.add_edge(risk_assessment, option_selection)
root.order.add_edge(option_selection, decision_making)
root.order.add_edge(decision_making, implementation)

print(root)