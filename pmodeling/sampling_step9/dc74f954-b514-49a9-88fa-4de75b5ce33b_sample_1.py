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

# Define the silent transition (skip)
skip = SilentTransition()

# Define the loop for the system setup
system_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, lighting_configure, irrigation_setup, nutrient_mix, pest_check, sensor_calibrate, data_integration])

# Define the exclusive choice for the growth monitoring and yield analysis
monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, yield_analyze])

# Define the partial order with the loop and choice
root = StrictPartialOrder(nodes=[system_setup_loop, monitoring_choice])
root.order.add_edge(system_setup_loop, monitoring_choice)

print(root)