import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
seed = Transition(label='Seed Selection')
germination = Transition(label='Germination Start')
nutrient = Transition(label='Nutrient Mix')
climate = Transition(label='Climate Adjust')
light = Transition(label='Light Scheduling')
pest_inspection = Transition(label='Pest Inspection')
bio_control = Transition(label='Bio Control')
growth = Transition(label='Growth Monitor')
water = Transition(label='Water Recirc')
harvest = Transition(label='Harvest Plan')
yield_forecast = Transition(label='Yield Forecast')
quality = Transition(label='Quality Check')
packaging = Transition(label='Packaging Prep')
cold_storage = Transition(label='Cold Storage')
delivery = Transition(label='Delivery Route')
energy_audit = Transition(label='Energy Audit')
sustain_report = Transition(label='Sustain Report')

# Loop for growth monitoring with pest inspection and bio control
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth, X(pest_inspection, bio_control)])

# Build the partial order
root = StrictPartialOrder(nodes=[
    seed, germination, nutrient, climate, light, growth_loop,
    harvest, yield_forecast, quality, packaging, cold_storage, delivery,
    energy_audit, sustain_report
])

# Define the control-flow dependencies
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, climate)
root.order.add_edge(climate, light)
root.order.add_edge(light, growth_loop)
root.order.add_edge(growth_loop, harvest)
root.order.add_edge(harvest, yield_forecast)
root.order.add_edge(yield_forecast, quality)
root.order.add_edge(quality, packaging)
root.order.add_edge(packaging, cold_storage)
root.order.add_edge(cold_storage, delivery)
root.order.add_edge(harvest, energy_audit)
root.order.add_edge(energy_audit, sustain_report)

# Silent transition for choice between harvest and no harvest
skip = SilentTransition()
choice = OperatorPOWL(operator=Operator.XOR, children=[harvest, skip])

# Final loop: do choice, then optionally do energy audit and sustain report
final_loop = OperatorPOWL(operator=Operator.LOOP, children=[choice, X(energy_audit, sustain_report)])
root.order.add_edge(growth_loop, final_loop)