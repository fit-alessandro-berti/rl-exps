import pm4py
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

# Define exclusive choice for stakeholder coordination and regulatory compliance checks
stakeholder_or_regulation = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, regulation_review])

# Define loop for continuous monitoring and adaptive management strategies
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, adjust_controls])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[site_survey, climate_check, soil_testing, media_select, design_layout, hydro_setup, nutrient_mix, sensor_install, stakeholder_or_regulation, permit_apply, community_train, plant_seed, monitoring_loop, harvest_plan, waste_recycle, feedback_loop])

# Define dependencies between nodes
root.order.add_edge(site_survey, climate_check)
root.order.add_edge(site_survey, soil_testing)
root.order.add_edge(climate_check, media_select)
root.order.add_edge(soil_testing, media_select)
root.order.add_edge(media_select, design_layout)
root.order.add_edge(design_layout, hydro_setup)
root.order.add_edge(hydro_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_install)
root.order.add_edge(sensor_install, stakeholder_or_regulation)
root.order.add_edge(stakeholder_or_regulation, permit_apply)
root.order.add_edge(permit_apply, community_train)
root.order.add_edge(community_train, plant_seed)
root.order.add_edge(plant_seed, monitoring_loop)
root.order.add_edge(monitoring_loop, harvest_plan)
root.order.add_edge(harvest_plan, waste_recycle)
root.order.add_edge(waste_recycle, feedback_loop)