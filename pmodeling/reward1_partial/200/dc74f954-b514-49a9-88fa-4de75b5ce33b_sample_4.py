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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for nutrient delivery and pest check
nutrient_check = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, pest_check])

# Define loop for climate setup
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, lighting_configure, irrigation_setup])

# Define loop for sensor calibration
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_calibrate, data_integration])

# Define root partial order with all nodes and dependencies
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, permit_filing, module_build, system_install,
    climate_loop, nutrient_check, sensor_loop, crop_planting, growth_monitor,
    yield_analyze, waste_manage, energy_audit
])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(design_layout, module_build)
root.order.add_edge(module_build, system_install)
root.order.add_edge(system_install, climate_loop)
root.order.add_edge(climate_loop, nutrient_check)
root.order.add_edge(nutrient_check, sensor_loop)
root.order.add_edge(sensor_loop, crop_planting)
root.order.add_edge(crop_planting, growth_monitor)
root.order.add_edge(growth_monitor, yield_analyze)
root.order.add_edge(yield_analyze, waste_manage)
root.order.add_edge(waste_manage, energy_audit)