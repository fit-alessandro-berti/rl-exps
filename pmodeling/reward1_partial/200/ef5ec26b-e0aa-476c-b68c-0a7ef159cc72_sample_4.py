root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Soil Testing'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Resource Plan'),
    Transition(label='Crop Selection'),
    Transition(label='Volunteer Sign-up'),
    Transition(label='Tech Setup'),
    Transition(label='Irrigation Check'),
    Transition(label='Data Collection'),
    Transition(label='Growth Monitoring'),
    Transition(label='Conflict Mediate'),
    Transition(label='Workshop Prep'),
    Transition(label='Market Forecast'),
    Transition(label='Yield Analysis'),
    Transition(label='Sustainability Audit'),
    Transition(label='Community Feedback'),
    Transition(label='Equipment Maintain'),
    Transition(label='Waste Manage')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Soil Testing'))
root.order.add_edge(Transition(label='Soil Testing'), Transition(label='Stakeholder Meet'))
root.order.add_edge(Transition(label='Stakeholder Meet'), Transition(label='Resource Plan'))
root.order.add_edge(Transition(label='Resource Plan'), Transition(label='Crop Selection'))
root.order.add_edge(Transition(label='Crop Selection'), Transition(label='Volunteer Sign-up'))
root.order.add_edge(Transition(label='Volunteer Sign-up'), Transition(label='Tech Setup'))
root.order.add_edge(Transition(label='Tech Setup'), Transition(label='Irrigation Check'))
root.order.add_edge(Transition(label='Irrigation Check'), Transition(label='Data Collection'))
root.order.add_edge(Transition(label='Data Collection'), Transition(label='Growth Monitoring'))
root.order.add_edge(Transition(label='Growth Monitoring'), Transition(label='Conflict Mediate'))
root.order.add_edge(Transition(label='Conflict Mediate'), Transition(label='Workshop Prep'))
root.order.add_edge(Transition(label='Workshop Prep'), Transition(label='Market Forecast'))
root.order.add_edge(Transition(label='Market Forecast'), Transition(label='Yield Analysis'))
root.order.add_edge(Transition(label='Yield Analysis'), Transition(label='Sustainability Audit'))
root.order.add_edge(Transition(label='Sustainability Audit'), Transition(label='Community Feedback'))
root.order.add_edge(Transition(label='Community Feedback'), Transition(label='Equipment Maintain'))
root.order.add_edge(Transition(label='Equipment Maintain'), Transition(label='Waste Manage'))