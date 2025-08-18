import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define the activities as transitions
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
permit_filing = Transition(label='Permit Filing')
design_layout = Transition(label='Design Layout')
install_hvac = Transition(label='Install HVAC')
set_lighting = Transition(label='Set Lighting')
build_racks = Transition(label='Build Racks')
install_hydroponics = Transition(label='Install Hydroponics')
configure_sensors = Transition(label='Configure Sensors')
select_crops = Transition(label='Select Crops')
seed_planting = Transition(label='Seed Planting')
monitor_growth = Transition(label='Monitor Growth')
nutrient_mixing = Transition(label='Nutrient Mixing')
staff_training = Transition(label='Staff Training')
market_launch = Transition(label='Market Launch')
waste_recycling = Transition(label='Waste Recycling')
customer_onboarding = Transition(label='Customer Onboarding')

# Add the activities to the root
root.add_node(site_survey)
root.add_node(structural_audit)
root.add_node(permit_filing)
root.add_node(design_layout)
root.add_node(install_hvac)
root.add_node(set_lighting)
root.add_node(build_racks)
root.add_node(install_hydroponics)
root.add_node(configure_sensors)
root.add_node(select_crops)
root.add_node(seed_planting)
root.add_node(monitor_growth)
root.add_node(nutrient_mixing)
root.add_node(staff_training)
root.add_node(market_launch)
root.add_node(waste_recycling)
root.add_node(customer_onboarding)

# Define the dependencies between activities
root.add_edge(site_survey, structural_audit)
root.add_edge(structural_audit, permit_filing)
root.add_edge(permit_filing, design_layout)
root.add_edge(design_layout, install_hvac)
root.add_edge(install_hvac, set_lighting)
root.add_edge(set_lighting, build_racks)
root.add_edge(build_racks, install_hydroponics)
root.add_edge(install_hydroponics, configure_sensors)
root.add_edge(configure_sensors, select_crops)
root.add_edge(select_crops, seed_planting)
root.add_edge(seed_planting, monitor_growth)
root.add_edge(monitor_growth, nutrient_mixing)
root.add_edge(nutrient_mixing, staff_training)
root.add_edge(staff_training, market_launch)
root.add_edge(market_launch, waste_recycling)
root.add_edge(waste_recycling, customer_onboarding)

# Print the root
print(root)