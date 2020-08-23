{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "\n",
    "Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter \n",
    "words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. \n",
    "Spaces will be included only when more than one word is present.\n",
    "\n",
    "Examples: \n",
    "spinWords( \"Hey fellow warriors\" ) => returns \"Hey wollef sroirraw\" \n",
    "spinWords( \"This is a test\") => returns \"This is a test\" \n",
    "spinWords( \"This is another test\" )=> returns \"This is rehtona test\"\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "def spin_words(sentence):\n",
    "    words=sentence.split()\n",
    "    spinned=[word if len(word)<5 else word[::-1] for word in words]\n",
    "    return ' '.join(spinned)\n",
    "\n",
    "# More simplified and eficient version\n",
    "def spin_words_v2(sentence):\n",
    "    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
