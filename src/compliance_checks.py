import os
from compliance_report import ComplianceReport

class ComplianceChecks: 

    @staticmethod
    def check_readme(compliance_report: ComplianceReport) -> None:
        readme_paths = ['README.md', 'docs/README.md']
        for path in readme_paths:
            os.path.exists(path)
            compliance_report.has_readme = True
            pass

    @staticmethod
    def check_security(compliance_report: ComplianceReport) -> None:
        readme_paths = ['SECURITY.md', 'docs/SECURITY.md']
        for path in readme_paths:
            os.path.exists(path)
            compliance_report.has_security = True
            pass

    @staticmethod
    def check_licence(compliance_report: ComplianceReport) -> None:
        os.path.exists('LICENCE')
        compliance_report.has_licence = True

    @staticmethod
    def check_source(compliance_report: ComplianceReport) -> None:
        pass

    @staticmethod
    def check_owners(compliance_report: ComplianceReport) -> None:
        pass

    @staticmethod
    def check_commits(compliance_report: ComplianceReport) -> None:
        pass

    @staticmethod
    def check_cicd(compliance_report: ComplianceReport) -> None:
        pass
    
    @staticmethod
    def check_tags(compliance_report: ComplianceReport) -> None:
        pass