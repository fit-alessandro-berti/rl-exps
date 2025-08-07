from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
climate_check = Transition(label='Climate Check')
soil_testing = Transition(label='Soil Testing')
media_select = Transition(label='Media Select')
design_layout = Transition(label='Design Layout')
hydro_setup = Transition(label='Hydro Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
regulation_review = Transition(label='Regulation Review')
permit_apply = Transition(label='Permit Apply')
stakeholder_meet = Transition(label='Stakeholder Meet')
community_train = Transition(label='Community Train')
plant_seed = Transition(label='Plant Seed')
monitor_growth = Transition(label='Monitor Growth')
adjust_controls = Transition(label='Adjust Controls')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
feedback_loop = Transition(label='Feedback Loop')

# Define the root node as a strict partial order with all activities
root = StrictPartialOrder(nodes=[
    site_survey, climate_check, soil_testing, media_select, design_layout,
    hydro_setup, nutrient_mix, sensor_install, regulation_review, permit_apply,
    stakeholder_meet, community_train, plant_seed, monitor_growth, adjust_controls,
    harvest_plan, waste_recycle, feedback_loop
])

# Define dependencies between activities
root.order.add_edge(site_survey, climate_check)
root.order.add_edge(site_survey, soil_testing)
root.order.add_edge(site_survey, media_select)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(climate_check, hydro_setup)
root.order.add_edge(climate_check, nutrient_mix)
root.order.add_edge(soil_testing, hydro_setup)
root.order.add_edge(soil_testing, nutrient_mix)
root.order.add_edge(media_select, design_layout)
root.order.add_edge(design_layout, hydro_setup)
root.order.add_edge(design_layout, nutrient_mix)
root.order.add_edge(sensor_install, regulation_review)
root.order.add_edge(sensor_install, permit_apply)
root.order.add_edge(stakeholder_meet, community_train)
root.order.add_edge(stakeholder_meet, plant_seed)
root.order.add_edge(monitor_growth, adjust_controls)
root.order.add_edge(monitor_growth, harvest_plan)
root.order.add_edge(monitor_growth, waste_recycle)
root.order.add_edge(feedback_loop, site_survey)
root.order.add_edge(feedback_loop, climate_check)
root.order.add_edge(feedback_loop, soil_testing)
root.order.add_edge(feedback_loop, media_select)
root.order.add_edge(feedback_loop, design_layout)
root.order.add_edge(feedback_loop, hydro_setup)
root.order.add_edge(feedback_loop, nutrient_mix)
root.order.add_edge(feedback_loop, sensor_install)
root.order.add_edge(feedback_loop, regulation_review)
root.order.add_edge(feedback_loop, permit_apply)
root.order.add_edge(feedback_loop, stakeholder_meet)
root.order.add_edge(feedback_loop, community_train)
root.order.add_edge(feedback_loop, plant_seed)
root.order.add_edge(feedback_loop, monitor_growth)
root.order.add_edge(feedback_loop, adjust_controls)
root.order.add_edge(feedback_loop, harvest_plan)
root.order.add_edge(feedback_loop, waste_recycle)

# The root node now represents the entire process