import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'System Assembly': Transition(label='System Assembly'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Light Calibration': Transition(label='Light Calibration'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Seedling Prep': Transition(label='Seedling Prep'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Irrigation Setup': Transition(label='Irrigation Setup'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Data Integration': Transition(label='Data Integration'),
    'Waste Routing': Transition(label='Waste Routing'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Regulation Check': Transition(label='Regulation Check'),
    'Operational Test': Transition(label='Operational Test'),
    'Community Outreach': Transition(label='Community Outreach')
}

# Define the control flow
site_survey = activities['Site Survey']
design_layout = activities['Design Layout']
system_assembly = activities['System Assembly']
climate_setup = activities['Climate Setup']
light_calibration = activities['Light Calibration']
seed_selection = activities['Seed Selection']
seedling_prep = activities['Seedling Prep']
nutrient_mix = activities['Nutrient Mix']
irrigation_setup = activities['Irrigation Setup']
sensor_install = activities['Sensor Install']
data_integration = activities['Data Integration']
waste_routing = activities['Waste Routing']
energy_audit = activities['Energy Audit']
regulation_check = activities['Regulation Check']
operational_test = activities['Operational Test']
community_outreach = activities['Community Outreach']

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, design_layout, system_assembly, climate_setup, light_calibration, seed_selection, seedling_prep, nutrient_mix, irrigation_setup, sensor_install, data_integration, waste_routing, energy_audit, regulation_check, operational_test, community_outreach])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_assembly)
root.order.add_edge(system_assembly, climate_setup)
root.order.add_edge(climate_setup, light_calibration)
root.order.add_edge(light_calibration, seed_selection)
root.order.add_edge(seed_selection, seedling_prep)
root.order.add_edge(seedling_prep, nutrient_mix)
root.order.add_edge(nutrient_mix, irrigation_setup)
root.order.add_edge(irrigation_setup, sensor_install)
root.order.add_edge(sensor_install, data_integration)
root.order.add_edge(data_integration, waste_routing)
root.order.add_edge(waste_routing, energy_audit)
root.order.add_edge(energy_audit, regulation_check)
root.order.add_edge(regulation_check, operational_test)
root.order.add_edge(operational_test, community_outreach)