import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent activities
skip = SilentTransition()

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[pilot_crop, data_gather, yield_optimize])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[staff_train, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor])

# Add dependencies to the root POWL model
root.order.add_edge(loop, xor)

# Print the final POWL model
print(root)