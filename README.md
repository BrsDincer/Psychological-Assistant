
<img src="https://user-images.githubusercontent.com/81470496/235321390-9f4c388c-68d1-4dca-a185-59fe35eabd97.jpg" width=200>

# Psychological Assistant - AI LLM Project

Within the scope of psychology, it is an LLM AI-Bot research aimed at increasing human interaction with AI.


### Usage Notes

- It is local. The connection is established via the address "_127.0.0.1_".
- It is preferable to use it as "ready-to-use", as there is a pre-trained model and data collected for specific purposes.
- The main training data is the file "maindatapsy.csv".
- If you want to train the model based on your own data, follow the instructions and place your own file in the same file path, preserving the filename as "maindatapsy.csv".
- When you start the program without any problems, you will receive a disposable "username" and "password". To enter the panel, you need to note this. You get new login information on every launch.

### Notes Not to Ignore

- As the model is pre-processed, it is the user's responsibility to follow the advice given in response to questions.
- When you get unexpected answers, please seek support from your advisor or experts.
- It is in the experimental stage and is only ready for pre-use.
- Please report any external abuse.

### API KEY
- You should add your own _OpenAI_ API key in "tokeninit.txt" file. Make sure you enter a valid key or the program will not run.

## How To Use

**Please make sure that Python modules are installed on your system**
```
$> pip install -r requirements.txt
```

- Ready-To-Use:
Within the scope of the research, the model fed with the data in the "data" folder is ready to be run directly. You don't need any changes.

```
$> python _psyassistant.py
```
or
```
$> python3 _psyassistant.py
```

- For custom data:
The main training data is the file "maindatapsy.csv". Create your own data and replace it with this file (_maindatapsy.csv_) without changing the file format (_csv_) and the names (_QUESTION_ - _ANSWER_) of the columns. The filename (_maindatapsy.csv_) must remain the same. Run the latest script as follows.

```
$> python _psyassistant.py -f
```

## Video


https://user-images.githubusercontent.com/81470496/235314220-2b8174e6-75b0-421e-88f3-9d60b6441d5e.mp4


## Examples For Responses
<div>
  <img src="https://github.com/BrsDincer/PsychologicalAssistant/blob/main/psychological_assistant/images/example1.PNG?raw=true" width=208>
  <img src="https://github.com/BrsDincer/PsychologicalAssistant/blob/main/psychological_assistant/images/example2.PNG?raw=true" width=208>
  <img src="https://github.com/BrsDincer/PsychologicalAssistant/blob/main/psychological_assistant/images/example3.PNG?raw=true" width=208>
  <img src="https://github.com/BrsDincer/PsychologicalAssistant/blob/main/psychological_assistant/images/example4.PNG?raw=true" width=208>
</div>

## Example For Prompt-Output
<img src="https://github.com/BrsDincer/PsychologicalAssistant/blob/main/psychological_assistant/images/intropage.PNG?raw=true" width=700>

## Coder

[Baris Dincer](https://www.linkedin.com/in/brs-dincer/)

## For Bitcoin Donation

- 37kdD9qqyeiPTJM8nXXFwfCi684QdeVajp

