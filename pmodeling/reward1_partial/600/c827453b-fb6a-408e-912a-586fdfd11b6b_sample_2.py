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

# Define exclusive choice for nutrient mix and waste collect
nutrient_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, waste_collect])

# Define loop for nutrient mix and waste collect
nutrient_waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_waste_choice])

# Define loop for drone dispatch and pest control
drone_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[drone_dispatch, pest_control])

# Define loop for pollination run and volunteer assign
pollination_volunteer_loop = OperatorPOWL(operator=Operator.LOOP, children=[pollination_run, volunteer_assign])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[sensor_setup, data_capture, nutrient_waste_loop, crop_rotate, compost_process, drone_pest_loop, pollination_volunteer_loop, feedback_gather, model_update, yield_forecast, water_adjust, report_generate, resource_audit, schedule_sync])

# Add edges between nodes
root.order.add_edge(sensor_setup, data_capture)
root.order.add_edge(data_capture, nutrient_waste_loop)
root.order.add_edge(nutrient_waste_loop, crop_rotate)
root.order.add_edge(crop_rotate, compost_process)
root.order.add_edge(compost_process, drone_pest_loop)
root.order.add_edge(drone_pest_loop, pollination_volunteer_loop)
root.order.add_edge(pollination_volunteer_loop, feedback_gather)
root.order.add_edge(feedback_gather, model_update)
root.order.add_edge(model_update, yield_forecast)
root.order.add_edge(yield_forecast, water_adjust)
root.order.add_edge(water_adjust, report_generate)
root.order.add_edge(report_generate, resource_audit)
root.order.add_edge(resource_audit, schedule_sync)