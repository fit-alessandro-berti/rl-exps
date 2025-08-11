import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_filing])
loop_design_layout = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, permit_filing])
loop_module_build = OperatorPOWL(operator=Operator.LOOP, children=[module_build, permit_filing])
loop_system_install = OperatorPOWL(operator=Operator.LOOP, children=[system_install, permit_filing])
loop_climate_setup = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, permit_filing])
loop_lighting_configure = OperatorPOWL(operator=Operator.LOOP, children=[lighting_configure, permit_filing])
loop_irrigation_setup = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup, permit_filing])
loop_nutrient_mix = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, permit_filing])
loop_pest_check = OperatorPOWL(operator=Operator.LOOP, children=[pest_check, permit_filing])
loop_sensor_calibrate = OperatorPOWL(operator=Operator.LOOP, children=[sensor_calibrate, permit_filing])
loop_data_integration = OperatorPOWL(operator=Operator.LOOP, children=[data_integration, permit_filing])
loop_crop_planting = OperatorPOWL(operator=Operator.LOOP, children=[crop_planting, permit_filing])
loop_growth_monitor = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, permit_filing])
loop_yield_analyze = OperatorPOWL(operator=Operator.LOOP, children=[yield_analyze, permit_filing])
loop_waste_manage = OperatorPOWL(operator=Operator.LOOP, children=[waste_manage, permit_filing])
loop_energy_audit = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, permit_filing])

xor = OperatorPOWL(operator=Operator.XOR, children=[
    loop_site_survey, loop_design_layout, loop_module_build, loop_system_install, loop_climate_setup,
    loop_lighting_configure, loop_irrigation_setup, loop_nutrient_mix, loop_pest_check, loop_sensor_calibrate,
    loop_data_integration, loop_crop_planting, loop_growth_monitor, loop_yield_analyze, loop_waste_manage,
    loop_energy_audit
])

root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, xor)

print(root)