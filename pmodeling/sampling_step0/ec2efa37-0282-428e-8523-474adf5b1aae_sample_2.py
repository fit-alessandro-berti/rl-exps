import pm4py
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

# Define the transitions
skip = SilentTransition()
xor = OperatorPOWL(operator=Operator.XOR, children=[quantum_init, data_ingest, ai_forecast, inventory_sync, procurement_plan, production_align, distribution_map, iot_monitor, risk_assess, maintenance_alert, quantum_compute, feedback_loop, schedule_adjust, demand_update, delivery_track, compliance_check])

# Define the partial order
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, xor)

print(root)