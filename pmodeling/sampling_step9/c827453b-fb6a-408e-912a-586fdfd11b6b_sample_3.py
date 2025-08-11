import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, data_capture])
crop_rotate_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_rotate, nutrient_mix])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, drone_dispatch])
pollination_run_loop = OperatorPOWL(operator=Operator.LOOP, children=[pollination_run, waste_collect])
volunteer_assign_loop = OperatorPOWL(operator=Operator.LOOP, children=[volunteer_assign, compost_process])
feedback_gather_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_gather, report_generate])
model_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[model_update, water_adjust])
yield_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, schedule_sync])

# Define partial order
root = StrictPartialOrder(nodes=[sensor_loop, crop_rotate_loop, pest_control_loop, pollination_run_loop, volunteer_assign_loop, feedback_gather_loop, model_update_loop, yield_forecast_loop])
root.order.add_edge(sensor_loop, crop_rotate_loop)
root.order.add_edge(crop_rotate_loop, nutrient_mix)
root.order.add_edge(pest_control_loop, drone_dispatch)
root.order.add_edge(pollination_run_loop, waste_collect)
root.order.add_edge(volunteer_assign_loop, compost_process)
root.order.add_edge(feedback_gather_loop, report_generate)
root.order.add_edge(model_update_loop, water_adjust)
root.order.add_edge(yield_forecast_loop, schedule_sync)

# Print the POWL model
print(root)