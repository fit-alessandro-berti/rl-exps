import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop and exclusive choice nodes
loop_quantum = OperatorPOWL(operator=Operator.LOOP, children=[quantum_calc, skip])
xor_data_capture = OperatorPOWL(operator=Operator.XOR, children=[data_capture, skip])
xor_scenario = OperatorPOWL(operator=Operator.XOR, children=[scenario_sim, skip])
xor_audit = OperatorPOWL(operator=Operator.XOR, children=[waste_audit, skip])
xor_contract = OperatorPOWL(operator=Operator.XOR, children=[contract_mod, skip])
xor_verify = OperatorPOWL(operator=Operator.XOR, children=[blockchain_verify, skip])
xor_alert = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_alert, skip])
xor_review = OperatorPOWL(operator=Operator.XOR, children=[compliance_review, skip])

# Define the root node
root = StrictPartialOrder(nodes=[loop_quantum, xor_data_capture, xor_scenario, xor_audit, xor_contract, xor_verify, xor_alert, xor_review])
root.order.add_edge(loop_quantum, xor_data_capture)
root.order.add_edge(loop_quantum, xor_scenario)
root.order.add_edge(xor_data_capture, xor_audit)
root.order.add_edge(xor_data_capture, xor_contract)
root.order.add_edge(xor_scenario, xor_verify)
root.order.add_edge(xor_scenario, xor_alert)
root.order.add_edge(xor_audit, xor_review)
root.order.add_edge(xor_contract, xor_review)
root.order.add_edge(xor_verify, xor_review)
root.order.add_edge(xor_alert, xor_review)