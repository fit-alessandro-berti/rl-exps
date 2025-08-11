import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_assembly = Transition(label='System Assembly')
climate_setup = Transition(label='Climate Setup')
light_calibration = Transition(label='Light Calibration')
seed_selection = Transition(label='Seed Selection')
seedling_prep = Transition(label='Seedling Prep')
nutrient_mix = Transition(label='Nutrient Mix')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
data_integration = Transition(label='Data Integration')
waste_routing = Transition(label='Waste Routing')
energy_audit = Transition(label='Energy Audit')
regulation_check = Transition(label='Regulation Check')
operational_test = Transition(label='Operational Test')
community_outreach = Transition(label='Community Outreach')

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the partial order nodes
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
loop_design_layout = OperatorPOWL(operator=Operator.LOOP, children=[design_layout])
loop_system_assembly = OperatorPOWL(operator=Operator.LOOP, children=[system_assembly])
loop_climate_setup = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup])
loop_light_calibration = OperatorPOWL(operator=Operator.LOOP, children=[light_calibration])
loop_seed_selection = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection])
loop_seedling_prep = OperatorPOWL(operator=Operator.LOOP, children=[seedling_prep])
loop_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])
loop_irrigation_setup = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup])
loop_sensor_install = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install])
loop_data_integration = OperatorPOWL(operator=Operator.LOOP, children=[data_integration])
loop_waste_routing = OperatorPOWL(operator=Operator.LOOP, children=[waste_routing])
loop_energy_audit = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit])
loop_regulation_check = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check])
loop_operational_test = OperatorPOWL(operator=Operator.LOOP, children=[operational_test])
loop_community_outreach = OperatorPOWL(operator=Operator.LOOP, children=[community_outreach])

# Define the partial order
root = StrictPartialOrder(nodes=[loop_site_survey, loop_design_layout, loop_system_assembly, loop_climate_setup, loop_light_calibration, loop_seed_selection, loop_seedling_prep, loop_nutrient_mix, loop_irrigation_setup, loop_sensor_install, loop_data_integration, loop_waste_routing, loop_energy_audit, loop_regulation_check, loop_operational_test, loop_community_outreach])

# Define the partial order dependencies
root.order.add_edge(loop_site_survey, loop_design_layout)
root.order.add_edge(loop_design_layout, loop_system_assembly)
root.order.add_edge(loop_system_assembly, loop_climate_setup)
root.order.add_edge(loop_climate_setup, loop_light_calibration)
root.order.add_edge(loop_light_calibration, loop_seed_selection)
root.order.add_edge(loop_seed_selection, loop_seedling_prep)
root.order.add_edge(loop_seedling_prep, loop_nutrient_mix)
root.order.add_edge(loop_nutrient_mix, loop_irrigation_setup)
root.order.add_edge(loop_irrigation_setup, loop_sensor_install)
root.order.add_edge(loop_sensor_install, loop_data_integration)
root.order.add_edge(loop_data_integration, loop_waste_routing)
root.order.add_edge(loop_waste_routing, loop_energy_audit)
root.order.add_edge(loop_energy_audit, loop_regulation_check)
root.order.add_edge(loop_regulation_check, loop_operational_test)
root.order.add_edge(loop_operational_test, loop_community_outreach)

# Print the root
print(root)