import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sensor_setup = Transition(label='Sensor Setup')
data_capture = Transition(label='Data Capture')
nutrient_mix = Transition(label='Nutrient Mix')
crop_rotate = Transition(label='Crop Rotate')
waste_collect = Transition(label='Waste Collect')
compost_process = Transition(label='Compost Process')
drone_dispatch = Transition(label='Drone Dispatch')
pest_control = Transition(label='Pest Control')
pollination_run = Transition(label='Pollination Run')
volunteer_assign = Transition(label='Volunteer Assign')
feedback_gather = Transition(label='Feedback Gather')
model_update = Transition(label='Model Update')
yield_forecast = Transition(label='Yield Forecast')
water_adjust = Transition(label='Water Adjust')
report_generate = Transition(label='Report Generate')
resource_audit = Transition(label='Resource Audit')
schedule_sync = Transition(label='Schedule Sync')

# Define loops and choices
loop_sensor_data = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, data_capture])
loop_crop_rotation = OperatorPOWL(operator=Operator.LOOP, children=[crop_rotate, nutrient_mix])
loop_drone_delivery = OperatorPOWL(operator=Operator.LOOP, children=[drone_dispatch, pest_control, pollination_run])
loop_volunteer_scheduling = OperatorPOWL(operator=Operator.LOOP, children=[volunteer_assign, feedback_gather])
loop_model_updates = OperatorPOWL(operator=Operator.LOOP, children=[model_update, yield_forecast])
loop_resource_audit = OperatorPOWL(operator=Operator.LOOP, children=[resource_audit, schedule_sync])

# Define XORs
xor_waste_processing = OperatorPOWL(operator=Operator.XOR, children=[waste_collect, compost_process])
xor_drones = OperatorPOWL(operator=Operator.XOR, children=[drone_dispatch, drone_dispatch])
xor_resource_audit = OperatorPOWL(operator=Operator.XOR, children=[resource_audit, resource_audit])

# Define root
root = StrictPartialOrder(nodes=[loop_sensor_data, loop_crop_rotation, loop_drone_delivery, loop_volunteer_scheduling, loop_model_updates, loop_resource_audit, xor_waste_processing, xor_drones, xor_resource_audit])
root.order.add_edge(loop_sensor_data, loop_crop_rotation)
root.order.add_edge(loop_crop_rotation, loop_drone_delivery)
root.order.add_edge(loop_drone_delivery, loop_volunteer_scheduling)
root.order.add_edge(loop_volunteer_scheduling, loop_model_updates)
root.order.add_edge(loop_model_updates, loop_resource_audit)
root.order.add_edge(loop_resource_audit, xor_waste_processing)
root.order.add_edge(xor_waste_processing, xor_drones)
root.order.add_edge(xor_drones, xor_resource_audit)

print(root)