from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
quantum_loop = OperatorPOWL(operator=Operator.LOOP, children=[quantum_setup, data_ingestion])
scenario_loop = OperatorPOWL(operator=Operator.LOOP, children=[scenario_simulate, risk_assess])

# Define exclusive choice nodes
anomaly_choice = OperatorPOWL(operator=Operator.XOR, children=[anomaly_detect, skip])
quantum_choice = OperatorPOWL(operator=Operator.XOR, children=[quantum_communicate, skip])
sync_choice = OperatorPOWL(operator=Operator.XOR, children=[supplier_sync, skip])

# Define partial order
root = StrictPartialOrder(nodes=[
    data_ingestion, quantum_setup, route_optimize, demand_forecast, scenario_simulate, risk_assess, anomaly_detect, 
    supplier_sync, quantum_communicate, inventory_adjust, procurement_plan, performance_track, feedback_loop, decision_automate, 
    cost_analyze, network_adapt, quantum_loop, scenario_loop, anomaly_choice, quantum_choice, sync_choice])

# Add dependencies to the partial order
root.order.add_edge(quantum_loop, scenario_loop)
root.order.add_edge(scenario_loop, anomaly_choice)
root.order.add_edge(anomaly_choice, quantum_choice)
root.order.add_edge(quantum_choice, sync_choice)
root.order.add_edge(sync_choice, decision_automate)
root.order.add_edge(decision_automate, cost_analyze)
root.order.add_edge(cost_analyze, network_adapt)

print(root)