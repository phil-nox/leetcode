#!/bin/bash
#                       <
#                     < <
# DOESN'T WORK !!!! < < <
#                     < <
#                       <
#
# use python3 task.py https://leetcode.com/problems/__nane_of_the_problem__
#

# example
# ./_old_task_by_link.sh https://leetcode.com/problems/subarray-sums-divisible-by-k/

# target        - url_to_leetcode with 'description/'
# data          - a tmp variable contains a response_received_by_curl
# m_prototype   - a method_prototype
# m_name        - a name_of_method
# problem_id    - a problem_id on leetcode
# difficulty    - a difficulty_tag on leetcode

# min_count     - a value for a new_file_name - 'max + 1'

target=$1

if [[ $1 != *"description/" ]];then
  target="$1description/"
fi

data=$(curl -s $target)
m_prototype=$(echo "$data" | grep -o 'class Solution:[^"]*' | grep -o 'def.*' | sed -e 's/List/list/g' -e 's/\\u003e/>/g')
m_name=$(echo $m_prototype | grep -Eo '.*\(' | sed -e 's/def //' -e 's/(//')
problem_id=$(echo "$data" | grep -o 'questionFrontendId":"[^"]*' | head -n1 | sed 's/questionFrontendId":"//')
problem_name=$(echo $target | awk -F "/" '{print $5}')
difficulty=$(echo "$data" | grep -o 'difficulty":"[^"]*' | head -n1 | sed 's/difficulty":"//' | tr '[:upper:]' '[:lower:]')
difficulty=${difficulty:0:4}

min_count=$(find . -maxdepth 1 -type f -name '[[:digit:]]*' | sort | head -n1 | grep -Eo '[0-9]+' | head -n1)

name_of_file="$(($min_count-1))-$difficulty-$problem_id.py"


cp _templace.py $name_of_file

sed -i '' -e "1s|^|# $target\n|" $name_of_file
sed -i '' -e  "s/pass/$m_prototype/" $name_of_file
sed -i '' -e  "s/__name_of_the_method__/$m_name/" $name_of_file

echo -e "new_file: \033[0;35m$name_of_file\033[0m by \033[0;36m$problem_name\033[0m"