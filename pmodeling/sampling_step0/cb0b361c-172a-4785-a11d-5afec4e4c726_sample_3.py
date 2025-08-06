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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
site_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_audit, layout_design])
system_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_install, climate_setup])
water_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_testing, nutrient_mix])
seed_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, planting_prep])
growth_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_inspect])
harvest_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, packaging_prep])
distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[distribution, sustainability])

# Define exclusive choices
site_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])
system_install_xor = OperatorPOWL(operator=Operator.XOR, children=[system_install_loop, skip])
climate_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
water_testing_xor = OperatorPOWL(operator=Operator.XOR, children=[water_testing_loop, skip])
nutrient_mix_xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
seed_selection_xor = OperatorPOWL(operator=Operator.XOR, children=[seed_selection_loop, skip])
planting_prep_xor = OperatorPOWL(operator=Operator.XOR, children=[planting_prep, skip])
growth_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor_loop, skip])
pest_inspect_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_inspect, skip])
harvest_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan_loop, skip])
packaging_prep_xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
distribution_xor = OperatorPOWL(operator=Operator.XOR, children=[distribution_loop, skip])

# Define the root
root = StrictPartialOrder(nodes=[site_audit_xor, system_install_xor, climate_setup_xor, water_testing_xor, nutrient_mix_xor, seed_selection_xor, planting_prep_xor, growth_monitor_xor, pest_inspect_xor, harvest_plan_xor, packaging_prep_xor, distribution_xor])
root.order.add_edge(site_audit_xor, system_install_xor)
root.order.add_edge(system_install_xor, climate_setup_xor)
root.order.add_edge(climate_setup_xor, water_testing_xor)
root.order.add_edge(water_testing_xor, nutrient_mix_xor)
root.order.add_edge(nutrient_mix_xor, seed_selection_xor)
root.order.add_edge(seed_selection_xor, planting_prep_xor)
root.order.add_edge(planting_prep_xor, growth_monitor_xor)
root.order.add_edge(growth_monitor_xor, pest_inspect_xor)
root.order.add_edge(pest_inspect_xor, harvest_plan_xor)
root.order.add_edge(harvest_plan_xor, packaging_prep_xor)
root.order.add_edge(packaging_prep_xor, distribution_xor)

# Return the root
return root