import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Loop for climate setup and light calibration
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, light_calibration])
# Loop for seedling preparation
seedling_loop = OperatorPOWL(operator=Operator.LOOP, children=[seedling_prep])

# XOR for nutrient mix and irrigation setup
nutrient_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, irrigation_setup])
# XOR for sensor install and data integration
sensor_xor = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, data_integration])

# XOR for waste routing and energy audit
waste_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_routing, energy_audit])
# XOR for regulation check and operational test
regulation_xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, operational_test])

# XOR for community outreach and operational test
community_xor = OperatorPOWL(operator=Operator.XOR, children=[community_outreach, operational_test])

# Loop for community outreach and operational test
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_outreach, operational_test])

# Construct the POWL model
root = StrictPartialOrder(nodes=[site_survey, design_layout, system_assembly, climate_loop, seedling_loop, nutrient_xor, sensor_xor, waste_xor, regulation_xor, community_xor, community_loop])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_assembly)
root.order.add_edge(system_assembly, climate_loop)
root.order.add_edge(system_assembly, seedling_loop)
root.order.add_edge(climate_loop, nutrient_xor)
root.order.add_edge(climate_loop, sensor_xor)
root.order.add_edge(seedling_loop, waste_xor)
root.order.add_edge(seedling_loop, regulation_xor)
root.order.add_edge(nutrient_xor, community_xor)
root.order.add_edge(sensor_xor, community_xor)
root.order.add_edge(waste_xor, regulation_xor)
root.order.add_edge(regulation_xor, community_loop)
root.order.add_edge(community_xor, community_loop)

print(root)