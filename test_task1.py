import subprocess


def test_hello_replit_output():
  # Run the script using subprocess and capture its output
  result = subprocess.run(["python", "task1.py"],
                          stdout=subprocess.PIPE,
                          text=True)
  output = result.stdout.strip()

  # Assert that the output is "Hello, Replit!"
  assert output == "Hello, Replit!"
