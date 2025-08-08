import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
CollectionSurvey = Transition(label='Collection Survey')
ProvenanceCheck = Transition(label='Provenance Check')
LegalReview = Transition(label='Legal Review')
ScientificTest = Transition(label='Scientific Test')
MaterialAnalysis = Transition(label='Material Analysis')
OwnershipAudit = Transition(label='Ownership Audit')
EthicalScreening = Transition(label='Ethical Screening')
ConditionReport = Transition(label='Condition Report')
ExpertConsultation = Transition(label='Expert Consultation')
TransportPlanning = Transition(label='Transport Planning')
SecurePacking = Transition(label='Secure Packing')
CustomsClearance = Transition(label='Customs Clearance')
InsuranceSetup = Transition(label='Insurance Setup')
ExhibitPreparation = Transition(label='Exhibit Preparation')
FinalApproval = Transition(label='Final Approval')

# Define the partial order
root = StrictPartialOrder(nodes=[CollectionSurvey, ProvenanceCheck, LegalReview, ScientificTest, MaterialAnalysis, OwnershipAudit, EthicalScreening, ConditionReport, ExpertConsultation, TransportPlanning, SecurePacking, CustomsClearance, InsuranceSetup, ExhibitPreparation, FinalApproval])

# Define the dependencies between nodes
root.order.add_edge(CollectionSurvey, ProvenanceCheck)
root.order.add_edge(CollectionSurvey, LegalReview)
root.order.add_edge(ProvenanceCheck, ScientificTest)
root.order.add_edge(ProvenanceCheck, MaterialAnalysis)
root.order.add_edge(LegalReview, OwnershipAudit)
root.order.add_edge(LegalReview, EthicalScreening)
root.order.add_edge(ScientificTest, ConditionReport)
root.order.add_edge(MaterialAnalysis, ConditionReport)
root.order.add_edge(OwnershipAudit, ExpertConsultation)
root.order.add_edge(EthicalScreening, ExpertConsultation)
root.order.add_edge(ConditionReport, TransportPlanning)
root.order.add_edge(ExpertConsultation, TransportPlanning)
root.order.add_edge(TransportPlanning, SecurePacking)
root.order.add_edge(SecurePacking, CustomsClearance)
root.order.add_edge(CustomsClearance, InsuranceSetup)
root.order.add_edge(InsuranceSetup, ExhibitPreparation)
root.order.add_edge(ExhibitPreparation, FinalApproval)