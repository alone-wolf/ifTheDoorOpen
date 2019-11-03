echo 'running>>> git remote -v'
git remote -v
echo ''
echo 'running>>> git fetch origin master:temp'
git fetch origin master:temp
echo ''
echo 'running>>> git branch'
git branch
echo ''
echo 'running>>> git diff temp'
git diff temp
echo ''
echo 'running>>> git merge temp'
git merge temp
echo ''
echo 'running>>> git branch -d temp'
git branch -d temp
echo ''
echo 'running>>> git branch'
git branch
