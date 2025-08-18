root = StrictPartialOrder(nodes=[
    Transition(label='Verify Provenance'),
    Transition(label='Assess Condition'),
    Transition(label='Negotiate Terms'),
    Transition(label='Arrange Transport'),
    Transition(label='Customs Clearance'),
    Transition(label='Secure Insurance'),
    Transition(label='Schedule Handlers'),
    Transition(label='Install Artwork'),
    Transition(label='Monitor Climate'),
    Transition(label='Manage Security'),
    Transition(label='Facilitate Access'),
    Transition(label='Document Display'),
    Transition(label='Coordinate Events'),
    Transition(label='Inspect Periodically'),
    Transition(label='Plan Return'),
    Transition(label='Deinstall Artwork'),
    Transition(label='Finalize Reports')
])

# Define the dependencies between the activities
root.order.add_edge(Transition(label='Verify Provenance'), Transition(label='Assess Condition'))
root.order.add_edge(Transition(label='Assess Condition'), Transition(label='Negotiate Terms'))
root.order.add_edge(Transition(label='Negotiate Terms'), Transition(label='Arrange Transport'))
root.order.add_edge(Transition(label='Arrange Transport'), Transition(label='Customs Clearance'))
root.order.add_edge(Transition(label='Customs Clearance'), Transition(label='Secure Insurance'))
root.order.add_edge(Transition(label='Secure Insurance'), Transition(label='Schedule Handlers'))
root.order.add_edge(Transition(label='Schedule Handlers'), Transition(label='Install Artwork'))
root.order.add_edge(Transition(label='Install Artwork'), Transition(label='Monitor Climate'))
root.order.add_edge(Transition(label='Monitor Climate'), Transition(label='Manage Security'))
root.order.add_edge(Transition(label='Manage Security'), Transition(label='Facilitate Access'))
root.order.add_edge(Transition(label='Facilitate Access'), Transition(label='Document Display'))
root.order.add_edge(Transition(label='Document Display'), Transition(label='Coordinate Events'))
root.order.add_edge(Transition(label='Coordinate Events'), Transition(label='Inspect Periodically'))
root.order.add_edge(Transition(label='Inspect Periodically'), Transition(label='Plan Return'))
root.order.add_edge(Transition(label='Plan Return'), Transition(label='Deinstall Artwork'))
root.order.add_edge(Transition(label='Deinstall Artwork'), Transition(label='Finalize Reports'))