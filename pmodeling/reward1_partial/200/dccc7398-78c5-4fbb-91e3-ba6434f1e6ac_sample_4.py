from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[permit_review, structure_build])
enviro_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[enviro_setup, nutrient_mix])
plant_robots_choice = OperatorPOWL(operator=Operator.XOR, children=[plant_robots, sensor_install])
data_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[data_sync, growth_monitor])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])
quality_check_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_check, market_launch])
feedback_loop_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, site_survey_choice])

root = StrictPartialOrder(nodes=[
    site_survey, design_draft, permit_review, structure_build, enviro_setup, nutrient_mix, seed_selection,
    plant_robots, sensor_install, data_sync, growth_monitor, pest_control, harvest_plan, quality_check,
    market_launch, feedback_loop_choice
])
root.order.add_edge(site_survey, site_survey_choice)
root.order.add_edge(design_draft, site_survey_choice)
root.order.add_edge(permit_review, enviro_setup_choice)
root.order.add_edge(structure_build, enviro_setup_choice)
root.order.add_edge(enviro_setup, plant_robots_choice)
root.order.add_edge(nutrient_mix, plant_robots_choice)
root.order.add_edge(plant_robots, data_sync_choice)
root.order.add_edge(sensor_install, data_sync_choice)
root.order.add_edge(data_sync, quality_check_choice)
root.order.add_edge(growth_monitor, quality_check_choice)
root.order.add_edge(pest_control, quality_check_choice)
root.order.add_edge(harvest_plan, quality_check_choice)
root.order.add_edge(quality_check, market_launch)
root.order.add_edge(market_launch, feedback_loop_choice)
root.order.add_edge(feedback_loop, site_survey_choice)