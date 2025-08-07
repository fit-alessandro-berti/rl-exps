import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    site_analysis,
    structure_check,
    enviro_design,
    hydro_setup,
    aeroponics_add,
    lighting_procure,
    water_recycle,
    rack_install,
    seed_select,
    germinate_seeds,
    nutrient_mix,
    staff_train,
    pest_control,
    pilot_crop,
    data_gather,
    yield_optimize
])

# Add dependencies between activities
# The actual dependencies would need to be determined based on the process flow
# For simplicity, let's assume the activities are independent for this example
# If there were dependencies, they would be added here like so:
# root.order.add_edge(site_analysis, structure_check)
# root.order.add_edge(site_analysis, enviro_design)
# And so on...

# Save the final result in the variable 'root'
print(root)