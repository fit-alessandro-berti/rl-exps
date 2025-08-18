import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model
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

# Define the dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, permits_check)
root.order.add_edge(permits_check, foundation_prep)
root.order.add_edge(foundation_prep, frame_assembly)
root.order.add_edge(frame_assembly, hydro_setup)
root.order.add_edge(hydro_setup, climate_setup)
root.order.add_edge(climate_setup, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, system_calibration)
root.order.add_edge(system_calibration, pest_control)
root.order.add_edge(pest_control, automation_link)
root.order.add_edge(automation_link, staff_training)
root.order.add_edge(staff_training, yield_tracking)
root.order.add_edge(yield_tracking, distribution_plan)

print(root)