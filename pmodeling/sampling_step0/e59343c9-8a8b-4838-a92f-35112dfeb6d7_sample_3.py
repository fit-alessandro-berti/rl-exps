import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define loop nodes
structure_loop = OperatorPOWL(operator=Operator.LOOP, children=[structure_build, nutrient_prep])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, climate_setup])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, data_analyze, pest_control])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_crop, package_goods, ship_products])

# Define XOR nodes
seed_xor = OperatorPOWL(operator=Operator.XOR, children=[seed_select, skip])
germinate_xor = OperatorPOWL(operator=Operator.XOR, children=[germinate_seeds, skip])

# Define partial order
root = StrictPartialOrder(nodes=[structure_loop, sensor_loop, monitor_loop, harvest_loop, seed_xor, germinate_xor])
root.order.add_edge(structure_loop, sensor_loop)
root.order.add_edge(sensor_loop, monitor_loop)
root.order.add_edge(monitor_loop, harvest_loop)
root.order.add_edge(seed_xor, germinate_xor)
root.order.add_edge(germinate_xor, harvest_loop)

# Print the root
print(root)