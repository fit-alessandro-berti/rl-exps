root = StrictPartialOrder(nodes=[
    Transition(label='Seed Select'),
    Transition(label='Germinate Seeds'),
    Transition(label='Transplant Seedlings'),
    Transition(label='Mix Nutrients'),
    Transition(label='Adjust pH'),
    Transition(label='Monitor Climate'),
    Transition(label='Control Humidity'),
    Transition(label='CO2 Regulation'),
    Transition(label='Detect Pests'),
    Transition(label='Deploy Biocontrols'),
    Transition(label='Schedule Harvest'),
    Transition(label='Automate Picking'),
    Transition(label='Package Produce'),
    Transition(label='Compost Waste'),
    Transition(label='Recycle Water'),
    Transition(label='Data Logging'),
    Transition(label='System Maintenance')
])

# Define the dependencies between activities
root.order.add_edge(Transition(label='Seed Select'), Transition(label='Germinate Seeds'))
root.order.add_edge(Transition(label='Germinate Seeds'), Transition(label='Transplant Seedlings'))
root.order.add_edge(Transition(label='Transplant Seedlings'), Transition(label='Mix Nutrients'))
root.order.add_edge(Transition(label='Mix Nutrients'), Transition(label='Adjust pH'))
root.order.add_edge(Transition(label='Adjust pH'), Transition(label='Monitor Climate'))
root.order.add_edge(Transition(label='Monitor Climate'), Transition(label='Control Humidity'))
root.order.add_edge(Transition(label='Control Humidity'), Transition(label='CO2 Regulation'))
root.order.add_edge(Transition(label='CO2 Regulation'), Transition(label='Detect Pests'))
root.order.add_edge(Transition(label='Detect Pests'), Transition(label='Deploy Biocontrols'))
root.order.add_edge(Transition(label='Deploy Biocontrols'), Transition(label='Schedule Harvest'))
root.order.add_edge(Transition(label='Schedule Harvest'), Transition(label='Automate Picking'))
root.order.add_edge(Transition(label='Automate Picking'), Transition(label='Package Produce'))
root.order.add_edge(Transition(label='Package Produce'), Transition(label='Compost Waste'))
root.order.add_edge(Transition(label='Compost Waste'), Transition(label='Recycle Water'))
root.order.add_edge(Transition(label='Recycle Water'), Transition(label='Data Logging'))
root.order.add_edge(Transition(label='Data Logging'), Transition(label='System Maintenance'))