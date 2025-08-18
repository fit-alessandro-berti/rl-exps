from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
provenance_check = Transition(label='Provenance Check')
radiocarbon_test = Transition(label='Radiocarbon Test')
material_analysis = Transition(label='Material Analysis')
microscopic_scan = Transition(label='Microscopic Scan')
expert_review = Transition(label='Expert Review')
context_validation = Transition(label='Context Validation')
legal_audit = Transition(label='Legal Audit')
export_verify = Transition(label='Export Verify')
digital_imaging = Transition(label='Digital Imaging')
three_d_modeling = Transition(label='3D Modeling')
consensus_meeting = Transition(label='Consensus Meeting')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')
virtual_setup = Transition(label='Virtual Setup')
archival_backup = Transition(label='Archival Backup')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(nodes=[
    provenance_check,
    radiocarbon_test,
    material_analysis,
    microscopic_scan,
    expert_review,
    context_validation,
    legal_audit,
    export_verify,
    digital_imaging,
    three_d_modeling,
    consensus_meeting,
    final_approval,
    catalog_entry,
    virtual_setup,
    archival_backup
])

# Define the order (dependencies) between transitions
root.order.add_edge(provenance_check, radiocarbon_test)
root.order.add_edge(provenance_check, material_analysis)
root.order.add_edge(provenance_check, microscopic_scan)
root.order.add_edge(provenance_check, expert_review)
root.order.add_edge(provenance_check, context_validation)
root.order.add_edge(provenance_check, legal_audit)
root.order.add_edge(provenance_check, export_verify)
root.order.add_edge(provenance_check, digital_imaging)
root.order.add_edge(provenance_check, three_d_modeling)
root.order.add_edge(provenance_check, consensus_meeting)
root.order.add_edge(provenance_check, final_approval)
root.order.add_edge(provenance_check, catalog_entry)
root.order.add_edge(provenance_check, virtual_setup)
root.order.add_edge(provenance_check, archival_backup)

root.order.add_edge(radiocarbon_test, material_analysis)
root.order.add_edge(radiocarbon_test, microscopic_scan)
root.order.add_edge(radiocarbon_test, expert_review)
root.order.add_edge(radiocarbon_test, context_validation)
root.order.add_edge(radiocarbon_test, legal_audit)
root.order.add_edge(radiocarbon_test, export_verify)
root.order.add_edge(radiocarbon_test, digital_imaging)
root.order.add_edge(radiocarbon_test, three_d_modeling)
root.order.add_edge(radiocarbon_test, consensus_meeting)
root.order.add_edge(radiocarbon_test, final_approval)
root.order.add_edge(radiocarbon_test, catalog_entry)
root.order.add_edge(radiocarbon_test, virtual_setup)
root.order.add_edge(radiocarbon_test, archival_backup)

root.order.add_edge(material_analysis, microscopic_scan)
root.order.add_edge(material_analysis, expert_review)
root.order.add_edge(material_analysis, context_validation)
root.order.add_edge(material_analysis, legal_audit)
root.order.add_edge(material_analysis, export_verify)
root.order.add_edge(material_analysis, digital_imaging)
root.order.add_edge(material_analysis, three_d_modeling)
root.order.add_edge(material_analysis, consensus_meeting)
root.order.add_edge(material_analysis, final_approval)
root.order.add_edge(material_analysis, catalog_entry)
root.order.add_edge(material_analysis, virtual_setup)
root.order.add_edge(material_analysis, archival_backup)

root.order.add_edge(microscopic_scan, expert_review)
root.order.add_edge(microscopic_scan, context_validation)
root.order.add_edge(microscopic_scan, legal_audit)
root.order.add_edge(microscopic_scan, export_verify)
root.order.add_edge(microscopic_scan, digital_imaging)
root.order.add_edge(microscopic_scan, three_d_modeling)
root.order.add_edge(microscopic_scan, consensus_meeting)
root.order.add_edge(microscopic_scan, final_approval)
root.order.add_edge(microscopic_scan, catalog_entry)
root.order.add_edge(microscopic_scan, virtual_setup)
root.order.add_edge(microscopic_scan, archival_backup)

root.order.add_edge(expert_review, context_validation)
root.order.add_edge(expert_review, legal_audit)
root.order.add_edge(expert_review, export_verify)
root.order.add_edge(expert_review, digital_imaging)
root.order.add_edge(expert_review, three_d_modeling)
root.order.add_edge(expert_review, consensus_meeting)
root.order.add_edge(expert_review, final_approval)
root.order.add_edge(expert_review, catalog_entry)
root.order.add_edge(expert_review, virtual_setup)
root.order.add_edge(expert_review, archival_backup)

root.order.add_edge(context_validation, legal_audit)
root.order.add_edge(context_validation, export_verify)
root.order.add_edge(context_validation, digital_imaging)
root.order.add_edge(context_validation, three_d_modeling)
root.order.add_edge(context_validation, consensus_meeting)
root.order.add_edge(context_validation, final_approval)
root.order.add_edge(context_validation, catalog_entry)
root.order.add_edge(context_validation, virtual_setup)
root.order.add_edge(context_validation, archival_backup)

root.order.add_edge(legal_audit, export_verify)
root.order.add_edge(legal_audit, digital_imaging)
root.order.add_edge(legal_audit, three_d_modeling)
root.order.add_edge(legal_audit, consensus_meeting)
root.order.add_edge(legal_audit, final_approval)
root.order.add_edge(legal_audit, catalog_entry)
root.order.add_edge(legal_audit, virtual_setup)
root.order.add_edge(legal_audit, archival_backup)

root.order.add_edge(export_verify, digital_imaging)
root.order.add_edge(export_verify, three_d_modeling)
root.order.add_edge(export_verify, consensus_meeting)
root.order.add_edge(export_verify, final_approval)
root.order.add_edge(export_verify, catalog_entry)
root.order.add_edge(export_verify, virtual_setup)
root.order.add_edge(export_verify, archival_backup)

root.order.add_edge(digital_imaging, three_d_modeling)
root.order.add_edge(digital_imaging, consensus_meeting)
root.order.add_edge(digital_imaging, final_approval)
root.order.add_edge(digital_imaging, catalog_entry)
root.order.add_edge(digital_imaging, virtual_setup)
root.order.add_edge(digital_imaging, archival_backup)

root.order.add_edge(three_d_modeling, consensus_meeting)
root.order.add_edge(three_d_modeling, final_approval)
root.order.add_edge(three_d_modeling, catalog_entry)
root.order.add_edge(three_d_modeling, virtual_setup)
root.order.add_edge(three_d_modeling, archival_backup)

root.order.add_edge(consensus_meeting, final_approval)
root.order.add_edge(consensus_meeting, catalog_entry)
root.order.add_edge(consensus_meeting, virtual_setup)
root.order.add_edge(consensus_meeting, archival_backup)

root.order.add_edge(final_approval, catalog_entry)
root.order.add_edge(final_approval, virtual_setup)
root.order.add_edge(final_approval, archival_backup)

root.order.add_edge(catalog_entry, virtual_setup)
root.order.add_edge(catalog_entry, archival_backup)

root.order.add_edge(virtual_setup, archival_backup)