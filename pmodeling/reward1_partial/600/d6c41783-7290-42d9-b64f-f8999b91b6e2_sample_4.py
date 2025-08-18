from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
quantum_modeling = Transition(label='Quantum Modeling')
data_encoding = Transition(label='Data Encoding')
route_simulation = Transition(label='Route Simulation')
demand_forecast = Transition(label='Demand Forecast')
supplier_sync = Transition(label='Supplier Sync')
entangle_nodes = Transition(label='Entangle Nodes')
risk_analysis = Transition(label='Risk Analysis')
inventory_scan = Transition(label='Inventory Scan')
latency_check = Transition(label='Latency Check')
transport_plan = Transition(label='Transport Plan')
quantum_compute = Transition(label='Quantum Compute')
scenario_test = Transition(label='Scenario Test')
resource_align = Transition(label='Resource Align')
protocol_update = Transition(label='Protocol Update')
feedback_loop = Transition(label='Feedback Loop')
cost_optimize = Transition(label='Cost Optimize')
impact_review = Transition(label='Impact Review')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        quantum_modeling,
        data_encoding,
        route_simulation,
        demand_forecast,
        supplier_sync,
        entangle_nodes,
        risk_analysis,
        inventory_scan,
        latency_check,
        transport_plan,
        quantum_compute,
        scenario_test,
        resource_align,
        protocol_update,
        feedback_loop,
        cost_optimize,
        impact_review
    ],
    order=[
        (quantum_modeling, data_encoding),
        (data_encoding, route_simulation),
        (route_simulation, demand_forecast),
        (demand_forecast, supplier_sync),
        (supplier_sync, entangle_nodes),
        (entangle_nodes, risk_analysis),
        (risk_analysis, inventory_scan),
        (inventory_scan, latency_check),
        (latency_check, transport_plan),
        (transport_plan, quantum_compute),
        (quantum_compute, scenario_test),
        (scenario_test, resource_align),
        (resource_align, protocol_update),
        (protocol_update, feedback_loop),
        (feedback_loop, cost_optimize),
        (cost_optimize, impact_review)
    ]
)

print(root)