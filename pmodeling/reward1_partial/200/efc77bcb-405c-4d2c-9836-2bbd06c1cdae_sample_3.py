import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[route_update, supplier_sync])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[contract_mod, blockchain_verify])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, scenario_sim])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, ai_adjust])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[waste_audit, report_generate])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_alert, compliance_review])

# Construct the POWL model
root = StrictPartialOrder(nodes=[data_capture, quantum_calc, demand_forecast, inventory_check, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(data_capture, quantum_calc)
root.order.add_edge(quantum_calc, demand_forecast)
root.order.add_edge(demand_forecast, inventory_check)
root.order.add_edge(inventory_check, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, contract_mod)
root.order.add_edge(xor6, blockchain_verify)
root.order.add_edge(xor6, risk_assess)
root.order.add_edge(xor6, scenario_sim)
root.order.add_edge(xor6, feedback_loop)
root.order.add_edge(xor6, ai_adjust)
root.order.add_edge(xor6, waste_audit)
root.order.add_edge(xor6, report_generate)
root.order.add_edge(xor6, stakeholder_alert)
root.order.add_edge(xor6, compliance_review)

print(root)