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

# Define the loops and choices
site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_filing])
design_layout_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, module_build])
system_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_install, climate_setup, lighting_configure, irrigation_setup, nutrient_mix, pest_check, sensor_calibrate, data_integration])
crop_planting_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_planting, growth_monitor, yield_analyze, waste_manage, energy_audit])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey_loop, design_layout_loop, system_install_loop, crop_planting_loop])
root.order.add_edge(site_survey_loop, design_layout_loop)
root.order.add_edge(site_survey_loop, system_install_loop)
root.order.add_edge(design_layout_loop, system_install_loop)
root.order.add_edge(system_install_loop, crop_planting_loop)
root.order.add_edge(crop_planting_loop, growth_monitor)
root.order.add_edge(crop_planting_loop, yield_analyze)
root.order.add_edge(crop_planting_loop, waste_manage)
root.order.add_edge(crop_planting_loop, energy_audit)