from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define partial order structure
root = StrictPartialOrder(
    nodes=[data_ingestion, quantum_setup, route_optimize, demand_forecast, scenario_simulate,
           risk_assess, anomaly_detect, supplier_sync, quantum_communicate, inventory_adjust,
           procurement_plan, performance_track, feedback_loop, decision_automate, cost_analyze,
           network_adapt],
    order={
        (data_ingestion, quantum_setup),
        (quantum_setup, route_optimize),
        (route_optimize, demand_forecast),
        (demand_forecast, scenario_simulate),
        (scenario_simulate, risk_assess),
        (risk_assess, anomaly_detect),
        (anomaly_detect, supplier_sync),
        (supplier_sync, quantum_communicate),
        (quantum_communicate, inventory_adjust),
        (inventory_adjust, procurement_plan),
        (procurement_plan, performance_track),
        (performance_track, feedback_loop),
        (feedback_loop, decision_automate),
        (decision_automate, cost_analyze),
        (cost_analyze, network_adapt)
    }
)

# Print the POWL model
print(root)