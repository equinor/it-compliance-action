import os
from compliance_report import ComplianceReport
from github.Repository import Repository

class ComplianceChecks: 

    @staticmethod
    def check_readme(repo: Repository, compliance_report: ComplianceReport) -> None:
        readme_paths = ['README.md', 'docs/README.md']
        for path in readme_paths:
            if os.path.exists(path):
                compliance_report.has_readme = True
                break

    @staticmethod
    def check_security(repo: Repository, compliance_report: ComplianceReport) -> None:
        readme_paths = ['SECURITY.md', 'docs/SECURITY.md']
        for path in readme_paths:
            if os.path.exists(path):
                compliance_report.has_security = True
                break

    @staticmethod
    def check_licence(repo: Repository, compliance_report: ComplianceReport) -> None:
        if repo.visibility != 'public':
            return
        if os.path.exists('LICENCE'):
            compliance_report.has_licence = True

    @staticmethod
    def check_source(repo: Repository, compliance_report: ComplianceReport) -> None:
        pass

    @staticmethod
    def check_owners(repo: Repository, compliance_report: ComplianceReport) -> None:
        pass

    @staticmethod
    def check_commits(repo: Repository, compliance_report: ComplianceReport) -> None:
        pass

    @staticmethod
    def check_cicd(repo: Repository, compliance_report: ComplianceReport) -> None:
        pass
    
    @staticmethod
    def check_tags(repo: Repository, compliance_report: ComplianceReport) -> None:
        pass