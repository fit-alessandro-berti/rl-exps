import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
enviro_design = Transition(label='Enviro Design')
hydro_setup = Transition(label='Hydro Setup')
aeroponics_add = Transition(label='Aeroponics Add')
lighting_procure = Transition(label='Lighting Procure')
water_recycle = Transition(label='Water Recycle')
rack_install = Transition(label='Rack Install')
seed_select = Transition(label='Seed Select')
germinate_seeds = Transition(label='Germinate Seeds')
nutrient_mix = Transition(label='Nutrient Mix')
staff_train = Transition(label='Staff Train')
pest_control = Transition(label='Pest Control')
pilot_crop = Transition(label='Pilot Crop')
data_gather = Transition(label='Data Gather')
yield_optimize = Transition(label='Yield Optimize')
skip = SilentTransition()

# Define the loop for the pilot crop cycle
loop = OperatorPOWL(operator=Operator.LOOP, children=[pilot_crop, yield_optimize])

# Define the XOR for the staff training and pest control
xor = OperatorPOWL(operator=Operator.XOR, children=[staff_train, pest_control])

# Define the root node with the loop and XOR
root = StrictPartialOrder(nodes=[loop, xor])

# Add edges for the dependencies
root.order.add_edge(loop, xor)

# Print the root node
print(root)