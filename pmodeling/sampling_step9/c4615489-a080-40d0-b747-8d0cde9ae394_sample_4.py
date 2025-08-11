import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop nodes
loop_design_layout = OperatorPOWL(operator=Operator.LOOP, children=[structural_audit, permit_filing, design_layout])
loop_install_hvac = OperatorPOWL(operator=Operator.LOOP, children=[install_hvac, set_lighting])
loop_build_racks = OperatorPOWL(operator=Operator.LOOP, children=[build_racks, install_hydroponics])
loop_configure_sensors = OperatorPOWL(operator=Operator.LOOP, children=[configure_sensors, select_crops])
loop_seed_planting = OperatorPOWL(operator=Operator.LOOP, children=[seed_planting, monitor_growth, nutrient_mixing])
loop_staff_training = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, market_launch, waste_recycling, customer_onboarding])

# Define the XOR nodes
xor_market_launch = OperatorPOWL(operator=Operator.XOR, children=[market_launch, waste_recycling, customer_onboarding])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_design_layout, loop_install_hvac, loop_build_racks, loop_configure_sensors, loop_seed_planting, loop_staff_training, xor_market_launch])
root.order.add_edge(loop_design_layout, loop_install_hvac)
root.order.add_edge(loop_install_hvac, loop_build_racks)
root.order.add_edge(loop_build_racks, loop_configure_sensors)
root.order.add_edge(loop_configure_sensors, loop_seed_planting)
root.order.add_edge(loop_seed_planting, loop_staff_training)
root.order.add_edge(loop_staff_training, xor_market_launch)

print(root)