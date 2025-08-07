import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_filing = Transition(label='Permit Filing')
module_build = Transition(label='Module Build')
system_install = Transition(label='System Install')
climate_setup = Transition(label='Climate Setup')
lighting_configure = Transition(label='Lighting Configure')
irrigation_setup = Transition(label='Irrigation Setup')
nutrient_mix = Transition(label='Nutrient Mix')
pest_check = Transition(label='Pest Check')
sensor_calibrate = Transition(label='Sensor Calibrate')
data_integration = Transition(label='Data Integration')
crop_planting = Transition(label='Crop Planting')
growth_monitor = Transition(label='Growth Monitor')
yield_analyze = Transition(label='Yield Analyze')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')

# Define the partial order model
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, permit_filing, module_build, system_install,
    climate_setup, lighting_configure, irrigation_setup, nutrient_mix,
    pest_check, sensor_calibrate, data_integration, crop_planting, growth_monitor,
    yield_analyze, waste_manage, energy_audit
])

# Define dependencies if any (if not, we assume the order is as defined above)
# Example: root.order.add_edge(site_survey, design_layout)
# Example: root.order.add_edge(design_layout, permit_filing)
# Example: root.order.add_edge(permit_filing, module_build)
# Example: root.order.add_edge(module_build, system_install)
# Example: root.order.add_edge(system_install, climate_setup)
# Example: root.order.add_edge(climate_setup, lighting_configure)
# Example: root.order.add_edge(lighting_configure, irrigation_setup)
# Example: root.order.add_edge(irrigation_setup, nutrient_mix)
# Example: root.order.add_edge(nutrient_mix, pest_check)
# Example: root.order.add_edge(pest_check, sensor_calibrate)
# Example: root.order.add_edge(sensor_calibrate, data_integration)
# Example: root.order.add_edge(data_integration, crop_planting)
# Example: root.order.add_edge(crop_planting, growth_monitor)
# Example: root.order.add_edge(growth_monitor, yield_analyze)
# Example: root.order.add_edge(yield_analyze, waste_manage)
# Example: root.order.add_edge(waste_manage, energy_audit)

# If no dependencies are defined, the process will follow the order of transitions defined above.