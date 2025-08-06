import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loops
site_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_audit])
permit_loop = OperatorPOWL(operator=Operator.LOOP, children=[permit_filing])
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout])
build_loop = OperatorPOWL(operator=Operator.LOOP, children=[build_racks])
install_hvac_loop = OperatorPOWL(operator=Operator.LOOP, children=[install_hvac])
set_lighting_loop = OperatorPOWL(operator=Operator.LOOP, children=[set_lighting])
install_hydroponics_loop = OperatorPOWL(operator=Operator.LOOP, children=[install_hydroponics])
configure_sensors_loop = OperatorPOWL(operator=Operator.LOOP, children=[configure_sensors])
monitor_growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth])
nutrient_mixing_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mixing])
staff_training_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training])
market_launch_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_launch])
waste_recycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycling])
customer_onboarding_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_onboarding])

# Define exclusive choices
site_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[site_audit_loop, skip])
permit_choice = OperatorPOWL(operator=Operator.XOR, children=[permit_loop, skip])
design_choice = OperatorPOWL(operator=Operator.XOR, children=[design_loop, skip])
build_choice = OperatorPOWL(operator=Operator.XOR, children=[build_loop, skip])
install_hvac_choice = OperatorPOWL(operator=Operator.XOR, children=[install_hvac_loop, skip])
set_lighting_choice = OperatorPOWL(operator=Operator.XOR, children=[set_lighting_loop, skip])
install_hydroponics_choice = OperatorPOWL(operator=Operator.XOR, children=[install_hydroponics_loop, skip])
configure_sensors_choice = OperatorPOWL(operator=Operator.XOR, children=[configure_sensors_loop, skip])
monitor_growth_choice = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth_loop, skip])
nutrient_mixing_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mixing_loop, skip])
staff_training_choice = OperatorPOWL(operator=Operator.XOR, children=[staff_training_loop, skip])
market_launch_choice = OperatorPOWL(operator=Operator.XOR, children=[market_launch_loop, skip])
waste_recycling_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling_loop, skip])
customer_onboarding_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_onboarding_loop, skip])

# Define partial order
root = StrictPartialOrder(nodes=[site_audit_choice, permit_choice, design_choice, build_choice, install_hvac_choice, set_lighting_choice, install_hydroponics_choice, configure_sensors_choice, monitor_growth_choice, nutrient_mixing_choice, staff_training_choice, market_launch_choice, waste_recycling_choice, customer_onboarding_choice])
root.order.add_edge(site_audit_choice, permit_choice)
root.order.add_edge(permit_choice, design_choice)
root.order.add_edge(design_choice, build_choice)
root.order.add_edge(build_choice, install_hvac_choice)
root.order.add_edge(install_hvac_choice, set_lighting_choice)
root.order.add_edge(set_lighting_choice, install_hydroponics_choice)
root.order.add_edge(install_hydroponics_choice, configure_sensors_choice)
root.order.add_edge(configure_sensors_choice, monitor_growth_choice)
root.order.add_edge(monitor_growth_choice, nutrient_mixing_choice)
root.order.add_edge(nutrient_mixing_choice, staff_training_choice)
root.order.add_edge(staff_training_choice, market_launch_choice)
root.order.add_edge(market_launch_choice, waste_recycling_choice)
root.order.add_edge(waste_recycling_choice, customer_onboarding_choice)

# Print the POWL model
print(root)