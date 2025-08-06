import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.petri_net.obj import PetriNet
from pm4py.objects.petri_net.utils import petri_utils

# Define the transitions for each activity
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

# Define the silent transitions (if any)
skip = SilentTransition()

# Define the loop for the design process
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, structural_audit, permit_filing])

# Define the XOR for the installation process
install_xor = OperatorPOWL(operator=Operator.XOR, children=[install_hvac, set_lighting, build_racks])

# Define the XOR for the hydroponic system installation
hydroponics_xor = OperatorPOWL(operator=Operator.XOR, children=[install_hydroponics, configure_sensors])

# Define the XOR for the crop selection and planting
crop_xor = OperatorPOWL(operator=Operator.XOR, children=[select_crops, seed_planting])

# Define the XOR for the monitoring and nutrient mixing
monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, nutrient_mixing])

# Define the XOR for the staff training and market launch
staff_xor = OperatorPOWL(operator=Operator.XOR, children=[staff_training, market_launch])

# Define the XOR for the waste recycling and customer onboarding
recycle_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, customer_onboarding])

# Define the root POWL model
root = StrictPartialOrder(nodes=[design_loop, install_xor, hydroponics_xor, crop_xor, monitor_xor, staff_xor, recycle_xor])
root.order.add_edge(design_loop, install_xor)
root.order.add_edge(install_xor, hydroponics_xor)
root.order.add_edge(hydroponics_xor, crop_xor)
root.order.add_edge(crop_xor, monitor_xor)
root.order.add_edge(monitor_xor, staff_xor)
root.order.add_edge(staff_xor, recycle_xor)