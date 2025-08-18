import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
specimen_sampling = Transition(label='Specimen Sampling')
spectroscopy_test = Transition(label='Spectroscopy Test')
radiocarbon_date = Transition(label='Radiocarbon Date')
material_analysis = Transition(label='Material Analysis')
forensic_review = Transition(label='Forensic Review')
expert_consult = Transition(label='Expert Consult')
legal_verify = Transition(label='Legal Verify')
ownership_audit = Transition(label='Ownership Audit')
risk_assess = Transition(label='Risk Assess')
insurance_quote = Transition(label='Insurance Quote')
condition_report = Transition(label='Condition Report')
documentation = Transition(label='Documentation')
committee_review = Transition(label='Committee Review')
final_approval = Transition(label='Final Approval')

# Define silent transitions for concurrency
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define POWL model
root = StrictPartialOrder(nodes=[
    provenance_check,
    specimen_sampling,
    spectroscopy_test,
    radiocarbon_date,
    material_analysis,
    forensic_review,
    expert_consult,
    legal_verify,
    ownership_audit,
    risk_assess,
    insurance_quote,
    condition_report,
    documentation,
    committee_review,
    final_approval
])

# Define dependencies
root.order.add_edge(provenance_check, specimen_sampling)
root.order.add_edge(provenance_check, spectroscopy_test)
root.order.add_edge(provenance_check, radiocarbon_date)
root.order.add_edge(provenance_check, material_analysis)
root.order.add_edge(provenance_check, forensic_review)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(provenance_check, legal_verify)
root.order.add_edge(provenance_check, ownership_audit)
root.order.add_edge(provenance_check, risk_assess)
root.order.add_edge(provenance_check, insurance_quote)
root.order.add_edge(provenance_check, condition_report)
root.order.add_edge(provenance_check, documentation)
root.order.add_edge(provenance_check, committee_review)
root.order.add_edge(provenance_check, final_approval)

# Add concurrency
root.order.add_edge(specimen_sampling, skip1)
root.order.add_edge(spectroscopy_test, skip2)
root.order.add_edge(radiocarbon_date, skip3)

# Finalize the model
root.order.add_edge(skip1, material_analysis)
root.order.add_edge(skip2, forensic_review)
root.order.add_edge(skip3, expert_consult)
root.order.add_edge(material_analysis, legal_verify)
root.order.add_edge(forensic_review, ownership_audit)
root.order.add_edge(expert_consult, risk_assess)
root.order.add_edge(legal_verify, insurance_quote)
root.order.add_edge(ownership_audit, condition_report)
root.order.add_edge(risk_assess, committee_review)
root.order.add_edge(insurance_quote, documentation)
root.order.add_edge(condition_report, final_approval)
root.order.add_edge(committee_review, final_approval)