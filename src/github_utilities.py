from typing import Sequence
from compliance_report import ComplianceReport
from github import Github, Issue, Auth, Repository
import os

class ComplianceIssuePublisher: 

    @staticmethod
    def publish_issues(repo: Repository.Repository, compliance_report: ComplianceReport) -> None:
        active_issues = ComplianceIssuePublisher._get_compliance_issues(repo)
        found_issues = [x for x in compliance_report.issues]
        for issue in found_issues:
            title = f'Compliance: {issue.title}'
            body = f'''---
id: {issue.id}
reference: {issue.reference}
---
**Description**

{issue.description}
'''
            if any([i.title is title and i.body is body for i in active_issues]):
                pass
            repo.create_issue(title=title, body=body, labels=['EquinorCompliance'])
        

    @staticmethod
    def _get_compliance_issues(repo: Repository.Repository) -> Sequence[Issue.Issue]:
        return repo.get_issues(labels=['EquinorCompliance']).get_page(0)
    
   
        
