from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
data_capture = Transition(label='Data Capture')
quantum_calc = Transition(label='Quantum Calc')
demand_forecast = Transition(label='Demand Forecast')
inventory_check = Transition(label='Inventory Check')
route_update = Transition(label='Route Update')
shipment_plan = Transition(label='Shipment Plan')
supplier_sync = Transition(label='Supplier Sync')
contract_mod = Transition(label='Contract Mod')
blockchain_verify = Transition(label='Blockchain Verify')
risk_assess = Transition(label='Risk Assess')
scenario_sim = Transition(label='Scenario Sim')
feedback_loop = Transition(label='Feedback Loop')
ai_adjust = Transition(label='AI Adjust')
waste_audit = Transition(label='Waste Audit')
report_generate = Transition(label='Report Generate')
stakeholder_alert = Transition(label='Stakeholder Alert')
compliance_review = Transition(label='Compliance Review')

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[inventory_check, route_update])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[supplier_sync, contract_mod])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[blockchain_verify, risk_assess])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[scenario_sim, feedback_loop])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ai_adjust, waste_audit])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[report_generate, stakeholder_alert])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[compliance_review, SilentTransition()])

# Create the root partial order
root = StrictPartialOrder(
    nodes=[
        data_capture,
        quantum_calc,
        demand_forecast,
        xor1,
        xor2,
        xor3,
        xor4,
        xor5,
        xor6,
        xor7
    ]
)

# Define the dependencies between nodes
root.order.add_edge(data_capture, quantum_calc)
root.order.add_edge(quantum_calc, demand_forecast)
root.order.add_edge(demand_forecast, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, SilentTransition())  # Assuming the final node has no successor

print(root)