root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Climate Check'),
    Transition(label='Soil Testing'),
    Transition(label='Media Select'),
    Transition(label='Design Layout'),
    Transition(label='Hydro Setup'),
    Transition(label='Nutrient Mix'),
    Transition(label='Sensor Install'),
    Transition(label='Regulation Review'),
    Transition(label='Permit Apply'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Community Train'),
    Transition(label='Plant Seed'),
    Transition(label='Monitor Growth'),
    Transition(label='Adjust Controls'),
    Transition(label='Harvest Plan'),
    Transition(label='Waste Recycle'),
    Transition(label='Feedback Loop')
])

# Add edges for each activity
root.order.add_edge(Transition(label='Site Survey'), Transition(label='Climate Check'))
root.order.add_edge(Transition(label='Climate Check'), Transition(label='Soil Testing'))
root.order.add_edge(Transition(label='Soil Testing'), Transition(label='Media Select'))
root.order.add_edge(Transition(label='Media Select'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Hydro Setup'))
root.order.add_edge(Transition(label='Hydro Setup'), Transition(label='Nutrient Mix'))
root.order.add_edge(Transition(label='Nutrient Mix'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Regulation Review'))
root.order.add_edge(Transition(label='Regulation Review'), Transition(label='Permit Apply'))
root.order.add_edge(Transition(label='Permit Apply'), Transition(label='Stakeholder Meet'))
root.order.add_edge(Transition(label='Stakeholder Meet'), Transition(label='Community Train'))
root.order.add_edge(Transition(label='Community Train'), Transition(label='Plant Seed'))
root.order.add_edge(Transition(label='Plant Seed'), Transition(label='Monitor Growth'))
root.order.add_edge(Transition(label='Monitor Growth'), Transition(label='Adjust Controls'))
root.order.add_edge(Transition(label='Adjust Controls'), Transition(label='Harvest Plan'))
root.order.add_edge(Transition(label='Harvest Plan'), Transition(label='Waste Recycle'))
root.order.add_edge(Transition(label='Waste Recycle'), Transition(label='Feedback Loop'))