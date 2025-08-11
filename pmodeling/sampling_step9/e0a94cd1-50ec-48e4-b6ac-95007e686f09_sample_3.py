import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_adjust, procurement_plan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, route_optimize])

# Define XOR
xor = OperatorPOWL(operator=Operator.XOR, children=[anomaly_detect, skip])

# Define root
root = StrictPartialOrder(nodes=[quantum_setup, loop1, loop2, xor, decision_automate, cost_analyze, network_adapt])
root.order.add_edge(quantum_setup, loop1)
root.order.add_edge(quantum_setup, loop2)
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(xor, decision_automate)
root.order.add_edge(decision_automate, cost_analyze)
root.order.add_edge(cost_analyze, network_adapt)