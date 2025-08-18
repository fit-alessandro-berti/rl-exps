from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
data_ingestion = Transition(label='Data Ingestion')
quantum_setup = Transition(label='Quantum Setup')
route_optimize = Transition(label='Route Optimize')
demand_forecast = Transition(label='Demand Forecast')
scenario_simulate = Transition(label='Scenario Simulate')
risk_assess = Transition(label='Risk Assess')
anomaly_detect = Transition(label='Anomaly Detect')
supplier_sync = Transition(label='Supplier Sync')
quantum_communicate = Transition(label='Quantum Communicate')
inventory_adjust = Transition(label='Inventory Adjust')
procurement_plan = Transition(label='Procurement Plan')
performance_track = Transition(label='Performance Track')
feedback_loop = Transition(label='Feedback Loop')
decision_automate = Transition(label='Decision Automate')
cost_analyze = Transition(label='Cost Analyze')
network_adapt = Transition(label='Network Adapt')

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[anomaly_detect, supplier_sync])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quantum_communicate, risk_assess])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[procurement_plan, inventory_adjust])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[performance_track, feedback_loop])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[cost_analyze, network_adapt])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[decision_automate, quantum_setup])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[route_optimize, demand_forecast])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[scenario_simulate, xor5])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[xor2, xor4])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[xor3, xor9])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[xor6, xor10])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[xor11, xor8, xor7])
root.order.add_edge(xor11, xor8)
root.order.add_edge(xor8, xor7)
root.order.add_edge(xor7, xor6)
root.order.add_edge(xor6, xor5)
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, xor11)

# Output the root POWL model
print(root)