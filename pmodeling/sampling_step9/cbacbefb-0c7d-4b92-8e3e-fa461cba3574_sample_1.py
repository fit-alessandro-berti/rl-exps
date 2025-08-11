import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
design_layout = Transition(label='Design Layout')
module_assembly = Transition(label='Module Assembly')
climate_setup = Transition(label='Climate Setup')
sensor_install = Transition(label='Sensor Install')
water_testing = Transition(label='Water Testing')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_phase = Transition(label='Planting Phase')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
yield_audit = Transition(label='Yield Audit')
packaging_prep = Transition(label='Packaging Prep')
market_delivery = Transition(label='Market Delivery')
waste_recycling = Transition(label='Waste Recycling')

# Define silent transitions
skip = SilentTransition()

# Define loops for certain activities
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, sensor_install, water_testing])
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, seed_selection, planting_phase, growth_monitor, pest_control])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan, yield_audit, packaging_prep, market_delivery, waste_recycling])

# Define the partial order
root = StrictPartialOrder(nodes=[site_analysis, design_layout, module_assembly, climate_loop, nutrient_mix_loop, harvest_loop])
root.order.add_edge(site_analysis, design_layout)
root.order.add_edge(site_analysis, module_assembly)
root.order.add_edge(design_layout, module_assembly)
root.order.add_edge(module_assembly, climate_loop)
root.order.add_edge(module_assembly, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, harvest_loop)

print(root)