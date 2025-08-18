import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
soil_sample = Transition(label='Soil Sample')
water_test = Transition(label='Water Test')
crop_selection = Transition(label='Crop Selection')
material_order = Transition(label='Material Order')
planter_setup = Transition(label='Planter Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy = Transition(label='Sensor Deploy')
solar_setup = Transition(label='Solar Setup')
data_integration = Transition(label='Data Integration')
community_meet = Transition(label='Community Meet')
training_session = Transition(label='Training Session')
yield_monitor = Transition(label='Yield Monitor')
adjust_plan = Transition(label='Adjust Plan')

# Define silent transitions
skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, adjust_plan])
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structure_check, soil_sample, water_test, crop_selection, material_order, planter_setup, irrigation_install, sensor_deploy, solar_setup, data_integration, community_meet, training_session, yield_monitor])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[exclusive_choice, xor])
root.order.add_edge(exclusive_choice, xor)

# Print the root
print(root)