import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loops and choices
# Site Survey -> Load Test -> Permit Review
site_survey_to_load_test = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, load_test, permit_review])
# Load Test -> Permit Review -> Design Layout
load_test_to_design_layout = OperatorPOWL(operator=Operator.LOOP, children=[load_test, permit_review, design_layout])
# Design Layout -> Material Sourcing -> Soil Prep
design_layout_to_material_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, material_sourcing, soil_prep])
# Material Sourcing -> Soil Prep -> Hydroponic Setup
material_sourcing_to_hydroponic_setup = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, soil_prep, hydroponic_setup])
# Soil Prep -> Hydroponic Setup -> Community Meet
soil_prep_to_community_meet = OperatorPOWL(operator=Operator.LOOP, children=[soil_prep, hydroponic_setup, community_meet])
# Hydroponic Setup -> Community Meet -> Crop Select
hydroponic_setup_to_crop_select = OperatorPOWL(operator=Operator.LOOP, children=[hydroponic_setup, community_meet, crop_select])
# Crop Select -> Sensor Install -> Water Testing
crop_select_to_sensor_install = OperatorPOWL(operator=Operator.LOOP, children=[crop_select, sensor_install, water_testing])
# Sensor Install -> Water Testing -> Pest Control
sensor_install_to_pest_control = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, water_testing, pest_control])
# Water Testing -> Pest Control -> Growth Monitor
water_testing_to_growth_monitor = OperatorPOWL(operator=Operator.LOOP, children=[water_testing, pest_control, growth_monitor])
# Pest Control -> Growth Monitor -> Harvest Plan
pest_control_to_harvest_plan = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, growth_monitor, harvest_plan])
# Growth Monitor -> Harvest Plan -> Market Launch
growth_monitor_to_market_launch = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, harvest_plan, market_launch])
# Harvest Plan -> Market Launch -> Feedback Collect
harvest_plan_to_feedback_collect = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, market_launch, feedback_collect])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    site_survey_to_load_test,
    load_test_to_design_layout,
    design_layout_to_material_sourcing,
    material_sourcing_to_hydroponic_setup,
    soil_prep_to_community_meet,
    hydroponic_setup_to_crop_select,
    crop_select_to_sensor_install,
    sensor_install_to_pest_control,
    water_testing_to_growth_monitor,
    pest_control_to_harvest_plan,
    growth_monitor_to_market_launch,
    harvest_plan_to_feedback_collect
])

# Define the partial order dependencies
root.order.add_edge(site_survey_to_load_test, load_test_to_design_layout)
root.order.add_edge(load_test_to_design_layout, design_layout_to_material_sourcing)
root.order.add_edge(design_layout_to_material_sourcing, material_sourcing_to_hydroponic_setup)
root.order.add_edge(material_sourcing_to_hydroponic_setup, soil_prep_to_community_meet)
root.order.add_edge(soil_prep_to_community_meet, hydroponic_setup_to_crop_select)
root.order.add_edge(hydroponic_setup_to_crop_select, crop_select_to_sensor_install)
root.order.add_edge(crop_select_to_sensor_install, sensor_install_to_pest_control)
root.order.add_edge(sensor_install_to_pest_control, water_testing_to_growth_monitor)
root.order.add_edge(water_testing_to_growth_monitor, pest_control_to_harvest_plan)
root.order.add_edge(pest_control_to_harvest_plan, growth_monitor_to_market_launch)
root.order.add_edge(growth_monitor_to_market_launch, harvest_plan_to_feedback_collect)