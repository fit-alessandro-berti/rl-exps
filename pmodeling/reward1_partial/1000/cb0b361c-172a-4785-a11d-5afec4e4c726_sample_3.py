import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
site_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_audit, layout_design])
water_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_testing, nutrient_mix])
planting_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_prep, growth_monitor])
pest_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_inspect, harvest_plan])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, distribution])
sustainability_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[site_survey, site_audit_loop, system_install, climate_setup, water_testing_loop, planting_loop, pest_inspect_loop, packaging_loop, sustainability_loop])
root.order.add_edge(site_survey, site_audit_loop)
root.order.add_edge(site_audit_loop, system_install)
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(climate_setup, water_testing_loop)
root.order.add_edge(water_testing_loop, planting_loop)
root.order.add_edge(planting_loop, pest_inspect_loop)
root.order.add_edge(pest_inspect_loop, packaging_loop)
root.order.add_edge(packaging_loop, sustainability_loop)