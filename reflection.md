# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").


When I first ran the game in Streamlit, the interface worked but the gameplay had several bugs. One issue I noticed was that the hint messages were incorrect. For example, when my guess was higher than the secret number, the game told me to go higher instead of lower. Another bug occurred on even-numbered attempts where the secret number was converted into a string, which caused incorrect comparisons and sometimes prevented the correct guess from being detected. I also noticed that Hard mode used a smaller range than Normal mode, which made the harder difficulty easier instead of more challenging.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---I used GitHub Copilot inside VS Code and ChatGPT to help analyze the code and understand the bugs in the game. One correct suggestion from the AI was explaining that converting the secret number into a string on even-numbered attempts caused the comparison with the integer guess to fail. I verified this by looking at the code and noticing that parse_guess() always returns an integer while the secret becomes a string. This caused the normal win condition guess == secret to return false even when the numbers matched. One misleading suggestion from AI was focusing too much on the exception-handling block instead of identifying that the real issue was the unnecessary conversion of the secret number into a string earlier in the code.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
To confirm that the bugs were fixed, I ran the Streamlit game again and tested several guesses to see if the hints behaved correctly. I also used pytest to test the game logic functions independently. For example, I wrote a test where the guess was higher than the secret number and verified the function returned "Too High". Running pytest confirmed that all tests passed successfully. AI tools helped suggest the structure of the tests, but I verified the results by running the code and checking the output.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

I learned that Streamlit reruns the entire script every time the user interacts with the interface. Because of this behavior, session state is used to store important variables such as the secret number, attempts, and score so they do not reset each time the page updates. Without session state, the game would generate a new secret number every time a button is clicked. Session state allows the app to remember values between reruns and maintain the game progress.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

---

One habit I want to reuse in future projects is writing tests to verify that my code works correctly after making changes. This project also showed me that AI tools can be helpful for understanding code and suggesting fixes, but their suggestions should always be reviewed carefully. In the future, I will test AI-generated solutions more thoroughly before accepting them. This project changed the way I think about AI-generated code because it showed that AI can help with debugging but still requires human judgment and verification.

## AI Model Comparison (Bonus)

For one of the bugs involving the secret number being converted to a string on even-numbered attempts, I compared explanations from GitHub Copilot and ChatGPT. Copilot identified that the comparison between an integer guess and a string secret caused incorrect behavior, but its explanation focused mainly on the exception block. ChatGPT provided a clearer explanation about how Python compares different data types and why the equality check failed. I found ChatGPT’s explanation easier to understand because it clearly described the type mismatch and its effect on the win condition.