from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop and choice operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[pilot_crop, data_gather, yield_optimize])
xor = OperatorPOWL(operator=Operator.XOR, children=[staff_train, pest_control])

# Define the root model
root = StrictPartialOrder(nodes=[site_analysis, structure_check, enviro_design, hydro_setup, aeroponics_add, lighting_procure, water_recycle, rack_install, seed_select, germinate_seeds, nutrient_mix, loop, xor])
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(structure_check, enviro_design)
root.order.add_edge(enviro_design, hydro_setup)
root.order.add_edge(hydro_setup, aeroponics_add)
root.order.add_edge(aeroponics_add, lighting_procure)
root.order.add_edge(lighting_procure, water_recycle)
root.order.add_edge(water_recycle, rack_install)
root.order.add_edge(rack_install, seed_select)
root.order.add_edge(seed_select, germinate_seeds)
root.order.add_edge(germinate_seeds, nutrient_mix)
root.order.add_edge(nutrient_mix, loop)
root.order.add_edge(loop, xor)

# Print the root model
print(root)