import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Data_Aggregation = Transition(label='Data Aggregation')
Anomaly_Detect = Transition(label='Anomaly Detect')
Risk_Assess = Transition(label='Risk Assess')
Demand_Model = Transition(label='Demand Model')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Auto_Negotiate = Transition(label='Auto Negotiate')
Inventory_Optimize = Transition(label='Inventory Optimize')
Contingency_Plan = Transition(label='Contingency Plan')
Resource_Allocate = Transition(label='Resource Allocate')
Sustainability_Check = Transition(label='Sustainability Check')
Compliance_Verify = Transition(label='Compliance Verify')
Impact_Score = Transition(label='Impact Score')
Distribution_Plan = Transition(label='Distribution Plan')
Feedback_Loop = Transition(label='Feedback Loop')
Performance_Audit = Transition(label='Performance Audit')
Schedule_Execute = Transition(label='Schedule Execute')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Data_Aggregation, Anomaly_Detect, Risk_Assess, Demand_Model, Stakeholder_Sync, Auto_Negotiate, Inventory_Optimize])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Contingency_Plan, Resource_Allocate, Sustainability_Check, Compliance_Verify, Impact_Score])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Distribution_Plan, Feedback_Loop, Performance_Audit, Schedule_Execute])

xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2, loop3])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop3)

# Print the POWL model
print(root)