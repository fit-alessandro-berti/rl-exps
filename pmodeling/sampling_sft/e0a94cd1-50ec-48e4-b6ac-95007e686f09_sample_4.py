import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
data_ingestion   = Transition(label='Data Ingestion')
quantum_setup    = Transition(label='Quantum Setup')
route_optimize   = Transition(label='Route Optimize')
demand_forecast  = Transition(label='Demand Forecast')
scenario_simulate = Transition(label='Scenario Simulate')
risk_assess      = Transition(label='Risk Assess')
anomaly_detect   = Transition(label='Anomaly Detect')
supplier_sync    = Transition(label='Supplier Sync')
quantum_communicate = Transition(label='Quantum Communicate')
inventory_adjust = Transition(label='Inventory Adjust')
procurement_plan = Transition(label='Procurement Plan')
decision_automate = Transition(label='Decision Automate')
cost_analyze     = Transition(label='Cost Analyze')
network_adapt    = Transition(label='Network Adapt')

# Define the feedback loop: do Performance Track, then optionally do Feedback Loop again
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Transition(label='Performance Track'), Transition(label='Feedback Loop')]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    data_ingestion,
    quantum_setup,
    route_optimize,
    demand_forecast,
    scenario_simulate,
    risk_assess,
    anomaly_detect,
    supplier_sync,
    quantum_communicate,
    inventory_adjust,
    procurement_plan,
    decision_automate,
    cost_analyze,
    network_adapt,
    feedback_loop
])

# Add the sequential dependencies
root.order.add_edge(data_ingestion,   quantum_setup)
root.order.add_edge(quantum_setup,    route_optimize)
root.order.add_edge(quantum_setup,    demand_forecast)
root.order.add_edge(route_optimize,   scenario_simulate)
root.order.add_edge(demand_forecast,  scenario_simulate)
root.order.add_edge(scenario_simulate, risk_assess)
root.order.add_edge(scenario_simulate, anomaly_detect)
root.order.add_edge(scenario_simulate, supplier_sync)
root.order.add_edge(scenario_simulate, quantum_communicate)
root.order.add_edge(risk_assess,      inventory_adjust)
root.order.add_edge(anomaly_detect,   inventory_adjust)
root.order.add_edge(supplier_sync,    inventory_adjust)
root.order.add_edge(quantum_communicate, inventory_adjust)
root.order.add_edge(inventory_adjust, procurement_plan)
root.order.add_edge(procurement_plan, decision_automate)
root.order.add_edge(decision_automate, cost_analyze)
root.order.add_edge(cost_analyze,     network_adapt)

# The feedback loop starts after Performance Track
root.order.add_edge(Transition(label='Performance Track'), feedback_loop)

# The loop continues with Feedback Loop as the body
root.order.add_edge(feedback_loop, Transition(label='Feedback Loop'))

print(root)