import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the dependencies
# Site Survey
root = StrictPartialOrder(nodes=[site_survey])
root.order.add_edge(site_survey, design_layout)

# Design Layout
root.order.add_edge(design_layout, permit_filing)

# Permit Filing
root.order.add_edge(permit_filing, module_build)

# Module Build
root.order.add_edge(module_build, system_install)

# System Install
root.order.add_edge(system_install, climate_setup)

# Climate Setup
root.order.add_edge(climate_setup, lighting_configure)

# Lighting Configure
root.order.add_edge(lighting_configure, irrigation_setup)

# Irrigation Setup
root.order.add_edge(irrigation_setup, nutrient_mix)

# Nutrient Mix
root.order.add_edge(nutrient_mix, pest_check)

# Pest Check
root.order.add_edge(pest_check, sensor_calibrate)

# Sensor Calibrate
root.order.add_edge(sensor_calibrate, data_integration)

# Data Integration
root.order.add_edge(data_integration, crop_planting)

# Crop Planting
root.order.add_edge(crop_planting, growth_monitor)

# Growth Monitor
root.order.add_edge(growth_monitor, yield_analyze)

# Yield Analyze
root.order.add_edge(yield_analyze, waste_manage)

# Waste Manage
root.order.add_edge(waste_manage, energy_audit)

# Energy Audit
root.order.add_edge(energy_audit, root)  # Assuming the energy audit leads back to the root (or start)