from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
quantum_init = Transition(label='Quantum Init')
data_ingest = Transition(label='Data Ingest')
ai_forecast = Transition(label='AI Forecast')
inventory_sync = Transition(label='Inventory Sync')
procurement_plan = Transition(label='Procurement Plan')
production_align = Transition(label='Production Align')
distribution_map = Transition(label='Distribution Map')
iot_monitor = Transition(label='IoT Monitor')
risk_assess = Transition(label='Risk Assess')
maintenance_alert = Transition(label='Maintenance Alert')
quantum_compute = Transition(label='Quantum Compute')
feedback_loop = Transition(label='Feedback Loop')
schedule_adjust = Transition(label='Schedule Adjust')
demand_update = Transition(label='Demand Update')
delivery_track = Transition(label='Delivery Track')
compliance_check = Transition(label='Compliance Check')

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[quantum_init, data_ingest])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ai_forecast, inventory_sync])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[procurement_plan, production_align])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[distribution_map, iot_monitor])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, maintenance_alert])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[quantum_compute, feedback_loop])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[schedule_adjust, demand_update])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[delivery_track, compliance_check])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

print(root)