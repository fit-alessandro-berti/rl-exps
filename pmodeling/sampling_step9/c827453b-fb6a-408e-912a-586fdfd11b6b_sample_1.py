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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_sensor_setup = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, data_capture])
loop_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, crop_rotate])
loop_waste_collect = OperatorPOWL(operator=Operator.LOOP, children=[waste_collect, compost_process])
loop_drone_dispatch = OperatorPOWL(operator=Operator.LOOP, children=[drone_dispatch, pest_control])
loop_pollination_run = OperatorPOWL(operator=Operator.LOOP, children=[pollination_run, volunteer_assign])
loop_feedback_gather = OperatorPOWL(operator=Operator.LOOP, children=[feedback_gather, model_update])
loop_yield_forecast = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, water_adjust])
loop_report_generate = OperatorPOWL(operator=Operator.LOOP, children=[report_generate, resource_audit])
loop_schedule_sync = OperatorPOWL(operator=Operator.LOOP, children=[schedule_sync, drone_dispatch])

# Define exclusive choices
xor_sensor_setup = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_sensor_setup])
xor_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_nutrient_mix])
xor_waste_collect = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_waste_collect])
xor_drone_dispatch = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_drone_dispatch])
xor_pollination_run = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_pollination_run])
xor_feedback_gather = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_feedback_gather])
xor_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_yield_forecast])
xor_report_generate = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_report_generate])
xor_schedule_sync = OperatorPOWL(operator=Operator.XOR, children=[skip, loop_schedule_sync])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor_sensor_setup, xor_nutrient_mix, xor_waste_collect, xor_drone_dispatch, xor_pollination_run, xor_feedback_gather, xor_yield_forecast, xor_report_generate, xor_schedule_sync])
root.order.add_edge(xor_sensor_setup, loop_sensor_setup)
root.order.add_edge(xor_nutrient_mix, loop_nutrient_mix)
root.order.add_edge(xor_waste_collect, loop_waste_collect)
root.order.add_edge(xor_drone_dispatch, loop_drone_dispatch)
root.order.add_edge(xor_pollination_run, loop_pollination_run)
root.order.add_edge(xor_feedback_gather, loop_feedback_gather)
root.order.add_edge(xor_yield_forecast, loop_yield_forecast)
root.order.add_edge(xor_report_generate, loop_report_generate)
root.order.add_edge(xor_schedule_sync, loop_schedule_sync)