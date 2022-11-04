# MorseCoderDecoder (MorseCD) Survey

## Assigned: Friday, 4th November, 2022

## Due: Friday, 4th November, 2022

### Steps to Complete

* Fix the Morse Code encoder/ decoder code. (See more about this below!)

* Send a _family friendly_ joke to the class Discord channel to tell the others that your system is up and running.

* Start a class conversation over Discord entirely in Morse code!

* Respond to the questions in `writing/reflection.md`

### Instructions

Edit the Files in `morsecd/morsecd/` (i.e., `decode.py,encode.py,main.py`)
to allow for the following;

* Fix the generator functions in `encode.py` and `decode.py` to process text or morse code data.

* Allow program to run without errors.

* Try out an added challenge (see more about this below!)

### Extra Project Challenges
Feeling up to an extra challenge?! Try one or more of the following challenges!

 * Enable a message to be added at the command line in text or Morse code.
 * Add a file loader to being in text or Morse data to process. 
 * Add automatic messages such as, "I'm running late", "I'll call in soon" and similar so that a pre-programmed message can be quickly processed and sent if the user is busy.
 * Add an instant joke-creator function to provide coded jokes which are read-in from a file and encoded with a key stroke.
 * Add sound and digital voice. 
 * You think of something!

### Execution

* Get into the virtual environment:
   + `poetry install`
* To get online help for the project
   + `poetry run morsecd --help`. 
* To input a seed and run the project with a seed (such as 9)
   + `poetry run morsecd --message` (then enter a message in text or Morse code.)

### Submission

As you are working, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 25%]:**: For the repository associated
with this assignment students will receive a checkmark grade if their last before-the-deadline
build passes. This is only checking some baseline writing and commit requirements as well as correct
running of the program. An additional reduction will be given if the commit log shows a cluster
of commits at the end clearly used just to pass this requirement. An addition reduction
will also be given if there is no commit during work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark
grade when the responses to the writing questions presented in the `reflection.md` reveal
a proficiency of both writing skills and technical knowledge. To receive a checkmark grade,
the submitted writing should have correct spelling, grammar, and punctuation in addition
to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 50%]**: Students will receive a portion
of their assignment grade when their program implementation reveals that they have mastered
all of the technical knowledge and skills developed during the completion of this assignment.
As a part of this grade, the instructor will assess aspects of the programming including,
but not limited to, the completeness and the correctness of the program and the use of
effective source code comments.

## Seeking Assistance

Students who have questions about this project outside of the class or lab times are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.

## More Information

 + [How Does Morse Code Work?](https://www.youtube.com/watch?v=iy8BaMs_JuI)

 + [HOW IT WORKS: Morse Code (Older Black and White Training video)](https://www.youtube.com/watch?v=xsDk5_bktFo)

 + [• − − • • • − • − • • • − − • (VSauce)](https://www.youtube.com/watch?v=HY_OIwideLg)
