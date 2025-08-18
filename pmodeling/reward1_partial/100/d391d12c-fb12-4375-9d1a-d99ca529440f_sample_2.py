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

# Define exclusive choices
check_climate = OperatorPOWL(operator=Operator.XOR, children=[climate_check, skip])
check_soil = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, skip])
select_media = OperatorPOWL(operator=Operator.XOR, children=[media_select, skip])
setup_hydro = OperatorPOWL(operator=Operator.XOR, children=[hydro_setup, skip])
mix_nutrient = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
install_sensor = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
review_regulation = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, skip])
apply_permit = OperatorPOWL(operator=Operator.XOR, children=[permit_apply, skip])
meet_stakeholders = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip])
train_community = OperatorPOWL(operator=Operator.XOR, children=[community_train, skip])

# Define loops
grow_crops = OperatorPOWL(operator=Operator.LOOP, children=[plant_seed, monitor_growth, adjust_controls, harvest_plan])
monitor_environment = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle, feedback_loop])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, check_climate, check_soil, select_media, design_layout, setup_hydro, mix_nutrient, install_sensor, review_regulation, apply_permit, meet_stakeholders, train_community, grow_crops, monitor_environment])
root.order.add_edge(site_survey, check_climate)
root.order.add_edge(site_survey, check_soil)
root.order.add_edge(site_survey, select_media)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(check_climate, setup_hydro)
root.order.add_edge(check_soil, mix_nutrient)
root.order.add_edge(select_media, install_sensor)
root.order.add_edge(design_layout, review_regulation)
root.order.add_edge(review_regulation, apply_permit)
root.order.add_edge(apply_permit, meet_stakeholders)
root.order.add_edge(meet_stakeholders, train_community)
root.order.add_edge(train_community, grow_crops)
root.order.add_edge(grow_crops, monitor_environment)