import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
rack_design = Transition(label='Rack Design')
system_setup = Transition(label='System Setup')
climate_calibrate = Transition(label='Climate Calibrate')
nutrient_prep = Transition(label='Nutrient Prep')
crop_select = Transition(label='Crop Select')
seed_germinate = Transition(label='Seed Germinate')
sensor_deploy = Transition(label='Sensor Deploy')
pest_control = Transition(label='Pest Control')
harvest_automate = Transition(label='Harvest Automate')
quality_check = Transition(label='Quality Check')
pack_produce = Transition(label='Pack Produce')
data_analyze = Transition(label='Data Analyze')
engage_community = Transition(label='Engage Community')
logistics_plan = Transition(label='Logistics Plan')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
rack_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[rack_design])
system_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_setup])
climate_calibrate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_calibrate])
nutrient_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_prep])
crop_select_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_select])
seed_germinate_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_germinate])
sensor_deploy_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_deploy])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
harvest_automate_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_automate])
quality_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check])
pack_produce_loop = OperatorPOWL(operator=Operator.LOOP, children=[pack_produce])
data_analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze])
engage_community_loop = OperatorPOWL(operator=Operator.LOOP, children=[engage_community])
logistics_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan])

# Define partial order
root = StrictPartialOrder(nodes=[
    site_survey_loop,
    rack_design_loop,
    system_setup_loop,
    climate_calibrate_loop,
    nutrient_prep_loop,
    crop_select_loop,
    seed_germinate_loop,
    sensor_deploy_loop,
    pest_control_loop,
    harvest_automate_loop,
    quality_check_loop,
    pack_produce_loop,
    data_analyze_loop,
    engage_community_loop,
    logistics_plan_loop
])

# Add dependencies between nodes
root.order.add_edge(site_survey_loop, rack_design_loop)
root.order.add_edge(rack_design_loop, system_setup_loop)
root.order.add_edge(system_setup_loop, climate_calibrate_loop)
root.order.add_edge(climate_calibrate_loop, nutrient_prep_loop)
root.order.add_edge(nutrient_prep_loop, crop_select_loop)
root.order.add_edge(crop_select_loop, seed_germinate_loop)
root.order.add_edge(seed_germinate_loop, sensor_deploy_loop)
root.order.add_edge(sensor_deploy_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, harvest_automate_loop)
root.order.add_edge(harvest_automate_loop, quality_check_loop)
root.order.add_edge(quality_check_loop, pack_produce_loop)
root.order.add_edge(pack_produce_loop, data_analyze_loop)
root.order.add_edge(data_analyze_loop, engage_community_loop)
root.order.add_edge(engage_community_loop, logistics_plan_loop)

print(root)