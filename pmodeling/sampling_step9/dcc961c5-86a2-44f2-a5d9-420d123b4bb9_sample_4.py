import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_acquire = Transition(label='Permit Acquire')
modular_build = Transition(label='Modular Build')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_automation = Transition(label='Seed Automation')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
sensor_install = Transition(label='Sensor Install')
growth_monitor = Transition(label='Growth Monitor')
waste_process = Transition(label='Waste Process')
data_analysis = Transition(label='Data Analysis')
staff_train = Transition(label='Staff Train')
community_link = Transition(label='Community Link')
yield_report = Transition(label='Yield Report')

# Define silent transitions
skip = SilentTransition()

# Define loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, permit_acquire])

# Define exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[modular_build, skip])

# Define POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the POWL model
print(root)