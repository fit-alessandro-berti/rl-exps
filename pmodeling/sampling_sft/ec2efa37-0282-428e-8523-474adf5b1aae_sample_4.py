import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
quantum_init      = Transition(label='Quantum Init')
data_ingest       = Transition(label='Data Ingest')
ai_forecast       = Transition(label='AI Forecast')
inventory_sync    = Transition(label='Inventory Sync')
procurement_plan  = Transition(label='Procurement Plan')
production_align  = Transition(label='Production Align')
distribution_map  = Transition(label='Distribution Map')
iot_monitor       = Transition(label='IoT Monitor')
risk_assess       = Transition(label='Risk Assess')
maintenance_alert = Transition(label='Maintenance Alert')
quantum_compute   = Transition(label='Quantum Compute')
feedback_loop     = Transition(label='Feedback Loop')
schedule_adjust   = Transition(label='Schedule Adjust')
demand_update     = Transition(label='Demand Update')
delivery_track    = Transition(label='Delivery Track')
compliance_check  = Transition(label='Compliance Check')

# Build the inner loop body: IoT Monitor -> Risk Assess -> Maintenance Alert
body = StrictPartialOrder(nodes=[iot_monitor, risk_assess, maintenance_alert])
body.order.add_edge(iot_monitor, risk_assess)
body.order.add_edge(risk_assess, maintenance_alert)

# Define the loop: do body, then optionally run Feedback Loop and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, feedback_loop])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    quantum_init, data_ingest, ai_forecast, inventory_sync,
    procurement_plan, production_align, distribution_map,
    loop, schedule_adjust, demand_update, delivery_track,
    compliance_check
])

# Define the control-flow dependencies
root.order.add_edge(quantum_init, data_ingest)
root.order.add_edge(data_ingest, ai_forecast)
root.order.add_edge(ai_forecast, inventory_sync)
root.order.add_edge(inventory_sync, procurement_plan)
root.order.add_edge(inventory_sync, production_align)
root.order.add_edge(inventory_sync, distribution_map)
root.order.add_edge(procurement_plan, schedule_adjust)
root.order.add_edge(production_align, schedule_adjust)
root.order.add_edge(distribution_map, schedule_adjust)
root.order.add_edge(schedule_adjust, demand_update)
root.order.add_edge(demand_update, delivery_track)
root.order.add_edge(delivery_track, compliance_check)

# The loop must follow the previous activities
root.order.add_edge(inventory_sync, loop)
root.order.add_edge(procurement_plan, loop)
root.order.add_edge(production_align, loop)
root.order.add_edge(distribution_map, loop)

# Feedback Loop can optionally follow the loop
root.order.add_edge(loop, feedback_loop)

# Compliance Check must follow all other activities
root.order.add_edge(schedule_adjust, compliance_check)
root.order.add_edge(demand_update, compliance_check)
root.order.add_edge(delivery_track, compliance_check)
root.order.add_edge(compliance_check, compliance_check)  # self-loop for consistency

# Print the root model for verification
print(root)