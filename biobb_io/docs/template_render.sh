DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
parent_dir="$(dirname $DIR)"
REPOSITORY="$(dirname $parent_dir)"
#read -p "Repository absolute path : " REPOSITORY
echo $REPOSITORY
repo_name=$(basename $REPOSITORY)
echo $repo_name
read -p "Version number ie 0.1.2 : " version
sed "s/{{version}}/${version}/g" $REPOSITORY/$repo_name/docs/README_template.md > $REPOSITORY/$repo_name/docs/source/readme.md
cp $REPOSITORY/$repo_name/docs/source/readme.md $REPOSITORY/README.md
sed 's/%%bash//g' $REPOSITORY/$repo_name/docs/command_line_template.rst > $REPOSITORY/$repo_name/docs/source/command_line.rst
sed -i '' 's/.. code:: bash/Command:\
\
.. code:: bash/g' $REPOSITORY/$repo_name/docs/source/command_line.rst
