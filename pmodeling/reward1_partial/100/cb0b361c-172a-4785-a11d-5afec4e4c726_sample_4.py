import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[structural_audit, layout_design, system_install, climate_setup, water_testing, nutrient_mix, seed_selection, planting_prep])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_inspect, harvest_plan, packaging_prep, distribution])
xor = OperatorPOWL(operator=Operator.XOR, children=[sustainability, skip])

root = StrictPartialOrder(nodes=[site_survey, loop1, loop2, xor])
root.order.add_edge(site_survey, loop1)
root.order.add_edge(site_survey, loop2)
root.order.add_edge(loop1, loop2)