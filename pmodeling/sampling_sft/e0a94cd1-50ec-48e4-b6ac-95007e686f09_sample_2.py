import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
data_ingest = Transition(label='Data Ingestion')
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

# Loop for continuous feedback and performance tracking
loop_body = StrictPartialOrder(nodes=[
    performance_track,
    feedback_loop,
    cost_analyze,
    network_adapt
])
loop_body.order.add_edge(performance_track, feedback_loop)
loop_body.order.add_edge(feedback_loop, cost_analyze)
loop_body.order.add_edge(cost_analyze, network_adapt)
loop = OperatorPOWL(operator=Operator.LOOP, children=[scenario_simulate, loop_body])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    data_ingest,
    quantum_setup,
    route_optimize,
    demand_forecast,
    risk_assess,
    anomaly_detect,
    supplier_sync,
    quantum_communicate,
    inventory_adjust,
    procurement_plan,
    loop,
    decision_automate
])

# Define the control-flow dependencies
root.order.add_edge(data_ingest, quantum_setup)
root.order.add_edge(quantum_setup, route_optimize)
root.order.add_edge(quantum_setup, demand_forecast)
root.order.add_edge(route_optimize, risk_assess)
root.order.add_edge(demand_forecast, risk_assess)
root.order.add_edge(risk_assess, anomaly_detect)
root.order.add_edge(anomaly_detect, supplier_sync)
root.order.add_edge(supplier_sync, quantum_communicate)
root.order.add_edge(quantum_communicate, inventory_adjust)
root.order.add_edge(inventory_adjust, procurement_plan)
root.order.add_edge(procurement_plan, loop)
root.order.add_edge(loop, decision_automate)