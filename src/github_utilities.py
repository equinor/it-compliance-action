from typing import Sequence
from compliance_report import ComplianceReport
from github import Github, Issue, Auth, Repository
import os


class ComplianceIssuePublisher:
    @staticmethod
    def publish_issues(
        repo: Repository.Repository, compliance_report: ComplianceReport
    ) -> None:
        active_issues = ComplianceIssuePublisher._get_compliance_issues(repo)
        for issue in compliance_report.issues:
            title = f"Compliance: {issue.title}"
            body: str = (
            f"---\n"
            f"id: {issue.id}\n"
            f"reference: {issue.reference}\n"
            f"---\n"
            f"**Description**\n\n"
            f"{issue.description.strip().replace('\n', '\n    ')}\n"
            )
            if any([i.title == title and i.body == body for i in active_issues]):
                continue
            repo.create_issue(title=title, body=body, labels=["EquinorCompliance"])

    @staticmethod
    def _get_compliance_issues(repo: Repository.Repository) -> Sequence[Issue.Issue]:
        return repo.get_issues(labels=["EquinorCompliance"]).get_page(0)
