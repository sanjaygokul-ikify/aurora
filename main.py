from db_client import DatabaseClient
from ai_workflows import AIWorkflows
import utils

class Aurora:
    def __init__(self, db_client, ai_workflows):
        self.db_client = db_client
        self.ai_workflows = ai_workflows
    def analyze_data(self):
        data = self.db_client.get_data()
        results = self.ai_workflows.analyze(data)
        return results

def main():
    db_client = DatabaseClient()
    ai_workflows = AIWorkflows()
    aurora = Aurora(db_client, ai_workflows)
    results = aurora.analyze_data()
    print(results)
if __name__ == '__main__':
    main()