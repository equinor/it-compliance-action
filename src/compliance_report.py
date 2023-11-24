import yaml
from typing import Generator

class ComplianceItem:
    
    def __init__(self, id: str, title: str, description: str, reference: str) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.reference = reference

class ComplianceReport:

    def __init__(self):
        self.has_readme = False
        self.has_security = False
        self.has_licence = False
        self.checklist = dict[str, ComplianceItem]()

        with open('src/compliance_checklist.yml', 'r') as stream:
            c = yaml.safe_load(stream)
            for i in c:
                self.checklist[i['id']] = ComplianceItem(i['id'], i['title'], i['description'], i['reference'])

    def __str__(self) -> str:
        return f'ComplianceReport(has_readme={self.has_readme},has_security={self.has_security},has_licence={self.has_licence})'
                

    
    @property
    def issues(self) -> Generator[ComplianceItem, None, None]:
        if not self.has_readme: 
            yield self.checklist['has_readme']
        if not self.has_security:
            yield self.checklist['has_security']
        if not self.has_licence:
            yield self.checklist['has_licence']

    


        
