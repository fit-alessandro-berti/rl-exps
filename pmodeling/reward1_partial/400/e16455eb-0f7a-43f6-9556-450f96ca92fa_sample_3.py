from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Verify_Provenance = Transition(label='Verify Provenance')
Assess_Condition = Transition(label='Assess Condition')
Negotiate_Terms = Transition(label='Negotiate Terms')
Arrange_Transport = Transition(label='Arrange Transport')
Customs_Clearance = Transition(label='Customs Clearance')
Secure_Insurance = Transition(label='Secure Insurance')
Schedule_Handlers = Transition(label='Schedule Handlers')
Install_Artwork = Transition(label='Install Artwork')
Monitor_Climate = Transition(label='Monitor Climate')
Manage_Security = Transition(label='Manage Security')
Facilitate_Access = Transition(label='Facilitate Access')
Document_Display = Transition(label='Document Display')
Coordinate_Events = Transition(label='Coordinate Events')
Inspect_Periodically = Transition(label='Inspect Periodically')
Plan_Return = Transition(label='Plan Return')
Deinstall_Artwork = Transition(label='Deinstall Artwork')
Finalize_Reports = Transition(label='Finalize Reports')

# Define the loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Arrange_Transport, Customs_Clearance, Secure_Insurance, Schedule_Handlers,
    Install_Artwork, Monitor_Climate, Manage_Security, Facilitate_Access, Document_Display,
    Coordinate_Events, Inspect_Periodically, Plan_Return, Deinstall_Artwork, Finalize_Reports
])

# Define the partial order
root = StrictPartialOrder(nodes=[
    Verify_Provenance, Assess_Condition, Negotiate_Terms, loop
])

# Define the order dependencies
root.order.add_edge(Verify_Provenance, Assess_Condition)
root.order.add_edge(Assess_Condition, Negotiate_Terms)
root.order.add_edge(Negotiate_Terms, Arrange_Transport)
root.order.add_edge(Arrange_Transport, Customs_Clearance)
root.order.add_edge(Customs_Clearance, Secure_Insurance)
root.order.add_edge(Secure_Insurance, Schedule_Handlers)
root.order.add_edge(Schedule_Handlers, Install_Artwork)
root.order.add_edge(Install_Artwork, Monitor_Climate)
root.order.add_edge(Monitor_Climate, Manage_Security)
root.order.add_edge(Manage_Security, Facilitate_Access)
root.order.add_edge(Facilitate_Access, Document_Display)
root.order.add_edge(Document_Display, Coordinate_Events)
root.order.add_edge(Coordinate_Events, Inspect_Periodically)
root.order.add_edge(Inspect_Periodically, Plan_Return)
root.order.add_edge(Plan_Return, Deinstall_Artwork)
root.order.add_edge(Deinstall_Artwork, Finalize_Reports)

print(root)