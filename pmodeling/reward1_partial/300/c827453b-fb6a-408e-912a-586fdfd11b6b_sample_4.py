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

# Define exclusive choice for nutrient mix and compost process
nutrient_compost_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, compost_process])

# Define loop for drone dispatch and pest control
drone_pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[drone_dispatch, pest_control])

# Define loop for volunteer assign and feedback gather
volunteer_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[volunteer_assign, feedback_gather])

# Define loop for model update and yield forecast
model_yield_loop = OperatorPOWL(operator=Operator.LOOP, children=[model_update, yield_forecast])

# Define loop for water adjust and report generate
water_report_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_adjust, report_generate])

# Define loop for resource audit and schedule sync
resource_schedule_loop = OperatorPOWL(operator=Operator.LOOP, children=[resource_audit, schedule_sync])

# Define root process
root = StrictPartialOrder(nodes=[sensor_setup, data_capture, nutrient_compost_choice, drone_pest_loop, volunteer_feedback_loop, model_yield_loop, water_report_loop, resource_schedule_loop])
root.order.add_edge(sensor_setup, data_capture)
root.order.add_edge(data_capture, nutrient_compost_choice)
root.order.add_edge(nutrient_compost_choice, drone_pest_loop)
root.order.add_edge(drone_pest_loop, volunteer_feedback_loop)
root.order.add_edge(volunteer_feedback_loop, model_yield_loop)
root.order.add_edge(model_yield_loop, water_report_loop)
root.order.add_edge(water_report_loop, resource_schedule_loop)