import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
IntakeReview = Transition(label='Intake Review')
ConditionScan = Transition(label='Condition Scan')
MaterialTest = Transition(label='Material Test')
StyleMatch = Transition(label='Style Match')
ProvenanceLog = Transition(label='Provenance Log')
ForgeryRisk = Transition(label='Forgery Risk')
LegalAudit = Transition(label='Legal Audit')
ExpertPanel = Transition(label='Expert Panel')
DataCrosscheck = Transition(label='Data Crosscheck')
ReportDraft = Transition(label='Report Draft')
BlockchainTag = Transition(label='Blockchain Tag')
Certification = Transition(label='Certification')
ClientFeedback = Transition(label='Client Feedback')
FinalApproval = Transition(label='Final Approval')
ReleasePrep = Transition(label='Release Prep')

# Define silent transitions (empty labels)
SkipIntake = SilentTransition()
SkipCondition = SilentTransition()
SkipMaterial = SilentTransition()
SkipStyle = SilentTransition()
SkipProvenance = SilentTransition()
SkipForgery = SilentTransition()
SkipLegal = SilentTransition()
SkipExpert = SilentTransition()
SkipData = SilentTransition()
SkipReport = SilentTransition()
SkipBlockchain = SilentTransition()
SkipCertification = SilentTransition()
SkipClient = SilentTransition()
SkipFinal = SilentTransition()

# Define the workflow structure using POWL operators
IntakeReviewNode = OperatorPOWL(operator=Operator.XOR, children=[SkipIntake, IntakeReview])
ConditionScanNode = OperatorPOWL(operator=Operator.XOR, children=[SkipCondition, ConditionScan])
MaterialTestNode = OperatorPOWL(operator=Operator.XOR, children=[SkipMaterial, MaterialTest])
StyleMatchNode = OperatorPOWL(operator=Operator.XOR, children=[SkipStyle, StyleMatch])
ProvenanceLogNode = OperatorPOWL(operator=Operator.XOR, children=[SkipProvenance, ProvenanceLog])
ForgeryRiskNode = OperatorPOWL(operator=Operator.XOR, children=[SkipForgery, ForgeriesRisk])
LegalAuditNode = OperatorPOWL(operator=Operator.XOR, children=[SkipLegal, LegalAudit])
ExpertPanelNode = OperatorPOWL(operator=Operator.XOR, children=[SkipExpert, ExpertPanel])
DataCrosscheckNode = OperatorPOWL(operator=Operator.XOR, children=[SkipData, DataCrosscheck])
ReportDraftNode = OperatorPOWL(operator=Operator.XOR, children=[SkipReport, ReportDraft])
BlockchainTagNode = OperatorPOWL(operator=Operator.XOR, children=[SkipBlockchain, BlockchainTag])
CertificationNode = OperatorPOWL(operator=Operator.XOR, children=[SkipCertification, Certification])
ClientFeedbackNode = OperatorPOWL(operator=Operator.XOR, children=[SkipClient, ClientFeedback])
FinalApprovalNode = OperatorPOWL(operator=Operator.XOR, children=[SkipFinal, FinalApproval])

# Construct the root POWL model
root = StrictPartialOrder(
    nodes=[
        IntakeReviewNode,
        ConditionScanNode,
        MaterialTestNode,
        StyleMatchNode,
        ProvenanceLogNode,
        ForgeriesRiskNode,
        LegalAuditNode,
        ExpertPanelNode,
        DataCrosscheckNode,
        ReportDraftNode,
        BlockchainTagNode,
        CertificationNode,
        ClientFeedbackNode,
        FinalApprovalNode
    ]
)

# Add dependencies between nodes
root.order.add_edge(IntakeReviewNode, ConditionScanNode)
root.order.add_edge(ConditionScanNode, MaterialTestNode)
root.order.add_edge(MaterialTestNode, StyleMatchNode)
root.order.add_edge(StyleMatchNode, ProvenanceLogNode)
root.order.add_edge(ProvenanceLogNode, ForgeriesRiskNode)
root.order.add_edge(ForgeriesRiskNode, LegalAuditNode)
root.order.add_edge(LegalAuditNode, ExpertPanelNode)
root.order.add_edge(ExpertPanelNode, DataCrosscheckNode)
root.order.add_edge(DataCrosscheckNode, ReportDraftNode)
root.order.add_edge(ReportDraftNode, BlockchainTagNode)
root.order.add_edge(BlockchainTagNode, CertificationNode)
root.order.add_edge(CertificationNode, ClientFeedbackNode)
root.order.add_edge(ClientFeedbackNode, FinalApprovalNode)

print(root)