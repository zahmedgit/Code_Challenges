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
    "You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an \n",
    "appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk \n",
    "Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing \n",
    "directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it \n",
    "takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will \n",
    "take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. \n",
    "Return false otherwise.\n",
    "\n",
    "Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). \n",
    "It will never give you an empty array (that's not a walk, that's standing still!).\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "def is_valid_walk(walk):\n",
    "    valid=False\n",
    "    directions={'n':0,'s':0,'w':0,'e':0}\n",
    "    if len(walk)!=10:\n",
    "        return valid\n",
    "    else:\n",
    "        for _ in walk:\n",
    "            directions[_]+=1\n",
    "        if (directions['n']==directions['s'] and directions['w']==directions['e']):\n",
    "            valid=True\n",
    "    return valid"
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
