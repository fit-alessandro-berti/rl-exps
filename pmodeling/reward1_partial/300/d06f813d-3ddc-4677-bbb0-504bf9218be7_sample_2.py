from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
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

# Define the dependencies
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

# Return the root
return root