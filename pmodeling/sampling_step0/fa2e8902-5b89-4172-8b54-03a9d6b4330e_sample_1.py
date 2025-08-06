root = StrictPartialOrder(nodes=[
    Transition(label='Seed Selection'),
    Transition(label='Germination Start'),
    Transition(label='Nutrient Mix'),
    Transition(label='Climate Adjust'),
    Transition(label='Light Scheduling'),
    Transition(label='Pest Inspection'),
    Transition(label='Bio Control'),
    Transition(label='Growth Monitor'),
    Transition(label='Water Recirc'),
    Transition(label='Harvest Plan'),
    Transition(label='Yield Forecast'),
    Transition(label='Quality Check'),
    Transition(label='Packaging Prep'),
    Transition(label='Cold Storage'),
    Transition(label='Delivery Route'),
    Transition(label='Energy Audit'),
    Transition(label='Sustain Report'),
])

root.order.add_edge(
    Transition(label='Seed Selection'),
    Transition(label='Germination Start'),
)

root.order.add_edge(
    Transition(label='Germination Start'),
    Transition(label='Nutrient Mix'),
)

root.order.add_edge(
    Transition(label='Nutrient Mix'),
    Transition(label='Climate Adjust'),
)

root.order.add_edge(
    Transition(label='Climate Adjust'),
    Transition(label='Light Scheduling'),
)

root.order.add_edge(
    Transition(label='Light Scheduling'),
    Transition(label='Pest Inspection'),
)

root.order.add_edge(
    Transition(label='Pest Inspection'),
    Transition(label='Bio Control'),
)

root.order.add_edge(
    Transition(label='Bio Control'),
    Transition(label='Growth Monitor'),
)

root.order.add_edge(
    Transition(label='Growth Monitor'),
    Transition(label='Water Recirc'),
)

root.order.add_edge(
    Transition(label='Water Recirc'),
    Transition(label='Harvest Plan'),
)

root.order.add_edge(
    Transition(label='Harvest Plan'),
    Transition(label='Yield Forecast'),
)

root.order.add_edge(
    Transition(label='Yield Forecast'),
    Transition(label='Quality Check'),
)

root.order.add_edge(
    Transition(label='Quality Check'),
    Transition(label='Packaging Prep'),
)

root.order.add_edge(
    Transition(label='Packaging Prep'),
    Transition(label='Cold Storage'),
)

root.order.add_edge(
    Transition(label='Cold Storage'),
    Transition(label='Delivery Route'),
)

root.order.add_edge(
    Transition(label='Delivery Route'),
    Transition(label='Energy Audit'),
)

root.order.add_edge(
    Transition(label='Energy Audit'),
    Transition(label='Sustain Report'),
)