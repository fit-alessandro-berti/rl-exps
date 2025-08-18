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

# Define POWL models
site_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[structural_audit, skip])
system_install_choice = OperatorPOWL(operator=Operator.XOR, children=[layout_design, system_install])
climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, skip])
water_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_testing, skip])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, skip])
planting_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_prep, skip])
pest_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_inspect, skip])
harvest_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, skip])
distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[distribution, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    system_install_choice,
    climate_control_loop,
    water_test_loop,
    nutrient_mix_loop,
    planting_prep_loop,
    growth_monitor,
    pest_inspect_loop,
    harvest_plan_loop,
    packaging_prep,
    distribution_loop,
    sustainability
])

# Define dependencies
root.order.add_edge(site_survey, system_install_choice)
root.order.add_edge(system_install_choice, climate_control_loop)
root.order.add_edge(climate_control_loop, water_test_loop)
root.order.add_edge(water_test_loop, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, planting_prep_loop)
root.order.add_edge(planting_prep_loop, growth_monitor)
root.order.add_edge(growth_monitor, pest_inspect_loop)
root.order.add_edge(pest_inspect_loop, harvest_plan_loop)
root.order.add_edge(harvest_plan_loop, packaging_prep)
root.order.add_edge(packaging_prep, distribution_loop)
root.order.add_edge(distribution_loop, sustainability)

print(root)