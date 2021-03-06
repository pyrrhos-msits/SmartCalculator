from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


def solve(case):
    return sum([int(x) for x in case.split()])


class CalcTest(StageTest):
    def generate(self) -> List[TestCase]:
        cases = ["0 1",
                 "1 0",
                 "2 3",
                 "100 123",
                 "-1 5",
                 "5 -2",
                 "-300 -400"]
        return [TestCase(stdin=case,
                         attach=solve(case))
                for case in cases]

    def check(self, reply: str, attach) -> CheckResult:
        return CheckResult(reply.strip() == str(attach).strip(), "")


if __name__ == '__main__':
    CalcTest("calculator.calculator").run_tests()
