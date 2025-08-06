from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
permit_approval = Transition(label='Permit Approval')
design_layout = Transition(label='Design Layout')
system_procure = Transition(label='System Procure')
nutrient_prep = Transition(label='Nutrient Prep')
structure_build = Transition(label='Structure Build')
sensor_install = Transition(label='Sensor Install')
climate_setup = Transition(label='Climate Setup')
seed_select = Transition(label='Seed Select')
germinate_seeds = Transition(label='Germinate Seeds')
monitor_growth = Transition(label='Monitor Growth')
data_analyze = Transition(label='Data Analyze')
pest_control = Transition(label='Pest Control')
harvest_crop = Transition(label='Harvest Crop')
package_goods = Transition(label='Package Goods')
ship_products = Transition(label='Ship Products')

# Define the silent transition for loop
skip = SilentTransition()

# Define the exclusive choice (XOR) between nutrient prep and skip
xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, skip])

# Define the loop (A, B) for structure build and sensor install
loop = OperatorPOWL(operator=Operator.LOOP, children=[structure_build, sensor_install])

# Define the partial order
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root
print(root)