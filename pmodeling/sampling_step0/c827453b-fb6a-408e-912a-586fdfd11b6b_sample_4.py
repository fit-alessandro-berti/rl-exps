import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, data_capture])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[crop_rotate, waste_collect])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[compost_process, skip])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[drone_dispatch, pest_control])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[pollination_run, skip])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[volunteer_assign, feedback_gather])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[model_update, skip])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, water_adjust])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[report_generate, skip])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[resource_audit, schedule_sync])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[skip, skip])

# Create the root node
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, loop4, xor4, loop5, xor5, loop6, xor6])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, xor5)
root.order.add_edge(loop6, xor6)

# Return the root node
return root