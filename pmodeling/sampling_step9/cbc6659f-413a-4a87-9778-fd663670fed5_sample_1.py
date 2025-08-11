import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
expert_review = Transition(label='Expert Review')
legal_audit = Transition(label='Legal Audit')
condition_report = Transition(label='Condition Report')
carbon_dating = Transition(label='Carbon Dating')
ownership_verify = Transition(label='Ownership Verify')
historical_match = Transition(label='Historical Match')
customs_clearance = Transition(label='Customs Clearance')
risk_assessment = Transition(label='Risk Assessment')
ethics_approval = Transition(label='Ethics Approval')
restoration_plan = Transition(label='Restoration Plan')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')
exhibit_prep = Transition(label='Exhibit Prep')

skip = SilentTransition()

# Provenance Check
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan, expert_review, legal_audit, condition_report, carbon_dating, ownership_verify, historical_match, customs_clearance, risk_assessment, ethics_approval, restoration_plan, final_approval, catalog_entry, exhibit_prep])

# Legal Audit
legal_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_audit])

# Risk Assessment
risk_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assessment])

# Ethics Approval
ethics_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[ethics_approval])

# Restoration Plan
restoration_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan])

# Final Approval
final_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_approval])

# Catalog Entry
catalog_entry_loop = OperatorPOWL(operator=Operator.LOOP, children=[catalog_entry])

# Exhibit Prep
exhibit_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_prep])

root = StrictPartialOrder(nodes=[provenance_loop, legal_audit_loop, risk_assessment_loop, ethics_approval_loop, restoration_plan_loop, final_approval_loop, catalog_entry_loop, exhibit_prep_loop])
root.order.add_edge(provenance_loop, legal_audit_loop)
root.order.add_edge(legal_audit_loop, risk_assessment_loop)
root.order.add_edge(risk_assessment_loop, ethics_approval_loop)
root.order.add_edge(ethics_approval_loop, restoration_plan_loop)
root.order.add_edge(restoration_plan_loop, final_approval_loop)
root.order.add_edge(final_approval_loop, catalog_entry_loop)
root.order.add_edge(catalog_entry_loop, exhibit_prep_loop)