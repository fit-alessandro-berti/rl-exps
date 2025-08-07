import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Loop for continuous monitoring & adaptive management
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_growth, adjust_controls]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, climate_check, soil_testing, media_select,
    design_layout, hydro_setup, nutrient_mix, sensor_install,
    regulation_review, permit_apply, stakeholder_meet,
    community_train, plant_seed, monitor_loop,
    harvest_plan, waste_recycle, feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, climate_check)
root.order.add_edge(site_survey, soil_testing)
root.order.add_edge(climate_check, media_select)
root.order.add_edge(soil_testing, media_select)
root.order.add_edge(media_select, design_layout)
root.order.add_edge(media_select, hydro_setup)
root.order.add_edge(media_select, nutrient_mix)
root.order.add_edge(media_select, sensor_install)
root.order.add_edge(design_layout, regulation_review)
root.order.add_edge(hydro_setup, regulation_review)
root.order.add_edge(nutrient_mix, regulation_review)
root.order.add_edge(sensor_install, regulation_review)
root.order.add_edge(regulation_review, permit_apply)
root.order.add_edge(permit_apply, stakeholder_meet)
root.order.add_edge(stakeholder_meet, community_train)
root.order.add_edge(community_train, plant_seed)
root.order.add_edge(plant_seed, monitor_loop)
root.order.add_edge(monitor_loop, harvest_plan)
root.order.add_edge(harvest_plan, waste_recycle)
root.order.add_edge(waste_recycle, feedback_loop)