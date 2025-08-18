import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
seed_selection = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
nutrient_mix = Transition(label='Nutrient Mix')
climate_adjust = Transition(label='Climate Adjust')
light_scheduling = Transition(label='Light Scheduling')
pest_inspection = Transition(label='Pest Inspection')
bio_control = Transition(label='Bio Control')
growth_monitor = Transition(label='Growth Monitor')
water_recirc = Transition(label='Water Recirc')
harvest_plan = Transition(label='Harvest Plan')
yield_forecast = Transition(label='Yield Forecast')
quality_check = Transition(label='Quality Check')
packaging_prep = Transition(label='Packaging Prep')
cold_storage = Transition(label='Cold Storage')
delivery_route = Transition(label='Delivery Route')
energy_audit = Transition(label='Energy Audit')
sustain_report = Transition(label='Sustain Report')

# Define silent transitions for non-executed steps
skip = SilentTransition()

# Define the workflow structure using the defined transitions and silent transitions
loop_germination = OperatorPOWL(operator=Operator.LOOP, children=[germination_start, nutrient_mix, climate_adjust, light_scheduling, pest_inspection, bio_control, growth_monitor, water_recirc])
loop_yield = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, quality_check, packaging_prep, cold_storage, delivery_route, energy_audit, sustain_report])

# Connect the loop nodes
root = StrictPartialOrder(nodes=[loop_germination, loop_yield])
root.order.add_edge(loop_germination, loop_yield)

# The final root of the POWL model
root