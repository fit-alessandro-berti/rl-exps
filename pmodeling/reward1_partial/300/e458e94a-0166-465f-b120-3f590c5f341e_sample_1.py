from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
InquiryReview = Transition(label='Inquiry Review')
ClientOnboard = Transition(label='Client Onboard')
ConceptDraft = Transition(label='Concept Draft')
FeedbackCycle = OperatorPOWL(operator=Operator.XOR, children=[Transition(label='Client Feedback'), Transition(label='Artist Feedback')])
ContractSetup = Transition(label='Contract Setup')
PaymentSchedule = Transition(label='Payment Schedule')
MaterialSourcing = Transition(label='Material Sourcing')
ArtworkCreate = Transition(label='Artwork Create')
QualityCheck = Transition(label='Quality Check')
FrameSelection = Transition(label='Frame Selection')
PackagingPrep = Transition(label='Packaging Prep')
ShipmentArrange = Transition(label='Shipment Arrange')
DeliveryConfirm = Transition(label='Delivery Confirm')
PostSaleSupport = Transition(label='Post-Sale Support')
RevisionManage = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Creative Revision'), Transition(label='Legal Compliance')])
DelayMitigate = OperatorPOWL(operator=Operator.LOOP, children=[Transition(label='Contingency Plan'), Transition(label='Legal Compliance')])

# Define the partial order
root = StrictPartialOrder(nodes=[
    InquiryReview,
    ClientOnboard,
    ConceptDraft,
    FeedbackCycle,
    ContractSetup,
    PaymentSchedule,
    MaterialSourcing,
    ArtworkCreate,
    QualityCheck,
    FrameSelection,
    PackagingPrep,
    ShipmentArrange,
    DeliveryConfirm,
    PostSaleSupport,
    RevisionManage,
    DelayMitigate
])

# Define the order between nodes
root.order.add_edge(InquiryReview, ClientOnboard)
root.order.add_edge(ClientOnboard, ConceptDraft)
root.order.add_edge(ConceptDraft, FeedbackCycle)
root.order.add_edge(FeedbackCycle, ContractSetup)
root.order.add_edge(ContractSetup, PaymentSchedule)
root.order.add_edge(PaymentSchedule, MaterialSourcing)
root.order.add_edge(MaterialSourcing, ArtworkCreate)
root.order.add_edge(ArtworkCreate, QualityCheck)
root.order.add_edge(QualityCheck, FrameSelection)
root.order.add_edge(FrameSelection, PackagingPrep)
root.order.add_edge(PackagingPrep, ShipmentArrange)
root.order.add_edge(ShipmentArrange, DeliveryConfirm)
root.order.add_edge(DeliveryConfirm, PostSaleSupport)
root.order.add_edge(PostSaleSupport, RevisionManage)
root.order.add_edge(RevisionManage, DelayMitigate)
root.order.add_edge(DelayMitigate, RevisionManage)