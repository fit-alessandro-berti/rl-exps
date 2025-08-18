import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Create the POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    design_draft,
    permit_review,
    structure_build,
    enviro_setup,
    nutrient_mix,
    seed_selection,
    plant_robots,
    sensor_install,
    data_sync,
    growth_monitor,
    pest_control,
    harvest_plan,
    quality_check,
    market_launch,
    feedback_loop
])

# Define the dependencies between activities
root.order.add_edge(site_survey, design_draft)
root.order.add_edge(design_draft, permit_review)
root.order.add_edge(permit_review, structure_build)
root.order.add_edge(structure_build, enviro_setup)
root.order.add_edge(enviro_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, plant_robots)
root.order.add_edge(plant_robots, sensor_install)
root.order.add_edge(sensor_install, data_sync)
root.order.add_edge(data_sync, growth_monitor)
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(pest_control, harvest_plan)
root.order.add_edge(harvest_plan, quality_check)
root.order.add_edge(quality_check, market_launch)
root.order.add_edge(market_launch, feedback_loop)

# Print the POWL model
print(root)