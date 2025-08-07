import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
root = StrictPartialOrder()

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_frame = OperatorPOWL(operator=Operator.LOOP, children=[foundation_prep, frame_assembly])
loop_hydro = OperatorPOWL(operator=Operator.LOOP, children=[hydro_setup, system_calibration])
loop_pest = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, automation_link])

# Define exclusive choice nodes
exclusive_choice_layout = OperatorPOWL(operator=Operator.XOR, children=[design_layout, permits_check])
exclusive_choice_seed = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])
exclusive_choice_control = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])

# Define partial order
root.nodes.extend([site_survey, exclusive_choice_layout, loop_frame, exclusive_choice_seed, loop_hydro, exclusive_choice_control, staff_training, yield_tracking, distribution_plan])
root.order.add_edge(site_survey, exclusive_choice_layout)
root.order.add_edge(exclusive_choice_layout, loop_frame)
root.order.add_edge(loop_frame, exclusive_choice_seed)
root.order.add_edge(exclusive_choice_seed, loop_hydro)
root.order.add_edge(loop_hydro, exclusive_choice_control)
root.order.add_edge(exclusive_choice_control, staff_training)
root.order.add_edge(staff_training, yield_tracking)
root.order.add_edge(yield_tracking, distribution_plan)