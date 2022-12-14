class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for number in range(1, n+1):
            divisible_by_3 = (number % 3 == 0)
            divisible_by_5 = (number % 5 == 0)
            number_ans_str = ""
            if divisible_by_3:
                number_ans_str += "Fizz"
            if divisible_by_5:
                number_ans_str += "Buzz"
            if not number_ans_str:
                number_ans_str = str(number)
        answer.append(number_ans_str)  

     return answer
