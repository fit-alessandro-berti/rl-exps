import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the partial order structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, nutrient_mix, crop_rotate, waste_collect, compost_process])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[drone_dispatch, pest_control, pollination_run])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[volunteer_assign, feedback_gather])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[model_update, yield_forecast, water_adjust])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[report_generate, resource_audit, schedule_sync])

# Connect the loops
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)