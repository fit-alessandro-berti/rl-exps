import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their exact names
verify_provenance = Transition(label='Verify Provenance')
assess_condition = Transition(label='Assess Condition')
negotiate_terms = Transition(label='Negotiate Terms')
arrange_transport = Transition(label='Arrange Transport')
customs_clearance = Transition(label='Customs Clearance')
secure_insurance = Transition(label='Secure Insurance')
schedule_handlers = Transition(label='Schedule Handlers')
install_artwork = Transition(label='Install Artwork')
monitor_climate = Transition(label='Monitor Climate')
manage_security = Transition(label='Manage Security')
facilitate_access = Transition(label='Facilitate Access')
document_display = Transition(label='Document Display')
coordinate_events = Transition(label='Coordinate Events')
inspect_periodically = Transition(label='Inspect Periodically')
plan_return = Transition(label='Plan Return')
deinstall_artwork = Transition(label='Deinstall Artwork')
finalize_reports = Transition(label='Finalize Reports')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    verify_provenance, 
    assess_condition, 
    negotiate_terms, 
    arrange_transport, 
    customs_clearance, 
    secure_insurance, 
    schedule_handlers, 
    install_artwork, 
    monitor_climate, 
    manage_security, 
    facilitate_access, 
    document_display, 
    coordinate_events, 
    inspect_periodically, 
    plan_return, 
    deinstall_artwork, 
    finalize_reports
])

# No dependencies are explicitly defined in this simple example, so we don't need to add edges explicitly
# In a more complex scenario, you would add edges to represent dependencies between activities

# The final result is saved in the variable 'root'