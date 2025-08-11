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

# Define silent activities
skip = SilentTransition()

# Define the exclusive choice (XOR) for IoT Monitor and Risk Assess
xor_iot_risk = OperatorPOWL(operator=Operator.XOR, children=[iot_monitor, risk_assess])

# Define the loop for Maintenance Alert and Compliance Check
loop_maintenance_compliance = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_alert, compliance_check])

# Define the partial order
root = StrictPartialOrder(nodes=[quantum_init, data_ingest, ai_forecast, inventory_sync, procurement_plan, production_align, distribution_map, xor_iot_risk, loop_maintenance_compliance, feedback_loop, schedule_adjust, demand_update, delivery_track])

# Define the dependencies
root.order.add_edge(quantum_init, data_ingest)
root.order.add_edge(quantum_init, ai_forecast)
root.order.add_edge(data_ingest, inventory_sync)
root.order.add_edge(ai_forecast, inventory_sync)
root.order.add_edge(inventory_sync, procurement_plan)
root.order.add_edge(inventory_sync, production_align)
root.order.add_edge(inventory_sync, distribution_map)
root.order.add_edge(distribution_map, xor_iot_risk)
root.order.add_edge(xor_iot_risk, loop_maintenance_compliance)
root.order.add_edge(loop_maintenance_compliance, feedback_loop)
root.order.add_edge(feedback_loop, schedule_adjust)
root.order.add_edge(schedule_adjust, demand_update)
root.order.add_edge(demand_update, delivery_track)
root.order.add_edge(delivery_track, compliance_check)

print(root)