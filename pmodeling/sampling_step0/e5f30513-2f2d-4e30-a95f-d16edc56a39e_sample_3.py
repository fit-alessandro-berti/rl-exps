root = StrictPartialOrder(nodes=[
    Transition(label='Intake Review'),
    Transition(label='Preliminary Inspect'),
    Transition(label='Provenance Check'),
    Transition(label='Archival Research'),
    Transition(label='Material Testing'),
    Transition(label='Radiocarbon Date'),
    Transition(label='Stylistic Assess'),
    Transition(label='Expert Consult'),
    Transition(label='Findings Compile'),
    Transition(label='Internal Review'),
    Transition(label='Client Present'),
    Transition(label='Approval Confirm'),
    Transition(label='Secure Package'),
    Transition(label='Transport Arrange'),
    Transition(label='Chain Custody')
])

root.order.add_edge(Transition(label='Intake Review'), Transition(label='Preliminary Inspect'))
root.order.add_edge(Transition(label='Preliminary Inspect'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Archival Research'))
root.order.add_edge(Transition(label='Archival Research'), Transition(label='Material Testing'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Radiocarbon Date'))
root.order.add_edge(Transition(label='Radiocarbon Date'), Transition(label='Stylistic Assess'))
root.order.add_edge(Transition(label='Stylistic Assess'), Transition(label='Expert Consult'))
root.order.add_edge(Transition(label='Expert Consult'), Transition(label='Findings Compile'))
root.order.add_edge(Transition(label='Findings Compile'), Transition(label='Internal Review'))
root.order.add_edge(Transition(label='Internal Review'), Transition(label='Client Present'))
root.order.add_edge(Transition(label='Client Present'), Transition(label='Approval Confirm'))
root.order.add_edge(Transition(label='Approval Confirm'), Transition(label='Secure Package'))
root.order.add_edge(Transition(label='Secure Package'), Transition(label='Transport Arrange'))
root.order.add_edge(Transition(label='Transport Arrange'), Transition(label='Chain Custody'))