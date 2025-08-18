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

# Define the partial order
root = StrictPartialOrder(nodes=[site_analysis, structure_check, enviro_design, hydro_setup, aeroponics_add, lighting_procure, water_recycle, rack_install, seed_select, germinate_seeds, nutrient_mix, staff_train, pest_control, pilot_crop, data_gather, yield_optimize])

# Define the order of execution
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(site_analysis, enviro_design)
root.order.add_edge(site_analysis, hydro_setup)
root.order.add_edge(site_analysis, aeroponics_add)
root.order.add_edge(site_analysis, lighting_procure)
root.order.add_edge(site_analysis, water_recycle)
root.order.add_edge(site_analysis, rack_install)
root.order.add_edge(site_analysis, seed_select)
root.order.add_edge(site_analysis, germinate_seeds)
root.order.add_edge(site_analysis, nutrient_mix)
root.order.add_edge(site_analysis, staff_train)
root.order.add_edge(site_analysis, pest_control)
root.order.add_edge(site_analysis, pilot_crop)
root.order.add_edge(site_analysis, data_gather)
root.order.add_edge(site_analysis, yield_optimize)