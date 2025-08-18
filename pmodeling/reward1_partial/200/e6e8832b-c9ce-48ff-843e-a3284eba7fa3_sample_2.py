root = StrictPartialOrder(
    nodes=[
        Transition('Asset Listing'),
        Transition('Valuation Check'),
        Transition('Compliance Scan'),
        Transition('Legal Review'),
        Transition('Remote Audit'),
        Transition('Auction Setup'),
        Transition('Bid Monitoring'),
        Transition('Fraud Detection'),
        Transition('Ownership Transfer'),
        Transition('Payment Clearing'),
        Transition('Tax Calculation'),
        Transition('Fund Allocation'),
        Transition('Dispute Handling'),
        Transition('Report Generation'),
        Transition('Stakeholder Update')
    ],
    order=[
        ('Asset Listing', 'Valuation Check'),
        ('Valuation Check', 'Compliance Scan'),
        ('Compliance Scan', 'Legal Review'),
        ('Legal Review', 'Remote Audit'),
        ('Remote Audit', 'Auction Setup'),
        ('Auction Setup', 'Bid Monitoring'),
        ('Bid Monitoring', 'Fraud Detection'),
        ('Fraud Detection', 'Ownership Transfer'),
        ('Ownership Transfer', 'Payment Clearing'),
        ('Payment Clearing', 'Tax Calculation'),
        ('Tax Calculation', 'Fund Allocation'),
        ('Fund Allocation', 'Dispute Handling'),
        ('Dispute Handling', 'Report Generation'),
        ('Report Generation', 'Stakeholder Update')
    ]
)