root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Climate Plan'),
    Transition(label='System Design'),
    Transition(label='AI Setup'),
    Transition(label='Seed Sourcing'),
    Transition(label='Nutrient Mix'),
    Transition(label='Install Hydro'),
    Transition(label='Energy Audit'),
    Transition(label='Staff Training'),
    Transition(label='Trial Growth'),
    Transition(label='Yield Measure'),
    Transition(label='Waste Cycle'),
    Transition(label='Compliance Check'),
    Transition(label='Market Study'),
    Transition(label='Community Meet'),
    Transition(label='Optimize Environment')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Climate Plan'))
root.order.add_edge(Transition(label='Climate Plan'), Transition(label='System Design'))
root.order.add_edge(Transition(label='System Design'), Transition(label='AI Setup'))
root.order.add_edge(Transition(label='AI Setup'), Transition(label='Seed Sourcing'))
root.order.add_edge(Transition(label='Seed Sourcing'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Install Hydro'))
root.order.add_edge(Transition(label='Install Hydro'), Transition(label='Energy Audit'))
root.order.add_edge(Transition(label='Energy Audit'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Trial Growth'))
root.order.add_edge(Transition(label='Trial Growth'), Transition(label='Yield Measure'))
root.order.add_edge(Transition(label='Yield Measure'), Transition(label='Waste Cycle'))
root.order.add_edge(Transition(label='Waste Cycle'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Market Study'))
root.order.add_edge(Transition(label='Market Study'), Transition(label='Community Meet'))
root.order.add_edge(Transition(label='Community Meet'), Transition(label='Optimize Environment'))