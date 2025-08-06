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

# Define the silent transitions
skip = SilentTransition()

# Define the partial order structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Status_Check, Forecast_Update, Risk_Assess, Scenario_Sim, Model_Run])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Option_Select, Team_Review, Plan_Approve])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Procure_Adjust, Route_Replan, Inventory_Shift])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Execute_Updates, Monitor_KPIs, Feedback_Loop])

# Define the XOR structure for the main process
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])

# Define the root partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)

# Print the root POWL model
print(root)