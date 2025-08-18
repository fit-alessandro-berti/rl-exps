root = StrictPartialOrder(nodes=[
    Transition('Artifact Intake'),
    Transition('Catalog Entry'),
    Transition('Visual Inspect'),
    Transition('Material Test'),
    Transition('Spectroscopy'),
    Transition('Historical Check'),
    Transition('Provenance Trace'),
    Transition('Style Compare'),
    Transition('3D Scanning'),
    Transition('Condition Assess'),
    Transition('Preservation Plan'),
    Transition('Legal Review'),
    Transition('Report Draft'),
    Transition('Report Finalize'),
    Transition('Archive Data'),
    Transition('Sale Prep')
])

root.order.add_edge(Transition('Artifact Intake'), Transition('Catalog Entry'))
root.order.add_edge(Transition('Catalog Entry'), Transition('Visual Inspect'))
root.order.add_edge(Transition('Visual Inspect'), Transition('Material Test'))
root.order.add_edge(Transition('Material Test'), Transition('Spectroscopy'))
root.order.add_edge(Transition('Spectroscopy'), Transition('Historical Check'))
root.order.add_edge(Transition('Historical Check'), Transition('Provenance Trace'))
root.order.add_edge(Transition('Provenance Trace'), Transition('Style Compare'))
root.order.add_edge(Transition('Style Compare'), Transition('3D Scanning'))
root.order.add_edge(Transition('3D Scanning'), Transition('Condition Assess'))
root.order.add_edge(Transition('Condition Assess'), Transition('Preservation Plan'))
root.order.add_edge(Transition('Preservation Plan'), Transition('Legal Review'))
root.order.add_edge(Transition('Legal Review'), Transition('Report Draft'))
root.order.add_edge(Transition('Report Draft'), Transition('Report Finalize'))
root.order.add_edge(Transition('Report Finalize'), Transition('Archive Data'))
root.order.add_edge(Transition('Archive Data'), Transition('Sale Prep'))