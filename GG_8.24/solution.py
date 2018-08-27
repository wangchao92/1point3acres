def solution(salary, target):
  salary_sorted = sorted(salary)
  prefix_sum = 0
  cap_num = len(salary)
  for s in salary_sorted:
    cap = (target - prefix_sum) / cap_num
    #print salary_sorted
    if cap <= s:
      return cap
    prefix_sum += s
    cap_num -= 1
  return "Impossible"
if __name__ == "__main__":
  salary = [100, 80, 70, 90, 110, 95, 88]
  target = 700
  print solution(salary, target)
