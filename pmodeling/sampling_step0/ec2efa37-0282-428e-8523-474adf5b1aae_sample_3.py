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

# Define the silent transitions
skip = SilentTransition()

# Define the loop nodes
quantum_loop = OperatorPOWL(operator=Operator.LOOP, children=[quantum_compute, skip])
iot_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[iot_monitor, skip])

# Define the XOR nodes
xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])

# Define the root node
root = StrictPartialOrder(nodes=[quantum_loop, iot_monitor_loop, xor])
root.order.add_edge(quantum_loop, iot_monitor_loop)
root.order.add_edge(iot_monitor_loop, xor)