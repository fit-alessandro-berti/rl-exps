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

site_audit = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structural_audit])
layout = OperatorPOWL(operator=Operator.LOOP, children=[layout_design, system_install])
climate = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, water_testing])
nutrient = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, seed_selection])
planting = OperatorPOWL(operator=Operator.LOOP, children=[planting_prep, growth_monitor])
pest = OperatorPOWL(operator=Operator.LOOP, children=[pest_inspect, harvest_plan])
packaging = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, distribution])

root = StrictPartialOrder(nodes=[site_audit, layout, climate, nutrient, planting, pest, packaging, sustainability])
root.order.add_edge(site_audit, layout)
root.order.add_edge(site_audit, climate)
root.order.add_edge(layout, climate)
root.order.add_edge(climate, nutrient)
root.order.add_edge(nutrient, planting)
root.order.add_edge(planting, pest)
root.order.add_edge(pest, packaging)
root.order.add_edge(packaging, sustainability)