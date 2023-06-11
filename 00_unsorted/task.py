import requests
from typing import Any
from dataclasses import dataclass
import os
import datetime
import sys


@dataclass(slots=True)
class RespLeetCode:
    link:       str
    code:       str
    front_id:   int
    difficulty: str
    func_name:  str


def f00_today_task() -> dict[str, Any]:
    return {
        'url': 'https://leetcode.com/graphql/',
        'headers': {
            'content-type': 'application/json'
        },
        'json': {
            'query': '''
                        query questionOfToday
                        {
                            activeDailyCodingChallengeQuestion
                            {
                                link
                                date
                            }
                        }
                    ''',
        },
    }


def f01_data_for_request(task_name: str) -> dict[str, Any]:
    return {
        'url': 'https://leetcode.com/graphql/',
        'headers': {
            'content-type': 'application/json'
        },
        'json': {
            'query': '''
                        query questionContent($titleSlug: String!)
                        {
                            question(titleSlug: $titleSlug)
                            {
                                difficulty
                                questionId
                                questionFrontendId
                                content
                                codeSnippets
                                {
                                    langSlug
                                    code
                                }
                            }
                        }
                    ''',
            'variables': {
                'titleSlug': task_name
            },
        },
    }


def f02_handle_resp(name: str, resp_json: dict[str, Any]) -> RespLeetCode:
    py3_code = ''
    if code_by_leetcode := [el['code'] for el in resp_json['data']['question']['codeSnippets'] if
                            el['langSlug'] == 'python3']:
        py3_code = code_by_leetcode[0].replace('List', 'list').replace('\t', '    ')

    func_name = py3_code[py3_code.find('def ') + 4: py3_code.find('(self')] if py3_code else ''

    return RespLeetCode(
        link=f'https://leetcode.com/problems/{name}/description/',
        code=py3_code,
        front_id=resp_json['data']['question']['questionFrontendId'],
        difficulty=resp_json['data']['question']['difficulty'].lower()[:4],
        func_name=func_name,
    )


if __name__ == '__main__':
    # step_00 - argv or request for a_day_problem ######################################################################
    the_name: str = ''  # titleSlug
    if len(sys.argv) > 1:
        the_name = sys.argv[1].split('/')[4]
    else:
        response = requests.post(**f00_today_task())
        target_url = response.json()['data']['activeDailyCodingChallengeQuestion']['link']
        target_url = target_url[9:] if target_url.startswith('/problems') else target_url
        the_name = target_url.strip('/')

    # step_01 - fetch a info about problem #############################################################################
    response = requests.post(**f01_data_for_request(task_name=the_name))
    response_json = response.json()
    leet_resp: RespLeetCode = f02_handle_resp(the_name, response_json)

    # step_02 - get a file_id for new file #############################################################################
    tmp = sorted([el for el in os.listdir() if el[0] in '0123456789'])  # [901-medi-958.py, 902-medi-129.py, ...]
    next_file_id: int = int(tmp[0].split('-')[0]) - 1                   #  900

    # step_03 - load a template and update it ##########################################################################
    with open('_template.py', 'r') as temp_file:
        lines = temp_file.readlines()

    for idx, a_line in enumerate(lines):
        if a_line.startswith('# _link'):
            lines[idx] = f'# {leet_resp.link}\n'
        if a_line.startswith('# _git_commit'):
            today: str = datetime.date.today().isoformat().replace('-', '_')
            lines[idx] = f'# git commit -m "{today} - {next_file_id:>3} - {leet_resp.difficulty} - {leet_resp.front_id:>4}"\n'
        if a_line.startswith('# _class_Solution:'):
            lines[idx] = leet_resp.code
        if a_line.startswith('# _method2test'):
            lines[idx] = f'    method2test = Solution.{leet_resp.func_name}'

    # step_04 - write a new file #######################################################################################
    with open(f'{next_file_id}-{leet_resp.difficulty}-{leet_resp.front_id}.py', 'w') as out_file:
        out_file.write(''.join(lines))

    # TODO repalce .todo -> test_method_name
