import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[system_install, climate_setup, water_testing, nutrient_mix, planting_prep, growth_monitor, pest_inspect, harvest_plan])
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, distribution])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, sustainability)

print(root)