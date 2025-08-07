import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
soil_prep = Transition(label='Soil Prep')
hydroponic_setup = Transition(label='Hydroponic Setup')
community_meet = Transition(label='Community Meet')
crop_select = Transition(label='Crop Select')
sensor_install = Transition(label='Sensor Install')
water_testing = Transition(label='Water Testing')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
market_launch = Transition(label='Market Launch')
feedback_collect = Transition(label='Feedback Collect')

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, permit_review, design_layout, material_sourcing, soil_prep,
    hydroponic_setup, community_meet, crop_select, sensor_install, water_testing, pest_control,
    growth_monitor, harvest_plan, market_launch, feedback_collect
])

# Add dependencies between nodes if necessary
# For example, if the community meet must happen after site survey:
root.order.add_edge(site_survey, community_meet)

# If there are more dependencies, add them similarly

print(root)