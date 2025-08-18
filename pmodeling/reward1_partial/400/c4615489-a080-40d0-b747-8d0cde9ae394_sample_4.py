import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define exclusive choices for each step
step1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structural_audit, permit_filing, design_layout])
step2 = OperatorPOWL(operator=Operator.XOR, children=[install_hvac, set_lighting, build_racks, install_hydroponics])
step3 = OperatorPOWL(operator=Operator.XOR, children=[configure_sensors, select_crops, seed_planting, monitor_growth])
step4 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mixing, staff_training, market_launch, waste_recycling])
step5 = OperatorPOWL(operator=Operator.XOR, children=[customer_onboarding])

# Define the partial order of activities
root = StrictPartialOrder(nodes=[step1, step2, step3, step4, step5])
root.order.add_edge(step1, step2)
root.order.add_edge(step2, step3)
root.order.add_edge(step3, step4)
root.order.add_edge(step4, step5)