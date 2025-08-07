import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey      = Transition(label='Site Survey')
design_planning  = Transition(label='Design Planning')
permit_filing    = Transition(label='Permit Filing')
structural_reinforce = Transition(label='Structural Reinforce')
hydroponic_setup = Transition(label='Hydroponic Setup')
sensor_install   = Transition(label='Sensor Install')
energy_audit     = Transition(label='Energy Audit')
crop_selection   = Transition(label='Crop Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
waste_process    = Transition(label='Waste Process')
climate_control  = Transition(label='Climate Control')
staff_training   = Transition(label='Staff Training')
market_study     = Transition(label='Market Study')
community_meet   = Transition(label='Community Meet')
launch_trial     = Transition(label='Launch Trial')
data_monitor     = Transition(label='Data Monitor')

# Build the loop body (trial + monitoring)
loop_body = StrictPartialOrder(nodes=[launch_trial, data_monitor])
loop_body.order.add_edge(launch_trial, data_monitor)

# LOOP: perform Site Survey -> Design Planning -> Permit Filing -> Structural Reinforce -> Hydroponic Setup -> Sensor Install -> Energy Audit
#       then optionally repeat: Crop Selection -> Nutrient Mix -> Waste Process -> Climate Control -> Staff Training -> Market Study -> Community Meet
#       and repeat the trial-monitoring cycle until exit
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[design_planning, loop_body]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_planning,
    permit_filing,
    structural_reinforce,
    hydroponic_setup,
    sensor_install,
    energy_audit,
    crop_selection,
    nutrient_mix,
    waste_process,
    climate_control,
    staff_training,
    market_study,
    community_meet,
    loop,
    data_monitor
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, design_planning)
root.order.add_edge(design_planning, permit_filing)
root.order.add_edge(permit_filing, structural_reinforce)
root.order.add_edge(structural_reinforce, hydroponic_setup)
root.order.add_edge(hydroponic_setup, sensor_install)
root.order.add_edge(sensor_install, energy_audit)
root.order.add_edge(energy_audit, crop_selection)
root.order.add_edge(crop_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, waste_process)
root.order.add_edge(waste_process, climate_control)
root.order.add_edge(climate_control, staff_training)
root.order.add_edge(staff_training, market_study)
root.order.add_edge(market_study, community_meet)
root.order.add_edge(community_meet, loop)
root.order.add_edge(loop, crop_selection)  # loop back to Crop Selection for another cycle
root.order.add_edge(loop, market_study)    # loop back to Market Study for another cycle
root.order.add_edge(loop, staff_training)  # loop back to Staff Training for another cycle
root.order.add_edge(loop, community_meet)  # loop back to Community Meet for another cycle
root.order.add_edge(loop, data_monitor)    # loop back to Data Monitor for another cycle