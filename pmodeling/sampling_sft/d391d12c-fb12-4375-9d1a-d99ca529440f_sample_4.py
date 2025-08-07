import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
site_survey      = Transition(label='Site Survey')
climate_check    = Transition(label='Climate Check')
soil_testing     = Transition(label='Soil Testing')
media_select     = Transition(label='Media Select')
design_layout    = Transition(label='Design Layout')
hydro_setup      = Transition(label='Hydro Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
sensor_install   = Transition(label='Sensor Install')
regulation_review= Transition(label='Regulation Review')
permit_apply     = Transition(label='Permit Apply')
stakeholder_meet = Transition(label='Stakeholder Meet')
community_train  = Transition(label='Community Train')
plant_seed       = Transition(label='Plant Seed')
monitor_growth   = Transition(label='Monitor Growth')
adjust_controls  = Transition(label='Adjust Controls')
harvest_plan     = Transition(label='Harvest Plan')
waste_recycle    = Transition(label='Waste Recycle')
feedback_loop    = Transition(label='Feedback Loop')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, climate_check, soil_testing, media_select,
    design_layout, hydro_setup, nutrient_mix, sensor_install,
    regulation_review, permit_apply, stakeholder_meet, community_train,
    plant_seed, monitor_growth, adjust_controls, harvest_plan,
    waste_recycle, feedback_loop
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, climate_check)
root.order.add_edge(site_survey, soil_testing)
root.order.add_edge(climate_check, media_select)
root.order.add_edge(soil_testing, media_select)
root.order.add_edge(media_select, design_layout)
root.order.add_edge(design_layout, hydro_setup)
root.order.add_edge(design_layout, nutrient_mix)
root.order.add_edge(design_layout, sensor_install)
root.order.add_edge(hydro_setup, plant_seed)
root.order.add_edge(nutrient_mix, plant_seed)
root.order.add_edge(sensor_install, plant_seed)
root.order.add_edge(plant_seed, monitor_growth)
root.order.add_edge(monitor_growth, adjust_controls)
root.order.add_edge(adjust_controls, monitor_growth)
root.order.add_edge(adjust_controls, harvest_plan)
root.order.add_edge(harvest_plan, waste_recycle)
root.order.add_edge(waste_recycle, feedback_loop)

# Add optional compliance and community steps
root.order.add_edge(regulation_review, permit_apply)
root.order.add_edge(stakeholder_meet, community_train)

# Loop for continuous monitoring and adaptation
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, adjust_controls])

# Replace the inner sequence in the loop with the full monitoring+adjustment sequence
for child in loop.children:
    root.order.add_edge(monitor_growth, child)
    root.order.add_edge(adjust_controls, child)

# Final loop edge
root.order.add_edge(loop, waste_recycle)
root.order.add_edge(loop, feedback_loop)

# Final feedback edge
root.order.add_edge(feedback_loop, site_survey)

print(root)