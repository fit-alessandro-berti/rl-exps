import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the workflow
workflow = StrictPartialOrder(
    nodes=[
        provenance_check,
        material_scan,
        expert_review,
        legal_audit,
        condition_report,
        carbon_dating,
        ownership_verify,
        historical_match,
        customs_clearance,
        risk_assessment,
        ethics_approval,
        restoration_plan,
        final_approval,
        catalog_entry,
        exhibit_prep
    ]
)

# Define the order of execution
workflow.order.add_edge(provenance_check, material_scan)
workflow.order.add_edge(material_scan, expert_review)
workflow.order.add_edge(expert_review, legal_audit)
workflow.order.add_edge(legal_audit, condition_report)
workflow.order.add_edge(condition_report, carbon_dating)
workflow.order.add_edge(carbon_dating, ownership_verify)
workflow.order.add_edge(ownership_verify, historical_match)
workflow.order.add_edge(historical_match, customs_clearance)
workflow.order.add_edge(customs_clearance, risk_assessment)
workflow.order.add_edge(risk_assessment, ethics_approval)
workflow.order.add_edge(ethics_approval, restoration_plan)
workflow.order.add_edge(restoration_plan, final_approval)
workflow.order.add_edge(final_approval, catalog_entry)
workflow.order.add_edge(catalog_entry, exhibit_prep)

# Set the root of the POWL model
root = workflow