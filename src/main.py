import os
import logging
from compliance_checks import ComplianceChecks
from compliance_report import ComplianceReport
from github_utilities import ComplianceIssuePublisher
from github import Github, Issue, Auth




if __name__ == '__main__':
    #

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)


    acces_token = os.environ.get('GITHUB_TOKEN')
    repo_uri = os.environ.get('GITHUB_REPOSITORY')
    branch_name = os.environ.get('GITHUB_REF_NAME')
    if(repo_uri is None or acces_token is None or branch_name is None):
        raise Exception('Could not find repository')
    token = Auth.Token(acces_token)
    
    github = Github(auth=token)
    repo = github.get_repo(repo_uri)
    branch = repo.get_branch(branch_name)
    # Create the compliance report object
    compliance_report = ComplianceReport()

    # Run compliance checks
    ComplianceChecks.check_readme(repo, compliance_report)
    ComplianceChecks.check_security(repo, compliance_report)
    ComplianceChecks.check_licence(repo, compliance_report)
    ComplianceChecks.check_source(repo, compliance_report)
    ComplianceChecks.check_owners(repo, compliance_report)
    ComplianceChecks.check_commits(repo, compliance_report)
    ComplianceChecks.check_cicd(repo, compliance_report)
    ComplianceChecks.check_tags(repo, compliance_report)
    
    # Write report to output
    output_file_name = os.environ.get('GITHUB_OUTPUT', 'github_output.txt')
    with open(output_file_name, 'a') as output_file:
        output_file.write(f'compliance={compliance_report}\n')
        print(f'compliance={compliance_report}')


    # For each failed compliance item, if the issue does not already exist, create it
    ComplianceIssuePublisher.publish_issues(repo, compliance_report=compliance_report)
    print(0)