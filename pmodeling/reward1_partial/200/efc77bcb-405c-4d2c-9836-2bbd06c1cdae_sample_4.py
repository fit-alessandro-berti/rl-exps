import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
loop_quantum_calc = OperatorPOWL(operator=Operator.LOOP, children=[quantum_calc])
xor_data_capture = OperatorPOWL(operator=Operator.XOR, children=[data_capture, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_quantum_calc, xor_data_capture, demand_forecast, inventory_check, route_update, shipment_plan, supplier_sync, contract_mod, blockchain_verify, risk_assess, scenario_sim, feedback_loop, ai_adjust, waste_audit, report_generate, stakeholder_alert, compliance_review])

# Add edges to the root model
root.order.add_edge(loop_quantum_calc, xor_data_capture)
root.order.add_edge(xor_data_capture, demand_forecast)
root.order.add_edge(demand_forecast, inventory_check)
root.order.add_edge(inventory_check, route_update)
root.order.add_edge(route_update, shipment_plan)
root.order.add_edge(shipment_plan, supplier_sync)
root.order.add_edge(supplier_sync, contract_mod)
root.order.add_edge(contract_mod, blockchain_verify)
root.order.add_edge(blockchain_verify, risk_assess)
root.order.add_edge(risk_assess, scenario_sim)
root.order.add_edge(scenario_sim, feedback_loop)
root.order.add_edge(feedback_loop, ai_adjust)
root.order.add_edge(ai_adjust, waste_audit)
root.order.add_edge(waste_audit, report_generate)
root.order.add_edge(report_generate, stakeholder_alert)
root.order.add_edge(stakeholder_alert, compliance_review)

print(root)