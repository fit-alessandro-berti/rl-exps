import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define exclusive choice for nutrient mix and crop rotate
xor_nutrient_mix_crop_rotate = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, crop_rotate])

# Define loop for waste collect and compost process
loop_waste_collect_compost = OperatorPOWL(operator=Operator.LOOP, children=[waste_collect, compost_process])

# Define loop for drone dispatch and pest control
loop_drone_dispatch_pest_control = OperatorPOWL(operator=Operator.LOOP, children=[drone_dispatch, pest_control])

# Define loop for pollination run and volunteer assign
loop_pollination_run_volunteer_assign = OperatorPOWL(operator=Operator.LOOP, children=[pollination_run, volunteer_assign])

# Define loop for feedback gather and model update
loop_feedback_gather_model_update = OperatorPOWL(operator=Operator.LOOP, children=[feedback_gather, model_update])

# Define loop for yield forecast and water adjust
loop_yield_forecast_water_adjust = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, water_adjust])

# Define loop for report generate and resource audit
loop_report_generate_resource_audit = OperatorPOWL(operator=Operator.LOOP, children=[report_generate, resource_audit])

# Define loop for schedule sync
loop_schedule_sync = OperatorPOWL(operator=Operator.LOOP, children=[schedule_sync])

# Define the root process
root = StrictPartialOrder(nodes=[
    sensor_setup,
    data_capture,
    xor_nutrient_mix_crop_rotate,
    loop_waste_collect_compost,
    loop_drone_dispatch_pest_control,
    loop_pollination_run_volunteer_assign,
    loop_feedback_gather_model_update,
    loop_yield_forecast_water_adjust,
    loop_report_generate_resource_audit,
    loop_schedule_sync
])

# Add dependencies
root.order.add_edge(sensor_setup, data_capture)
root.order.add_edge(data_capture, xor_nutrient_mix_crop_rotate)
root.order.add_edge(xor_nutrient_mix_crop_rotate, loop_waste_collect_compost)
root.order.add_edge(loop_waste_collect_compost, loop_drone_dispatch_pest_control)
root.order.add_edge(loop_drone_dispatch_pest_control, loop_pollination_run_volunteer_assign)
root.order.add_edge(loop_pollination_run_volunteer_assign, loop_feedback_gather_model_update)
root.order.add_edge(loop_feedback_gather_model_update, loop_yield_forecast_water_adjust)
root.order.add_edge(loop_yield_forecast_water_adjust, loop_report_generate_resource_audit)
root.order.add_edge(loop_report_generate_resource_audit, loop_schedule_sync)

print(root)