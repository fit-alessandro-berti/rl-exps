import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, specimen_sampling])
spectroscopy_loop = OperatorPOWL(operator=Operator.LOOP, children=[spectroscopy_test, radiocarbon_date, material_analysis])
forensic_loop = OperatorPOWL(operator=Operator.LOOP, children=[forensic_review, expert_consult, legal_verify, ownership_audit])
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, insurance_quote, condition_report])
documentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[documentation, committee_review, final_approval])

root = StrictPartialOrder(nodes=[provenance_loop, spectroscopy_loop, forensic_loop, risk_loop, documentation_loop])
root.order.add_edge(provenance_loop, spectroscopy_loop)
root.order.add_edge(spectroscopy_loop, forensic_loop)
root.order.add_edge(forensic_loop, risk_loop)
root.order.add_edge(risk_loop, documentation_loop)