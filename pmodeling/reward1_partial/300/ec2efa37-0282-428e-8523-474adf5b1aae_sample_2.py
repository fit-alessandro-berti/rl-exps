import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[quantum_compute, maintenance_alert])
loop = OperatorPOWL(operator=Operator.LOOP, children=[iot_monitor, risk_assess])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, compliance_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[schedule_adjust, demand_update])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[delivery_track, compliance_check])

# Define the partial order
root = StrictPartialOrder(nodes=[quantum_init, data_ingest, ai_forecast, inventory_sync, procurement_plan, production_align, distribution_map, xor, loop, xor2, xor3, xor4])
root.order.add_edge(quantum_init, data_ingest)
root.order.add_edge(data_ingest, ai_forecast)
root.order.add_edge(ai_forecast, inventory_sync)
root.order.add_edge(inventory_sync, procurement_plan)
root.order.add_edge(procurement_plan, production_align)
root.order.add_edge(production_align, distribution_map)
root.order.add_edge(distribution_map, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, compliance_check)

# Print the root node
print(root)