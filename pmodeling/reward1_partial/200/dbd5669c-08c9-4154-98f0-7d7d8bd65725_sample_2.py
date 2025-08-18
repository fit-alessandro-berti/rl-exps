import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'Material Sourcing': Transition(label='Material Sourcing'),
    'Unit Assembly': Transition(label='Unit Assembly'),
    'System Wiring': Transition(label='System Wiring'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Water Testing': Transition(label='Water Testing'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Seed Selection': Transition(label='Seed Selection'),
    'Planting Setup': Transition(label='Planting Setup'),
    'Climate Control': Transition(label='Climate Control'),
    'Pest Management': Transition(label='Pest Management'),
    'Data Calibration': Transition(label='Data Calibration'),
    'Yield Analysis': Transition(label='Yield Analysis'),
    'Community Meet': Transition(label='Community Meet'),
    'Compliance Check': Transition(label='Compliance Check'),
    'Expansion Plan': Transition(label='Expansion Plan')
}

# Define the workflow
site_survey = activities['Site Survey']
design_layout = activities['Design Layout']
material_sourcing = activities['Material Sourcing']
unit_assembly = activities['Unit Assembly']
system_wiring = activities['System Wiring']
sensor_install = activities['Sensor Install']
water_testing = activities['Water Testing']
nutrient_mix = activities['Nutrient Mix']
seed_selection = activities['Seed Selection']
planting_setup = activities['Planting Setup']
climate_control = activities['Climate Control']
pest_management = activities['Pest Management']
data_calibration = activities['Data Calibration']
yield_analysis = activities['Yield Analysis']
community_meet = activities['Community Meet']
compliance_check = activities['Compliance Check']
expansion_plan = activities['Expansion Plan']

# Define the workflow structure
root = StrictPartialOrder(nodes=[site_survey, design_layout, material_sourcing, unit_assembly, system_wiring, sensor_install, water_testing, nutrient_mix, seed_selection, planting_setup, climate_control, pest_management, data_calibration, yield_analysis, community_meet, compliance_check, expansion_plan])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, material_sourcing)
root.order.add_edge(material_sourcing, unit_assembly)
root.order.add_edge(unit_assembly, system_wiring)
root.order.add_edge(system_wiring, sensor_install)
root.order.add_edge(sensor_install, water_testing)
root.order.add_edge(water_testing, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, planting_setup)
root.order.add_edge(planting_setup, climate_control)
root.order.add_edge(climate_control, pest_management)
root.order.add_edge(pest_management, data_calibration)
root.order.add_edge(data_calibration, yield_analysis)
root.order.add_edge(yield_analysis, community_meet)
root.order.add_edge(community_meet, compliance_check)
root.order.add_edge(compliance_check, expansion_plan)

# Print the root
print(root)