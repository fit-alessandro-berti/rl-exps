import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) as objects
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
RadiocarbonTest = Transition(label='Radiocarbon Test')
StylisticReview = Transition(label='Stylistic Review')
ExpertConsult = Transition(label='Expert Consult')
DocumentAudit = Transition(label='Document Audit')
LegalVerify = Transition(label='Legal Verify')
ConditionReport = Transition(label='Condition Report')
DiscrepancyFlag = Transition(label='Discrepancy Flag')
ReExamination = Transition(label='Re-examination')
AlternativeSource = Transition(label='Alternative Source')
AcquisitionVote = Transition(label='Acquisition Vote')
CatalogEntry = Transition(label='Catalog Entry')
ExhibitPlan = Transition(label='Exhibit Plan')
FinalApproval = Transition(label='Final Approval')

# Define silent transitions (no action)
Skip1 = SilentTransition()
Skip2 = SilentTransition()
Skip3 = SilentTransition()

# Define the partial order structure
# Initial provenance check
initial_provenance = OperatorPOWL(operator=Operator.LOOP, children=[ProvenanceCheck])

# Material analysis
material_analysis = OperatorPOWL(operator=Operator.XOR, children=[MaterialScan, Skip1])

# Radiocarbon test
radiocarbon_test = OperatorPOWL(operator=Operator.XOR, children=[RadiocarbonTest, Skip2])

# Stylistic review
stylistic_review = OperatorPOWL(operator=Operator.XOR, children=[StylisticReview, Skip3])

# Expert consultation
expert_consult = OperatorPOWL(operator=Operator.XOR, children=[ExpertConsult, Skip3])

# Document audit
document_audit = OperatorPOWL(operator=Operator.XOR, children=[DocumentAudit, Skip3])

# Legal verification
legal_verify = OperatorPOWL(operator=Operator.XOR, children=[LegalVerify, Skip3])

# Condition report
condition_report = OperatorPOWL(operator=Operator.XOR, children=[ConditionReport, Skip3])

# Discrepancy flag
discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[DiscrepancyFlag, Skip3])

# Re-examination
re_examination = OperatorPOWL(operator=Operator.XOR, children=[ReExamination, Skip3])

# Alternative source
alternative_source = OperatorPOWL(operator=Operator.XOR, children=[AlternativeSource, Skip3])

# Acquisition vote
acquisition_vote = OperatorPOWL(operator=Operator.XOR, children=[AcquisitionVote, Skip3])

# Catalog entry
catalog_entry = OperatorPOWL(operator=Operator.XOR, children=[CatalogEntry, Skip3])

# Exhibit plan
exhibit_plan = OperatorPOWL(operator=Operator.XOR, children=[ExhibitPlan, Skip3])

# Final approval
final_approval = OperatorPOWL(operator=Operator.XOR, children=[FinalApproval, Skip3])

# Connect the nodes
root = StrictPartialOrder(nodes=[initial_provenance, material_analysis, radiocarbon_test, stylistic_review, expert_consult, document_audit, legal_verify, condition_report, discrepancy_flag, re_examination, alternative_source, acquisition_vote, catalog_entry, exhibit_plan, final_approval])

# Define the partial order edges
root.order.add_edge(initial_provenance, material_analysis)
root.order.add_edge(material_analysis, radiocarbon_test)
root.order.add_edge(radiocarbon_test, stylistic_review)
root.order.add_edge(stylistic_review, expert_consult)
root.order.add_edge(expert_consult, document_audit)
root.order.add_edge(document_audit, legal_verify)
root.order.add_edge(legal_verify, condition_report)
root.order.add_edge(condition_report, discrepancy_flag)
root.order.add_edge(discrepancy_flag, re_examination)
root.order.add_edge(re_examination, alternative_source)
root.order.add_edge(alternative_source, acquisition_vote)
root.order.add_edge(acquisition_vote, catalog_entry)
root.order.add_edge(catalog_entry, exhibit_plan)
root.order.add_edge(exhibit_plan, final_approval)

print(root)