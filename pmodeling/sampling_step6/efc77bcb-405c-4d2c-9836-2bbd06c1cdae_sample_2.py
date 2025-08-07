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

# Define the partial order
root = StrictPartialOrder(nodes=[data_capture, quantum_calc, demand_forecast, inventory_check, route_update, shipment_plan, supplier_sync, contract_mod, blockchain_verify, risk_assess, scenario_sim, feedback_loop, ai_adjust, waste_audit, report_generate, stakeholder_alert, compliance_review])

# Define dependencies if any (not applicable in this case, as all activities are independent)
# root.order.add_edge(data_capture, quantum_calc)
# root.order.add_edge(data_capture, demand_forecast)
# ...
# root.order.add_edge(feedback_loop, ai_adjust)
# ...

# Save the final result in the variable 'root'
print(root)