import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as Transition objects
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

# Define the root as a StrictPartialOrder
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

# The process flow is defined by the order of the nodes in the StrictPartialOrder
# Since there are no dependencies between the activities in this case, the order is sequential
# This is represented by adding edges between the nodes if there were dependencies

# Print the root model
print(root)