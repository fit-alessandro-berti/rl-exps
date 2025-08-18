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

# Define the workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_audit,
    layout_design,
    system_install,
    climate_setup,
    water_testing,
    nutrient_mix,
    seed_selection,
    planting_prep,
    growth_monitor,
    pest_inspect,
    harvest_plan,
    packaging_prep,
    distribution,
    sustainability
])

# Define the dependencies
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, layout_design)
root.order.add_edge(layout_design, system_install)
root.order.add_edge(system_install, climate_setup)
root.order.add_edge(climate_setup, water_testing)
root.order.add_edge(water_testing, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, planting_prep)
root.order.add_edge(planting_prep, growth_monitor)
root.order.add_edge(growth_monitor, pest_inspect)
root.order.add_edge(pest_inspect, harvest_plan)
root.order.add_edge(harvest_plan, packaging_prep)
root.order.add_edge(packaging_prep, distribution)
root.order.add_edge(distribution, sustainability)

print(root)