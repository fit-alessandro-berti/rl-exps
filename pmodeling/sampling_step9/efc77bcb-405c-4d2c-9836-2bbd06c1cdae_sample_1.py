import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, quantum_calc, demand_forecast, inventory_check])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[route_update, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[supplier_sync, contract_mod, blockchain_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, scenario_sim])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, ai_adjust])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[waste_audit, report_generate])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_alert, compliance_review])

root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)

# Print the POWL model
print(root)