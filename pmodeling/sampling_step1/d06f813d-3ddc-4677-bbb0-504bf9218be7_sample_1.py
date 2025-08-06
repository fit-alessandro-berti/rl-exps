import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
    provenance_check, specimen_sampling, spectroscopy_test, radiocarbon_date,
    material_analysis, forensic_review, expert_consult, legal_verify,
    ownership_audit, risk_assess, insurance_quote, condition_report,
    documentation, committee_review, final_approval
])

# Define the dependencies
root.order.add_edge(provenance_check, specimen_sampling)
root.order.add_edge(specimen_sampling, spectroscopy_test)
root.order.add_edge(specimen_sampling, radiocarbon_date)
root.order.add_edge(specimen_sampling, material_analysis)
root.order.add_edge(specimen_sampling, forensic_review)
root.order.add_edge(specimen_sampling, expert_consult)
root.order.add_edge(specimen_sampling, legal_verify)
root.order.add_edge(specimen_sampling, ownership_audit)
root.order.add_edge(specimen_sampling, risk_assess)
root.order.add_edge(specimen_sampling, insurance_quote)
root.order.add_edge(specimen_sampling, condition_report)
root.order.add_edge(specimen_sampling, documentation)
root.order.add_edge(specimen_sampling, committee_review)
root.order.add_edge(specimen_sampling, final_approval)