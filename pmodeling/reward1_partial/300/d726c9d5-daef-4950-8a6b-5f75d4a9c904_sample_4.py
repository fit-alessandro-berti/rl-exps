from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
site_survey_and_structure_check = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structure_check])
soil_and_water_test = OperatorPOWL(operator=Operator.XOR, children=[soil_sample, water_test])
crop_and_material_order = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, material_order])
planter_and_irrigation_install = OperatorPOWL(operator=Operator.XOR, children=[planter_setup, irrigation_install])
sensor_and_solar_setup = OperatorPOWL(operator=Operator.XOR, children=[sensor_deploy, solar_setup])
data_and_community_meet = OperatorPOWL(operator=Operator.XOR, children=[data_integration, community_meet])
training_and_yield_monitor = OperatorPOWL(operator=Operator.XOR, children=[training_session, yield_monitor])
adjust_plan = Transition(label='Adjust Plan')

# Define the loop for the training and yield monitor
training_and_yield_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[training_and_yield_monitor, adjust_plan])

# Define the root
root = StrictPartialOrder(nodes=[site_survey_and_structure_check, soil_and_water_test, crop_and_material_order, planter_and_irrigation_install, sensor_and_solar_setup, data_and_community_meet, training_and_yield_monitor_loop])
root.order.add_edge(site_survey_and_structure_check, soil_and_water_test)
root.order.add_edge(soil_and_water_test, crop_and_material_order)
root.order.add_edge(crop_and_material_order, planter_and_irrigation_install)
root.order.add_edge(planter_and_irrigation_install, sensor_and_solar_setup)
root.order.add_edge(sensor_and_solar_setup, data_and_community_meet)
root.order.add_edge(data_and_community_meet, training_and_yield_monitor_loop)

# Print the root
print(root)