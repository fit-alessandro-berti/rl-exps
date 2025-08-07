import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey       = Transition(label='Site Survey')
climate_check     = Transition(label='Climate Check')
soil_testing      = Transition(label='Soil Testing')
media_select      = Transition(label='Media Select')
design_layout     = Transition(label='Design Layout')
hydro_setup       = Transition(label='Hydro Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
sensor_install    = Transition(label='Sensor Install')
regulation_review = Transition(label='Regulation Review')
permit_apply      = Transition(label='Permit Apply')
stakeholder_meet  = Transition(label='Stakeholder Meet')
community_train   = Transition(label='Community Train')
plant_seed        = Transition(label='Plant Seed')
monitor_growth    = Transition(label='Monitor Growth')
adjust_controls   = Transition(label='Adjust Controls')
harvest_plan      = Transition(label='Harvest Plan')
waste_recycle     = Transition(label='Waste Recycle')
feedback_loop     = Transition(label='Feedback Loop')

# Define the monitoring & adaptive branch: Monitor Growth -> Adjust Controls -> repeat
monitor_adapt = StrictPartialOrder(nodes=[monitor_growth, adjust_controls])
monitor_adapt.order.add_edge(monitor_growth, adjust_controls)

# Define the loop: do Plant Seed, then optionally repeat Monitor_Adapt then Plant Seed
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[plant_seed, monitor_adapt])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, climate_check, soil_testing, media_select, design_layout,
    hydro_setup, nutrient_mix, sensor_install, regulation_review, permit_apply,
    stakeholder_meet, community_train, monitor_loop, harvest_plan,
    waste_recycle, feedback_loop
])

# Define the sequence and loop dependencies
root.order.add_edge(site_survey, climate_check)
root.order.add_edge(climate_check, soil_testing)
root.order.add_edge(soil_testing, media_select)
root.order.add_edge(media_select, design_layout)
root.order.add_edge(design_layout, hydro_setup)
root.order.add_edge(hydro_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_install)
root.order.add_edge(sensor_install, regulation_review)
root.order.add_edge(regulation_review, permit_apply)
root.order.add_edge(permit_apply, stakeholder_meet)
root.order.add_edge(stakeholder_meet, community_train)
root.order.add_edge(community_train, monitor_loop)
root.order.add_edge(monitor_loop, harvest_plan)
root.order.add_edge(harvest_plan, waste_recycle)
root.order.add_edge(waste_recycle, feedback_loop)