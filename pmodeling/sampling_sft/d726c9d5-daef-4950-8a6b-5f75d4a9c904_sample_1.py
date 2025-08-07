import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
soil_sample     = Transition(label='Soil Sample')
water_test      = Transition(label='Water Test')
crop_selection  = Transition(label='Crop Selection')
material_order  = Transition(label='Material Order')
planter_setup   = Transition(label='Planter Setup')
irrigation_install = Transition(label='Irrigation Install')
sensor_deploy   = Transition(label='Sensor Deploy')
solar_setup     = Transition(label='Solar Setup')
data_integration = Transition(label='Data Integration')
community_meet  = Transition(label='Community Meet')
training_session= Transition(label='Training Session')
yield_monitor   = Transition(label='Yield Monitor')
adjust_plan     = Transition(label='Adjust Plan')

# Define the choice for either community engagement or training
community_choice = OperatorPOWL(operator=Operator.XOR, children=[community_meet, training_session])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, structure_check, soil_sample, water_test,
    crop_selection, material_order, planter_setup,
    irrigation_install, sensor_deploy, solar_setup,
    data_integration, community_choice,
    yield_monitor, adjust_plan
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structure_check)
root.order.add_edge(site_survey, soil_sample)
root.order.add_edge(structure_check, water_test)
root.order.add_edge(soil_sample, water_test)
root.order.add_edge(water_test, crop_selection)
root.order.add_edge(crop_selection, material_order)
root.order.add_edge(material_order, planter_setup)
root.order.add_edge(planter_setup, irrigation_install)
root.order.add_edge(irrigation_install, sensor_deploy)
root.order.add_edge(sensor_deploy, solar_setup)
root.order.add_edge(solar_setup, data_integration)
root.order.add_edge(data_integration, community_choice)
root.order.add_edge(community_choice, yield_monitor)
root.order.add_edge(yield_monitor, adjust_plan)

print(root)