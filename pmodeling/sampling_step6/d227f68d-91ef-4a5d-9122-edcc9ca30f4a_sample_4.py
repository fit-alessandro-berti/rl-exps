import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permits_check = Transition(label='Permits Check')
foundation_prep = Transition(label='Foundation Prep')
frame_assembly = Transition(label='Frame Assembly')
hydro_setup = Transition(label='Hydro Setup')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
system_calibration = Transition(label='System Calibration')
pest_control = Transition(label='Pest Control')
automation_link = Transition(label='Automation Link')
staff_training = Transition(label='Staff Training')
yield_tracking = Transition(label='Yield Tracking')
distribution_plan = Transition(label='Distribution Plan')

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    permits_check,
    foundation_prep,
    frame_assembly,
    hydro_setup,
    climate_setup,
    seed_selection,
    nutrient_mix,
    system_calibration,
    pest_control,
    automation_link,
    staff_training,
    yield_tracking,
    distribution_plan
])

# Add dependencies if any (this example doesn't have any explicit dependencies)
# For example, if Site Survey must come before Design Layout:
# root.order.add_edge(site_survey, design_layout)

# You can add dependencies like this:
# root.order.add_edge(site_survey, design_layout)

# Save the final result in the variable 'root'
print(root)