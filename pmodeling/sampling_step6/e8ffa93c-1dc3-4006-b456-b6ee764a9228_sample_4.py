import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
env_analysis = Transition(label='Env Analysis')
structure_build = Transition(label='Structure Build')
hydroponics_fit = Transition(label='Hydroponics Fit')
nutrient_mix = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
energy_audit = Transition(label='Energy Audit')
crop_select = Transition(label='Crop Select')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
community_meet = Transition(label='Community Meet')
supply_sync = Transition(label='Supply Sync')
data_review = Transition(label='Data Review')

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    env_analysis,
    structure_build,
    hydroponics_fit,
    nutrient_mix,
    climate_setup,
    energy_audit,
    crop_select,
    pest_control,
    growth_monitor,
    harvest_plan,
    waste_recycle,
    community_meet,
    supply_sync,
    data_review
])

# Print the root of the POWL model
print(root)