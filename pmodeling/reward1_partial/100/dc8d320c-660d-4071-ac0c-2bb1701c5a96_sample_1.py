root = StrictPartialOrder(nodes=[
    Transition(label='Artifact Intake'),
    Transition(label='Provenance Check'),
    Transition(label='Material Testing'),
    Transition(label='Historical Review'),
    Transition(label='Expert Interview'),
    Transition(label='Condition Audit'),
    Transition(label='Digital Catalog'),
    Transition(label='Forgery Detection'),
    Transition(label='Legal Compliance'),
    Transition(label='Restoration Plan'),
    Transition(label='Valuation Report'),
    Transition(label='Market Analysis'),
    Transition(label='Final Approval'),
    Transition(label='Sale Preparation'),
    Transition(label='Client Notification')
])

root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Material Testing'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Historical Review'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Expert Interview'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Condition Audit'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Digital Catalog'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Forgery Detection'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Artifact Intake'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Material Testing'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Historical Review'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Expert Interview'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Condition Audit'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Digital Catalog'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Forgery Detection'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Material Testing'), Transition(label='Historical Review'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Expert Interview'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Condition Audit'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Digital Catalog'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Forgery Detection'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Material Testing'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Historical Review'), Transition(label='Expert Interview'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Condition Audit'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Digital Catalog'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Forgery Detection'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Historical Review'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Condition Audit'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Digital Catalog'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Forgery Detection'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Expert Interview'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Condition Audit'), Transition(label='Digital Catalog'))
root.order.add_edge(Transition(label='Condition Audit'), Transition(label='Forgery Detection'))
root.order.add_edge(Transition(label='Condition Audit'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Condition Audit'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Condition Audit'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Condition Audit'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Condition Audit'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Condition Audit'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Condition Audit'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Digital Catalog'), Transition(label='Forgery Detection'))
root.order.add_edge(Transition(label='Digital Catalog'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Digital Catalog'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Digital Catalog'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Digital Catalog'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Digital Catalog'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Digital Catalog'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Digital Catalog'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Forgery Detection'), Transition(label='Legal Compliance'))
root.order.add_edge(Transition(label='Forgery Detection'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Forgery Detection'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Forgery Detection'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Forgery Detection'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Forgery Detection'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Forgery Detection'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Legal Compliance'), Transition(label='Restoration Plan'))
root.order.add_edge(Transition(label='Legal Compliance'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Legal Compliance'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Legal Compliance'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Legal Compliance'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Legal Compliance'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Restoration Plan'), Transition(label='Valuation Report'))
root.order.add_edge(Transition(label='Restoration Plan'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Restoration Plan'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Restoration Plan'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Restoration Plan'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Valuation Report'), Transition(label='Market Analysis'))
root.order.add_edge(Transition(label='Valuation Report'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Valuation Report'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Valuation Report'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Market Analysis'), Transition(label='Final Approval'))
root.order.add_edge(Transition(label='Market Analysis'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Market Analysis'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Final Approval'), Transition(label='Sale Preparation'))
root.order.add_edge(Transition(label='Final Approval'), Transition(label='Client Notification'))

root.order.add_edge(Transition(label='Sale Preparation'), Transition(label='Client Notification'))