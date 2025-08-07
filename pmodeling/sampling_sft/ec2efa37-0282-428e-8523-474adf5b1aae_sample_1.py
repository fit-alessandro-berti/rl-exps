import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the loop body: IoT Monitor -> Risk Assess -> Maintenance Alert -> Feedback Loop
loop_body = StrictPartialOrder(nodes=[iot_monitor, risk_assess, maintenance_alert, feedback_loop])
loop_body.order.add_edge(iot_monitor, risk_assess)
loop_body.order.add_edge(risk_assess, maintenance_alert)
loop_body.order.add_edge(maintenance_alert, feedback_loop)

# Define the main process as a partial order
root = StrictPartialOrder(nodes=[
    quantum_init,
    data_ingest,
    ai_forecast,
    inventory_sync,
    procurement_plan,
    production_align,
    distribution_map,
    compliance_check,
    schedule_adjust,
    demand_update,
    delivery_track
])

# Add the initial control-flow edges
root.order.add_edge(quantum_init, data_ingest)
root.order.add_edge(data_ingest, ai_forecast)
root.order.add_edge(ai_forecast, inventory_sync)
root.order.add_edge(inventory_sync, procurement_plan)
root.order.add_edge(procurement_plan, production_align)
root.order.add_edge(production_align, distribution_map)
root.order.add_edge(distribution_map, compliance_check)
root.order.add_edge(compliance_check, schedule_adjust)
root.order.add_edge(schedule_adjust, demand_update)
root.order.add_edge(demand_update, delivery_track)

# Add the loop node: execute IoT Monitor, then optionally Risk Assess -> Maintenance Alert -> Feedback Loop and repeat
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[iot_monitor, loop_body])
root.order.add_edge(distribution_map, loop_node)

# Final edge to the end
root.order.add_edge(loop_node, delivery_track)

print(root)