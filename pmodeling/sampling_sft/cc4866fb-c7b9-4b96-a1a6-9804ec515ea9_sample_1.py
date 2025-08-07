import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
design_planning  = Transition(label='Design Planning')
permit_filing    = Transition(label='Permit Filing')
structural_reinforce = Transition(label='Structural Reinforce')
hydroponic_setup  = Transition(label='Hydroponic Setup')
sensor_install    = Transition(label='Sensor Install')
energy_audit      = Transition(label='Energy Audit')
crop_selection    = Transition(label='Crop Selection')
nutrient_mix      = Transition(label='Nutrient Mix')
waste_process     = Transition(label='Waste Process')
climate_control   = Transition(label='Climate Control')
staff_training    = Transition(label='Staff Training')
market_study      = Transition(label='Market Study')
community_meet    = Transition(label='Community Meet')
launch_trial      = Transition(label='Launch Trial')
data_monitor      = Transition(label='Data Monitor')

# Define the loop body for continuous monitoring and data analysis
loop_body = StrictPartialOrder(nodes=[climate_control, staff_training, data_monitor])
loop_body.order.add_edge(climate_control, staff_training)
loop_body.order.add_edge(staff_training, data_monitor)

# Define the loop: do climate_control, then either exit or repeat loop_body and do climate_control again
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, loop_body])

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
    market_study,
    community_meet,
    launch_trial
])

# Add dependencies
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
root.order.add_edge(loop, market_study)
root.order.add_edge(market_study, community_meet)
root.order.add_edge(community_meet, launch_trial)