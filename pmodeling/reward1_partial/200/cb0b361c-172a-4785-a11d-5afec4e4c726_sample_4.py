from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

site_survey_to_audit = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structural_audit])
audit_to_layout = OperatorPOWL(operator=Operator.XOR, children=[structural_audit, layout_design])
layout_to_install = OperatorPOWL(operator=Operator.XOR, children=[layout_design, system_install])
install_to_climate = OperatorPOWL(operator=Operator.XOR, children=[system_install, climate_setup])
climate_to_water = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, water_testing])
water_to_nutrient = OperatorPOWL(operator=Operator.XOR, children=[water_testing, nutrient_mix])
nutrient_to_seed = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_selection])
seed_to_planting = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, planting_prep])
planting_to_monitor = OperatorPOWL(operator=Operator.XOR, children=[planting_prep, growth_monitor])
monitor_to_pest = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_inspect])
pest_to_harvest = OperatorPOWL(operator=Operator.XOR, children=[pest_inspect, harvest_plan])
harvest_to_packaging = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, packaging_prep])
packaging_to_distribution = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, distribution])
distribution_to_sustainability = OperatorPOWL(operator=Operator.XOR, children=[distribution, sustainability])

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