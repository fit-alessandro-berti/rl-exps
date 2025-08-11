import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define activities as transitions
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
layout_design = Transition(label='Layout Design')
system_install = Transition(label='System Install')
climate_setup = Transition(label='Climate Setup')
water_testing = Transition(label='Water Testing')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_prep = Transition(label='Planting Prep')
growth_monitor = Transition(label='Growth Monitor')
pest_inspect = Transition(label='Pest Inspect')
harvest_plan = Transition(label='Harvest Plan')
packaging_prep = Transition(label='Packaging Prep')
distribution = Transition(label='Distribution')
sustainability = Transition(label='Sustainability')

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the POWL model structure
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[system_install, climate_setup, water_testing, nutrient_mix, seed_selection])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[planting_prep, growth_monitor, pest_inspect, harvest_plan])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, distribution])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop_1, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[loop_2, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, skip])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[xor_2, xor_3])

# Add transitions to the root
root.add_transition(site_survey)
root.add_transition(structural_audit)
root.add_transition(layout_design)
root.add_transition(xor_4)
root.add_transition(sustainability)

# Add edges to the root
root.add_edge(site_survey, layout_design)
root.add_edge(structural_audit, layout_design)
root.add_edge(layout_design, xor)
root.add_edge(xor, xor_2)
root.add_edge(xor_2, xor_3)
root.add_edge(xor_3, xor_4)
root.add_edge(xor_4, sustainability)