import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) for the process
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

# Define silent transitions for concurrency
skip = SilentTransition()

# Define partial order nodes
site_process = StrictPartialOrder(nodes=[site_survey, design_layout, permits_check])
frame_process = StrictPartialOrder(nodes=[foundation_prep, frame_assembly])
hydro_process = StrictPartialOrder(nodes=[hydro_setup, climate_setup])
seed_process = StrictPartialOrder(nodes=[seed_selection, nutrient_mix])
calibration_process = StrictPartialOrder(nodes=[system_calibration, pest_control])
automation_process = StrictPartialOrder(nodes=[automation_link, staff_training])
yield_process = StrictPartialOrder(nodes=[yield_tracking, distribution_plan])

# Define dependencies
site_process.order.add_edge(site_survey, design_layout)
site_process.order.add_edge(site_survey, permits_check)
frame_process.order.add_edge(foundation_prep, frame_assembly)
hydro_process.order.add_edge(hydro_setup, climate_setup)
seed_process.order.add_edge(seed_selection, nutrient_mix)
calibration_process.order.add_edge(system_calibration, pest_control)
automation_process.order.add_edge(automation_link, staff_training)
yield_process.order.add_edge(yield_tracking, distribution_plan)

# Define root node with concurrent nodes
root = StrictPartialOrder(nodes=[site_process, frame_process, hydro_process, seed_process, calibration_process, automation_process, yield_process])