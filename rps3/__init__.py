import check50
from re import escape


@check50.check()
def exists():
    """rps3.py exists"""
    check50.exists("rps3.py")

@check50.check(exists)
def test_invalid_letter():
    """rejects invalid letter a"""
    input = "a"
    output = "Make sure it is a positive odd integer"
    check50.run("python3 rps3.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()

@check50.check(exists)
def test_invalid_number():
    """rejects invalid number 2"""
    input = "2"
    output = "Make sure it is a positive odd integer"
    check50.run("python3 rps3.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()

@check50.check(exists)
def test_p1isROCK():
    """input of \"R\" for Player 1 is accepted"""
    input1 = "1"
    input2 = "R"
    output = "Tie\n---\nRound 1\nPlayer 1 Score: 0, Computer Score: 0\nPlayer 1: "
    check50.run("python3 rps3.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdout(regex(output), output, regex=True).kill()

@check50.check(exists)
def test_p1isPAPER():
    """input of \"p\" for Player 1 is accepted"""
    input1 = "1"
    input2 = "p"
    output = "Computer: r\nPlayer 1 wins the round\n---\nFinal Score: Player 1: 1, Computer: 0\nPlayer 1 Wins the game\n---\nDetailed Game Results:\nRound 1: Player 1 wins the round"
    check50.run("python3 rps3.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdout(regex(output), output, regex=True).kill()

@check50.check(exists)
def test_p1isSCISSOR():
    """input of \"s\" for Player 1 is accepted"""
    input1 = "1"
    input2 = "s"
    output = "Computer: r\nComputer wins the round\n---\nFinal Score: Player 1: 0, Computer: 1\nComputer Wins the game\n---\nDetailed Game Results:\nRound 1: Computer wins the round"
    check50.run("python3 rps3.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdout(regex(output), output, regex=True).kill() 

@check50.check(exists)
def test_invalid():
    """input of \"f\" for Player 1 results in \"Make sure to enter r for rock, p for paper and s for scissors\""""
    input1 = "1"
    input2 = "f"
    output = "Make sure to enter r for rock, p for paper and s for scissors\nPlayer 1: "
    check50.run("python3 rps3.py").stdin(input1, prompt=True).stdin(input2, prompt=True).stdout(regex(output), output, regex=True).kill()  

@check50.check(exists)
def main_function():
    """main function exists"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py main_function").exit(0)


@check50.check(exists)
def custom_function():
    """implemented at least 3 top-level functions other than main"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py custom_functions").exit(0)

def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
