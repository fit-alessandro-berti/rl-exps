import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
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

# Define operators
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, module_build])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[system_install, climate_setup])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[lighting_configure, irrigation_setup])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, pest_check])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[sensor_calibrate, data_integration])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, growth_monitor])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, waste_manage])
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, exclusive_choice_1, exclusive_choice_2, exclusive_choice_3, exclusive_choice_4, exclusive_choice_5, exclusive_choice_6, exclusive_choice_7, exclusive_choice_8])
root.order.add_edge(site_survey, exclusive_choice_1)
root.order.add_edge(site_survey, exclusive_choice_2)
root.order.add_edge(site_survey, exclusive_choice_3)
root.order.add_edge(site_survey, exclusive_choice_4)
root.order.add_edge(site_survey, exclusive_choice_5)
root.order.add_edge(site_survey, exclusive_choice_6)
root.order.add_edge(site_survey, exclusive_choice_7)
root.order.add_edge(site_survey, exclusive_choice_8)