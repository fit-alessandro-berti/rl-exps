import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
sensor_setup        = Transition(label='Sensor Setup')
data_capture        = Transition(label='Data Capture')
nutrient_mix        = Transition(label='Nutrient Mix')
crop_rotate         = Transition(label='Crop Rotate')
waste_collect       = Transition(label='Waste Collect')
compost_process     = Transition(label='Compost Process')
drone_dispatch      = Transition(label='Drone Dispatch')
pest_control        = Transition(label='Pest Control')
pollination_run     = Transition(label='Pollination Run')
volunteer_assign    = Transition(label='Volunteer Assign')
feedback_gather     = Transition(label='Feedback Gather')
model_update        = Transition(label='Model Update')
yield_forecast      = Transition(label='Yield Forecast')
water_adjust        = Transition(label='Water Adjust')
report_generate     = Transition(label='Report Generate')
resource_audit      = Transition(label='Resource Audit')
schedule_sync       = Transition(label='Schedule Sync')

# Define the loop for continuous improvement: Model Update -> Yield Forecast -> Water Adjust -> Report Generate
improve_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[model_update, YieldForecast, water_adjust, report_generate]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    sensor_setup,
    data_capture,
    nutrient_mix,
    crop_rotate,
    waste_collect,
    compost_process,
    drone_dispatch,
    pest_control,
    pollination_run,
    volunteer_assign,
    feedback_gather,
    improve_loop,
    resource_audit,
    schedule_sync
])

# Sequential edges
root.order.add_edge(sensor_setup, data_capture)
root.order.add_edge(data_capture, nutrient_mix)
root.order.add_edge(nutrient_mix, crop_rotate)
root.order.add_edge(crop_rotate, waste_collect)
root.order.add_edge(waste_collect, compost_process)
root.order.add_edge(compost_process, drone_dispatch)
root.order.add_edge(drone_dispatch, pest_control)
root.order.add_edge(pest_control, pollination_run)
root.order.add_edge(pollination_run, volunteer_assign)
root.order.add_edge(volunteer_assign, feedback_gather)
root.order.add_edge(feedback_gather, improve_loop)

# Parallel edges for continuous improvement
root.order.add_edge(improve_loop, resource_audit)
root.order.add_edge(improve_loop, schedule_sync)