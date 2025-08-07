import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the root node as a strict partial order with all activities
root = StrictPartialOrder(nodes=[
    site_analysis,
    design_layout,
    module_assembly,
    climate_setup,
    sensor_install,
    water_testing,
    nutrient_mix,
    seed_selection,
    planting_phase,
    growth_monitor,
    pest_control,
    harvest_plan,
    yield_audit,
    packaging_prep,
    market_delivery,
    waste_recycling
])

# Since all activities are concurrent, there are no explicit dependencies
# However, if there were dependencies, they would be added here using root.order.add_edge(source, target)

print(root)