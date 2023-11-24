from typing import Sequence
from compliance_report import ComplianceReport
from github import Github, Issue, Auth
import os

class ComplianceIssuePublisher: 

    def __init__(self) -> None:
        acces_token = os.environ.get('GITHUB_TOKEN')
        repo_uri = os.environ.get('GITHUB_REPOSITORY')
        if(repo_uri is None or acces_token is None):
            raise Exception('Could not find repository')
        token = Auth.Token(acces_token)
        
        self.github = Github(auth=token)
        self.repo = self.github.get_repo(repo_uri)

    def publish_issues(self, compliance_report: ComplianceReport) -> None:
        active_issues = self._get_compliance_issues()
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
            self.repo.create_issue(title=title, body=body, labels=['compliance'])
        


    def _get_compliance_issues(self) -> Sequence[Issue.Issue]:
        pass
        return self.repo.get_issues(labels=['compliance']).get_page(0)
    
   
        
