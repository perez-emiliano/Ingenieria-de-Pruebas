import sys, json, urllib.request
owner='perez-emiliano'
repo='Ingenieria-de-Pruebas'
base='https://api.github.com/repos/%s/%s' % (owner,repo)
# get runs
try:
    runs=json.load(urllib.request.urlopen(base+'/actions/runs'))['workflow_runs']
except Exception as e:
    print('ERROR_FETCH_RUNS',e)
    sys.exit(0)
# print summary
print('found_runs',len(runs))
# show first 10
for r in runs[:10]:
    print('RUN', r.get('id'), r.get('name'), r.get('head_sha')[:7], r.get('status'), r.get('conclusion'), r.get('html_url'))
# find run for recent commit (3d0ac9e)
target_prefix='3d0ac9e'
match=None
for r in runs:
    if r.get('head_sha','').startswith(target_prefix):
        match=r
        break
if not match:
    # fallback: take most recent
    match=runs[0] if runs else None
if not match:
    print('NO_MATCH')
    sys.exit(0)
run_id=match['id']
print('\nTARGET_RUN', run_id, match.get('name'), match.get('head_sha')[:7], match.get('html_url'))
# fetch jobs for run
jobs_url=base+f'/actions/runs/{run_id}/jobs'
jobs=json.load(urllib.request.urlopen(jobs_url)).get('jobs',[])
print('jobs_count', len(jobs))
for j in jobs:
    print('\nJOB', j.get('id'), j.get('name'), j.get('status'), j.get('conclusion'))
    steps=j.get('steps') or []
    for s in steps:
        print('  STEP', s.get('number'), s.get('name'), s.get('status'), s.get('conclusion'))
    # provide job html url if present
    if j.get('html_url'):
        print('  HTML', j.get('html_url'))
# try to download logs zip
logs_url=base+f'/actions/runs/{run_id}/logs'
print('\nLOGS_URL', logs_url)
try:
    req=urllib.request.Request(logs_url)
    r=urllib.request.urlopen(req)
    # if redirected to download, print final URL
    print('logs_response_url', r.geturl())
except Exception as e:
    print('ERROR_FETCH_LOGS', e)
