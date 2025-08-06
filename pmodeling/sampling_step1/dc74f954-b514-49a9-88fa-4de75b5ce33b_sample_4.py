import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order graph
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    permit_filing,
    module_build,
    system_install,
    climate_setup,
    lighting_configure,
    irrigation_setup,
    nutrient_mix,
    pest_check,
    sensor_calibrate,
    data_integration,
    crop_planting,
    growth_monitor,
    yield_analyze,
    waste_manage,
    energy_audit
])

# Define the dependencies between the activities
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permit_filing)
root.order.add_edge(permit_filing, module_build)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(climate_setup, lighting_configure)
root.order.add_edge(lighting_configure, irrigation_setup)
root.order.add_edge(irrigation_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, pest_check)
root.order.add_edge(pest_check, sensor_calibrate)
root.order.add_edge(sensor_calibrate, data_integration)
root.order.add_edge(data_integration, crop_planting)
root.order.add_edge(crop_planting, growth_monitor)
root.order.add_edge(growth_monitor, yield_analyze)
root.order.add_edge(yield_analyze, waste_manage)
root.order.add_edge(waste_manage, energy_audit)

# Return the root of the POWL model
return root