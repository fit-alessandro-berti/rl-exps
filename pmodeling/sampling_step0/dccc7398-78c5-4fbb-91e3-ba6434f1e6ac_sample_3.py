from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_draft = Transition(label='Design Draft')
permit_review = Transition(label='Permit Review')
structure_build = Transition(label='Structure Build')
enviro_setup = Transition(label='Enviro Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
plant_robots = Transition(label='Plant Robots')
sensor_install = Transition(label='Sensor Install')
data_sync = Transition(label='Data Sync')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
quality_check = Transition(label='Quality Check')
market_launch = Transition(label='Market Launch')
feedback_loop = Transition(label='Feedback Loop')

# Define exclusive choices for coordinating activities
site_survey_to_design_draft = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_draft])
design_draft_to_permit_review = OperatorPOWL(operator=Operator.XOR, children=[design_draft, permit_review])
permit_review_to_structure_build = OperatorPOWL(operator=Operator.XOR, children=[permit_review, structure_build])
structure_build_to_enviro_setup = OperatorPOWL(operator=Operator.XOR, children=[structure_build, enviro_setup])
enviro_setup_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[enviro_setup, nutrient_mix])
nutrient_mix_to_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_selection])
seed_selection_to_plant_robots = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, plant_robots])
plant_robots_to_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[plant_robots, sensor_install])
sensor_install_to_data_sync = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, data_sync])
data_sync_to_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[data_sync, growth_monitor])
growth_monitor_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])
pest_control_to_harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])
harvest_plan_to_quality_check = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, quality_check])
quality_check_to_market_launch = OperatorPOWL(operator=Operator.XOR, children=[quality_check, market_launch])
market_launch_to_feedback_loop = OperatorPOWL(operator=Operator.XOR, children=[market_launch, feedback_loop])

# Define the root node with the activities and exclusive choices
root = StrictPartialOrder(nodes=[
    site_survey_to_design_draft,
    design_draft_to_permit_review,
    permit_review_to_structure_build,
    structure_build_to_enviro_setup,
    enviro_setup_to_nutrient_mix,
    nutrient_mix_to_seed_selection,
    seed_selection_to_plant_robots,
    plant_robots_to_sensor_install,
    sensor_install_to_data_sync,
    data_sync_to_growth_monitor,
    growth_monitor_to_pest_control,
    pest_control_to_harvest_plan,
    harvest_plan_to_quality_check,
    quality_check_to_market_launch,
    market_launch_to_feedback_loop
])

# Add edges to the partial order
root.order.add_edge(site_survey_to_design_draft, design_draft_to_permit_review)
root.order.add_edge(design_draft_to_permit_review, permit_review_to_structure_build)
root.order.add_edge(permit_review_to_structure_build, structure_build_to_enviro_setup)
root.order.add_edge(structure_build_to_enviro_setup, enviro_setup_to_nutrient_mix)
root.order.add_edge(enviro_setup_to_nutrient_mix, nutrient_mix_to_seed_selection)
root.order.add_edge(nutrient_mix_to_seed_selection, seed_selection_to_plant_robots)
root.order.add_edge(seed_selection_to_plant_robots, plant_robots_to_sensor_install)
root.order.add_edge(plant_robots_to_sensor_install, sensor_install_to_data_sync)
root.order.add_edge(sensor_install_to_data_sync, data_sync_to_growth_monitor)
root.order.add_edge(data_sync_to_growth_monitor, growth_monitor_to_pest_control)
root.order.add_edge(growth_monitor_to_pest_control, pest_control_to_harvest_plan)
root.order.add_edge(pest_control_to_harvest_plan, harvest_plan_to_quality_check)
root.order.add_edge(harvest_plan_to_quality_check, quality_check_to_market_launch)
root.order.add_edge(quality_check_to_market_launch, market_launch_to_feedback_loop)

# Print the root node
print(root)