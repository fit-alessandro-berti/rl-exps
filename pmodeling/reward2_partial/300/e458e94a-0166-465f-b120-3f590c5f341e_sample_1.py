import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Inquiry_Review = Transition(label='Inquiry Review')
Client_Onboard = Transition(label='Client Onboard')
Concept_Draft = Transition(label='Concept Draft')
Feedback_Cycle = Transition(label='Feedback Cycle')
Contract_Setup = Transition(label='Contract Setup')
Payment_Schedule = Transition(label='Payment Schedule')
Material_Sourcing = Transition(label='Material Sourcing')
Artwork_Create = Transition(label='Artwork Create')
Quality_Check = Transition(label='Quality Check')
Frame_Selection = Transition(label='Frame Selection')
Packaging_Prep = Transition(label='Packaging Prep')
Shipment_Arrange = Transition(label='Shipment Arrange')
Delivery_Confirm = Transition(label='Delivery Confirm')
Post_Sale_Support = Transition(label='Post-Sale Support')
Revision_Manage = Transition(label='Revision Manage')
Delay_Mitigate = Transition(label='Delay Mitigate')

# Define the process
root = StrictPartialOrder(nodes=[
    Inquiry_Review,
    Client_Onboard,
    Concept_Draft,
    Feedback_Cycle,
    Contract_Setup,
    Payment_Schedule,
    Material_Sourcing,
    Artwork_Create,
    Quality_Check,
    Frame_Selection,
    Packaging_Prep,
    Shipment_Arrange,
    Delivery_Confirm,
    Post_Sale_Support,
    Revision_Manage,
    Delay_Mitigate
])

# Define the order
root.order.add_edge(Inquiry_Review, Client_Onboard)
root.order.add_edge(Client_Onboard, Concept_Draft)
root.order.add_edge(Concept_Draft, Feedback_Cycle)
root.order.add_edge(Feedback_Cycle, Contract_Setup)
root.order.add_edge(Contract_Setup, Payment_Schedule)
root.order.add_edge(Payment_Schedule, Material_Sourcing)
root.order.add_edge(Material_Sourcing, Artwork_Create)
root.order.add_edge(Artwork_Create, Quality_Check)
root.order.add_edge(Quality_Check, Frame_Selection)
root.order.add_edge(Frame_Selection, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Shipment_Arrange)
root.order.add_edge(Shipment_Arrange, Delivery_Confirm)
root.order.add_edge(Delivery_Confirm, Post_Sale_Support)
root.order.add_edge(Post_Sale_Support, Revision_Manage)
root.order.add_edge(Revision_Manage, Delay_Mitigate)

print(root)