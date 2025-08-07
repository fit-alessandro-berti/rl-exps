import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Loop for iterative climate control and data monitoring
loop_body = StrictPartialOrder(nodes=[climate_control, data_monitor])
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_body])

# Build the overall partial order
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
    loop,
    staff_training,
    market_study,
    community_meet,
    launch_trial
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
root.order.add_edge(waste_process, loop)
root.order.add_edge(loop, staff_training)
root.order.add_edge(staff_training, market_study)
root.order.add_edge(market_study, community_meet)
root.order.add_edge(community_meet, launch_trial)

# Final dependencies for iterative monitoring
root.order.add_edge(loop, data_monitor)

# Final dependencies for launching trial
root.order.add_edge(launch_trial, data_monitor)