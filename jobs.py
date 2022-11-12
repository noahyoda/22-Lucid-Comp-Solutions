
def canDoJob(tools, count, job_tools, job_count):
    for i in range(len(job_tools)):
        tool = job_tools[i]
        if tool not in tools:
            return False
        tool_index = tools.index(tool)
        if int(job_count[i]) > int(count[tool_index]):
            return False
    return True

tools = input().split(', ')
tool_count = input().split(', ')
jobs = int(input())
job_list = []

for i in range(jobs):
    job = input()
    job_tools = input().split(', ')
    job_tool_count = input().split(', ')
    #check = all(item in tools for item in job_tools)
    check = canDoJob(tools, tool_count, job_tools, job_tool_count)
    if check:
        job_list.append(job)

job_list = sorted(job_list)
for j in job_list:
    print(j)