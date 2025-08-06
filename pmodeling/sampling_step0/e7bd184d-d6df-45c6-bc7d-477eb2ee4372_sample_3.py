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

# Define the workflow
loop = OperatorPOWL(operator=Operator.LOOP, children=[hydro_setup, aeroponics_add])
xor = OperatorPOWL(operator=Operator.XOR, children=[staff_train, pest_control])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pilot_crop, data_gather])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[yield_optimize, data_gather])

root = StrictPartialOrder(nodes=[site_analysis, structure_check, enviro_design, loop, xor, xor2, xor3, yield_optimize])
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(structure_check, enviro_design)
root.order.add_edge(enviro_design, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, yield_optimize)

# Print the root
print(root)