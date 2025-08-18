import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
IntakeDocument = Transition(label='Intake Document')
VisualInspect = Transition(label='Visual Inspect')
ImagingScan = Transition(label='Imaging Scan')
MaterialTest = Transition(label='Material Test')
DatabaseCross = Transition(label='Database Cross')
ProvenanceCheck = Transition(label='Provenance Check')
ExpertConsult = Transition(label='Expert Consult')
CarbonDating = Transition(label='Carbon Dating')
ForensicAnalyze = Transition(label='Forensic Analyze')
AnomalyReview = Transition(label='Anomaly Review')
RiskAssess = Transition(label='Risk Assess')
ReportDraft = Transition(label='Report Draft')
InsuranceQuote = Transition(label='Insurance Quote')
StoragePlan = Transition(label='Storage Plan')
FinalApproval = Transition(label='Final Approval')

# Define the partial order
root = StrictPartialOrder(nodes=[IntakeDocument, VisualInspect, ImagingScan, MaterialTest, DatabaseCross, ProvenanceCheck, ExpertConsult, CarbonDating, ForensicAnalyze, AnomalyReview, RiskAssess, ReportDraft, InsuranceQuote, StoragePlan, FinalApproval])

# Define the order dependencies
root.order.add_edge(IntakeDocument, VisualInspect)
root.order.add_edge(IntakeDocument, ImagingScan)
root.order.add_edge(VisualInspect, MaterialTest)
root.order.add_edge(ImagingScan, MaterialTest)
root.order.add_edge(MaterialTest, DatabaseCross)
root.order.add_edge(DatabaseCross, ProvenanceCheck)
root.order.add_edge(ProvenanceCheck, ExpertConsult)
root.order.add_edge(ExpertConsult, CarbonDating)
root.order.add_edge(CarbonDating, ForensicAnalyze)
root.order.add_edge(ForensicAnalyze, AnomalyReview)
root.order.add_edge(AnomalyReview, RiskAssess)
root.order.add_edge(RiskAssess, ReportDraft)
root.order.add_edge(ReportDraft, InsuranceQuote)
root.order.add_edge(InsuranceQuote, StoragePlan)
root.order.add_edge(StoragePlan, FinalApproval)

print(root)