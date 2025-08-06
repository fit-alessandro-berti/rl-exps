from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

A = Transition(label='Site Survey')
B = Transition(label='Design Layout')
C = Transition(label='System Assembly')
D = Transition(label='Climate Setup')
E = Transition(label='Light Calibration')
F = Transition(label='Seed Selection')
G = Transition(label='Seedling Prep')
H = Transition(label='Nutrient Mix')
I = Transition(label='Irrigation Setup')
J = Transition(label='Sensor Install')
K = Transition(label='Data Integration')
L = Transition(label='Waste Routing')
M = Transition(label='Energy Audit')
N = Transition(label='Regulation Check')
O = Transition(label='Operational Test')
P = Transition(label='Community Outreach')

skip = SilentTransition()

# Site Survey
# Design Layout
site_survey_design_layout = OperatorPOWL(operator=OperatorPOWL.XOR, children=[A, B])
# System Assembly
# Climate Setup
climate_setup = OperatorPOWL(operator=OperatorPOWL.XOR, children=[C, D])
# Light Calibration
# Seed Selection
seed_selection = OperatorPOWL(operator=OperatorPOWL.XOR, children=[E, F])
# Seedling Prep
# Nutrient Mix
nutrient_mix = OperatorPOWL(operator=OperatorPOWL.XOR, children=[H, G])
# Irrigation Setup
# Sensor Install
sensor_install = OperatorPOWL(operator=OperatorPOWL.XOR, children=[I, J])
# Data Integration
# Waste Routing
waste_routing = OperatorPOWL(operator=OperatorPOWL.XOR, children=[L, K])
# Energy Audit
# Regulation Check
energy_audit_regulation_check = OperatorPOWL(operator=OperatorPOWL.XOR, children=[M, N])
# Operational Test
# Community Outreach
operational_test_community_outreach = OperatorPOWL(operator=OperatorPOWL.XOR, children=[O, P])

root = StrictPartialOrder(nodes=[site_survey_design_layout, climate_setup, seed_selection, nutrient_mix, sensor_install, waste_routing, energy_audit_regulation_check, operational_test_community_outreach])
root.order.add_edge(site_survey_design_layout, climate_setup)
root.order.add_edge(site_survey_design_layout, seed_selection)
root.order.add_edge(climate_setup, nutrient_mix)
root.order.add_edge(climate_setup, sensor_install)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(seed_selection, sensor_install)
root.order.add_edge(nutrient_mix, waste_routing)
root.order.add_edge(nutrient_mix, energy_audit_regulation_check)
root.order.add_edge(sensor_install, waste_routing)
root.order.add_edge(sensor_install, energy_audit_regulation_check)
root.order.add_edge(waste_routing, operational_test_community_outreach)
root.order.add_edge(energy_audit_regulation_check, operational_test_community_outreach)