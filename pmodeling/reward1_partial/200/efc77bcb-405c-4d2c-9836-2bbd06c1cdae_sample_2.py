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

# Define silent transitions for the loop and XOR operators
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, quantum_calc])
xor = OperatorPOWL(operator=Operator.XOR, children=[inventory_check, skip])

# Define the root partial order with the defined nodes and order
root = StrictPartialOrder(nodes=[loop, xor, demand_forecast, route_update, shipment_plan, supplier_sync, contract_mod, blockchain_verify, risk_assess, scenario_sim, feedback_loop, ai_adjust, waste_audit, report_generate, stakeholder_alert, compliance_review])
root.order.add_edge(loop, demand_forecast)
root.order.add_edge(loop, route_update)
root.order.add_edge(loop, shipment_plan)
root.order.add_edge(loop, supplier_sync)
root.order.add_edge(loop, contract_mod)
root.order.add_edge(loop, blockchain_verify)
root.order.add_edge(loop, risk_assess)
root.order.add_edge(loop, scenario_sim)
root.order.add_edge(loop, feedback_loop)
root.order.add_edge(loop, ai_adjust)
root.order.add_edge(loop, waste_audit)
root.order.add_edge(loop, report_generate)
root.order.add_edge(loop, stakeholder_alert)
root.order.add_edge(loop, compliance_review)

print(root)