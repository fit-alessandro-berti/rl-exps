import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the workflow model
root = StrictPartialOrder(nodes=[
    site_survey,
    load_test,
    permit_review,
    design_layout,
    material_sourcing,
    soil_prep,
    hydroponic_setup,
    community_meet,
    crop_select,
    sensor_install,
    water_testing,
    pest_control,
    growth_monitor,
    harvest_plan,
    market_launch,
    feedback_collect
])

# Define the control flow
root.order.add_edge(site_survey, load_test)
root.order.add_edge(load_test, permit_review)
root.order.add_edge(permit_review, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, soil_prep)
root.order.add_edge(soil_prep, hydroponic_setup)
root.order.add_edge(hydroponic_setup, community_meet)
root.order.add_edge(community_meet, crop_select)
root.order.add_edge(crop_select, sensor_install)
root.order.add_edge(sensor_install, water_testing)
root.order.add_edge(water_testing, pest_control)
root.order.add_edge(pest_control, growth_monitor)
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(harvest_plan, market_launch)
root.order.add_edge(market_launch, feedback_collect)

# Print the workflow model
print(root)