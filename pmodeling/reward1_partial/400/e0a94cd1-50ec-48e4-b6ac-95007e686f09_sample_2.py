import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[scenario_simulate, feedback_loop])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[anomaly_detect, quantum_communicate])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[quantum_setup, inventory_adjust])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, procurement_plan])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, network_adapt])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[decision_automate, cost_analyze])

# Construct the POWL model
root = StrictPartialOrder(nodes=[
    data_ingestion,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6
])

# Add dependencies
root.order.add_edge(data_ingestion, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor2)

print(root)