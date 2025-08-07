import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the POWL model
root = StrictPartialOrder(nodes=[site_survey, structural_audit, layout_design, system_install, climate_setup, water_testing, nutrient_mix, seed_selection, planting_prep, growth_monitor, pest_inspect, harvest_plan, packaging_prep, distribution, sustainability])

# Add dependencies if needed (e.g., site_survey depends on structural_audit, etc.)
# root.order.add_edge(site_survey, structural_audit)
# root.order.add_edge(site_survey, layout_design)
# ...

# Print the root model for verification
print(root)