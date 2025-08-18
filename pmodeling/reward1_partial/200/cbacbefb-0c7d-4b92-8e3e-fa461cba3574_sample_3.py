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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define sub-workflows
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, skip])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, skip])
water_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_testing, skip])
nutrient_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, skip])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, skip])
yield_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_audit, skip])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, skip])
delivery_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_delivery, skip])
recycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycling, skip])

# Define the main workflow
root = StrictPartialOrder(nodes=[site_analysis, design_layout, module_assembly, climate_loop, sensor_loop, water_loop, nutrient_loop, seed_selection, planting_phase, growth_monitor, pest_loop, harvest_plan, yield_loop, packaging_loop, delivery_loop, recycling_loop])
root.order.add_edge(site_analysis, design_layout)
root.order.add_edge(design_layout, module_assembly)
root.order.add_edge(module_assembly, climate_loop)
root.order.add_edge(climate_loop, sensor_loop)
root.order.add_edge(sensor_loop, water_loop)
root.order.add_edge(water_loop, nutrient_loop)
root.order.add_edge(nutrient_loop, seed_selection)
root.order.add_edge(seed_selection, planting_phase)
root.order.add_edge(planting_phase, growth_monitor)
root.order.add_edge(growth_monitor, pest_loop)
root.order.add_edge(pest_loop, harvest_plan)
root.order.add_edge(harvest_plan, yield_loop)
root.order.add_edge(yield_loop, packaging_loop)
root.order.add_edge(packaging_loop, delivery_loop)
root.order.add_edge(delivery_loop, recycling_loop)

# Output the root node
print(root)