import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the exclusive choice for environmental control
climate_light_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, light_calibration])

# Define the exclusive choice for seed selection and seedling preparation
seedling_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, seedling_prep])

# Define the loop for nutrient solution formulation and irrigation setup
nutrient_irrigation_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, irrigation_setup])

# Define the exclusive choice for sensor installation and data integration
sensor_data_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, data_integration])

# Define the loop for waste routing and energy audit
waste_energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_routing, energy_audit])

# Define the loop for operational test and community outreach
test_outreach_loop = OperatorPOWL(operator=Operator.LOOP, children=[operational_test, community_outreach])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, design_layout, system_assembly, climate_light_choice, seedling_choice, nutrient_irrigation_loop, sensor_data_choice, waste_energy_loop, test_outreach_loop])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_assembly)
root.order.add_edge(system_assembly, climate_light_choice)
root.order.add_edge(system_assembly, seedling_choice)
root.order.add_edge(climate_light_choice, nutrient_irrigation_loop)
root.order.add_edge(seedling_choice, sensor_data_choice)
root.order.add_edge(nutrient_irrigation_loop, waste_energy_loop)
root.order.add_edge(sensor_data_choice, test_outreach_loop)
root.order.add_edge(waste_energy_loop, test_outreach_loop)