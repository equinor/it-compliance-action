import os
from compliance_checks import ComplianceChecks
from compliance_report import ComplianceReport
from github_utilities import ComplianceIssuePublisher



if __name__ == '__main__':
    # Create the compliance report object
    compliance_report = ComplianceReport()

    # Run compliance checks
    ComplianceChecks.check_readme(compliance_report)
    ComplianceChecks.check_security(compliance_report)
    ComplianceChecks.check_licence(compliance_report)
    ComplianceChecks.check_source(compliance_report)
    ComplianceChecks.check_owners(compliance_report)
    ComplianceChecks.check_commits(compliance_report)
    ComplianceChecks.check_cicd(compliance_report)
    ComplianceChecks.check_tags(compliance_report)
    
    # Write report to output
    output_file_name = os.environ.get('GITHUB_OUTPUT', 'github_output.txt')
    with open(output_file_name, 'a') as output_file:
        output_file.write(f'compliance={compliance_report}\n')
        print(f'compliance={compliance_report}')


    # For each failed compliance item, if the issue does not already exist, create it
    issue_publisher = ComplianceIssuePublisher()
    issue_publisher.publish_issues(compliance_report=compliance_report)