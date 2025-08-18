import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the workflow model
loop_climate = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust, light_scheduling])
loop_water = OperatorPOWL(operator=Operator.LOOP, children=[water_recirc])
loop_pest = OperatorPOWL(operator=Operator.LOOP, children=[pest_inspection, bio_control])
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor])
loop_yield = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast])
loop_quality = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, packaging_prep])
loop_storage = OperatorPOWL(operator=Operator.LOOP, children=[cold_storage, delivery_route])
loop_audit = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, sustain_report])

xor_pest = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, bio_control])
xor_yield = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, quality_check])
xor_storage = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, delivery_route])
xor_audit = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, sustain_report])

root = StrictPartialOrder(nodes=[
    seed_selection, germination_start, nutrient_mix, loop_climate, loop_water, loop_pest, loop_monitor, harvest_plan,
    xor_pest, loop_yield, xor_yield, loop_quality, xor_storage, loop_storage, xor_audit, loop_audit
])

# Define dependencies between nodes
root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, nutrient_mix)
root.order.add_edge(nutrient_mix, loop_climate)
root.order.add_edge(loop_climate, light_scheduling)
root.order.add_edge(light_scheduling, loop_water)
root.order.add_edge(loop_water, loop_pest)
root.order.add_edge(loop_pest, growth_monitor)
root.order.add_edge(growth_monitor, loop_yield)
root.order.add_edge(loop_yield, harvest_plan)
root.order.add_edge(harvest_plan, xor_pest)
root.order.add_edge(xor_pest, loop_quality)
root.order.add_edge(loop_quality, xor_yield)
root.order.add_edge(xor_yield, loop_storage)
root.order.add_edge(loop_storage, xor_storage)
root.order.add_edge(xor_storage, loop_audit)
root.order.add_edge(loop_audit, xor_audit)

print(root)