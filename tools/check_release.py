"""Fail safely while institutional pages contain unresolved publication blockers."""
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
blocked=[]
for p in root.rglob('*.html'):
 text=p.read_text()
 if '[PENDING:' in text or 'DRAFT FOR REVIEW' in text:
  blocked.append(str(p.relative_to(root)))
if blocked:
 print('RELEASE BLOCKED: resolve operator information and review institutional drafts:')
 print('\n'.join(blocked))
 sys.exit(1)
print('Draft check passed. Explicit owner approval and the release checklist are still required.')
