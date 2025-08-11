import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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
skip = SilentTransition()

# Define the loop for nutrient mixing
loop_nutrient_mixing = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mixing])

# Define the XOR for market launch strategies
xor_market_launch = OperatorPOWL(operator=Operator.XOR, children=[market_launch, skip])

# Define the XOR for customer onboarding strategies
xor_customer_onboarding = OperatorPOWL(operator=Operator.XOR, children=[customer_onboarding, skip])

# Define the XOR for waste recycling strategies
xor_waste_recycling = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, skip])

# Define the XOR for staff training strategies
xor_staff_training = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])

# Define the XOR for monitor growth strategies
xor_monitor_growth = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, skip])

# Define the XOR for nutrient mixing strategies
xor_nutrient_mixing = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mixing, skip])

# Define the XOR for seed planting strategies
xor_seed_planting = OperatorPOWL(operator=Operator.XOR, children=[seed_planting, skip])

# Define the XOR for select crops strategies
xor_select_crops = OperatorPOWL(operator=Operator.XOR, children=[select_crops, skip])

# Define the XOR for hydroponics installation strategies
xor_install_hydroponics = OperatorPOWL(operator=Operator.XOR, children=[install_hydroponics, skip])

# Define the XOR for sensor configuration strategies
xor_configure_sensors = OperatorPOWL(operator=Operator.XOR, children=[configure_sensors, skip])

# Define the XOR for lighting installation strategies
xor_set_lighting = OperatorPOWL(operator=Operator.XOR, children=[set_lighting, skip])

# Define the XOR for rack building strategies
xor_build_racks = OperatorPOWL(operator=Operator.XOR, children=[build_racks, skip])

# Define the XOR for HVAC installation strategies
xor_install_hvac = OperatorPOWL(operator=Operator.XOR, children=[install_hvac, skip])

# Define the XOR for design layout strategies
xor_design_layout = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])

# Define the XOR for permit filing strategies
xor_permit_filing = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])

# Define the XOR for structural audit strategies
xor_structural_audit = OperatorPOWL(operator=Operator.XOR, children=[structural_audit, skip])

# Define the XOR for site survey strategies
xor_site_survey = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])

# Define the XOR for all strategies
xor_all_strategies = OperatorPOWL(operator=Operator.XOR, children=[xor_site_survey, xor_structural_audit, xor_permit_filing, xor_design_layout, xor_install_hvac, xor_set_lighting, xor_build_racks, xor_install_hydroponics, xor_configure_sensors, xor_select_crops, xor_seed_planting, xor_monitor_growth, xor_nutrient_mixing, xor_staff_training, xor_customer_onboarding, xor_waste_recycling, xor_market_launch])

# Define the POWL model
root = StrictPartialOrder(nodes=[xor_all_strategies])
root.order.add_edge(xor_all_strategies, xor_site_survey)
root.order.add_edge(xor_all_strategies, xor_structural_audit)
root.order.add_edge(xor_all_strategies, xor_permit_filing)
root.order.add_edge(xor_all_strategies, xor_design_layout)
root.order.add_edge(xor_all_strategies, xor_install_hvac)
root.order.add_edge(xor_all_strategies, xor_set_lighting)
root.order.add_edge(xor_all_strategies, xor_build_racks)
root.order.add_edge(xor_all_strategies, xor_install_hydroponics)
root.order.add_edge(xor_all_strategies, xor_configure_sensors)
root.order.add_edge(xor_all_strategies, xor_select_crops)
root.order.add_edge(xor_all_strategies, xor_seed_planting)
root.order.add_edge(xor_all_strategies, xor_monitor_growth)
root.order.add_edge(xor_all_strategies, xor_nutrient_mixing)
root.order.add_edge(xor_all_strategies, xor_staff_training)
root.order.add_edge(xor_all_strategies, xor_customer_onboarding)
root.order.add_edge(xor_all_strategies, xor_waste_recycling)
root.order.add_edge(xor_all_strategies, xor_market_launch)