{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Data for Sentiment Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['A beautiful and very entertaining animated sequel that makes me have a nice time for a magical hour and a half.\\n', 'Frozen II may sing about change, but that progress is what you project onto it.\\n']\n"
     ]
    }
   ],
   "source": [
    "#Import the movie reviews corpus\n",
    "with open(\"Frozen2.txt\", 'r') as fh:  \n",
    "    reviews = fh.readlines()\n",
    "print(reviews[:2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sentiments by Review"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'textblob'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-180aed7d9a09>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#install textblob if not already installed using \"pip install -U textblob\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mtextblob\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mTextBlob\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'{:40} : {:10} : {:10}'\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Review\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"Polarity\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"Subjectivity\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'textblob'"
     ]
    }
   ],
   "source": [
    "#install textblob if not already installed using \"pip install -U textblob\"\n",
    "from textblob import TextBlob\n",
    "\n",
    "print('{:40} : {:10} : {:10}'.format(\"Review\", \"Polarity\", \"Subjectivity\") )\n",
    "\n",
    "for review in reviews:\n",
    "    #Find sentiment of a review\n",
    "    sentiment = TextBlob(review)\n",
    "    #Print individual sentiments\n",
    "    print('{:40} :   {: 01.2f}    :   {:01.2f}'.format(review[:40]\\\n",
    "                , sentiment.polarity, sentiment.subjectivity) )\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 02_04 Summarizing Sentiment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'TextBlob' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-8dfc39188f2d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;31m#Categorize each review\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mreview\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mreviews\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m     \u001b[0msentiment\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mTextBlob\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mreview\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[1;31m#Custom formula to convert polarity\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'TextBlob' is not defined"
     ]
    }
   ],
   "source": [
    "\n",
    "#Categorize Polarity into Positive, Neutral or Negative\n",
    "labels = [\"Negative\", \"Neutral\", \"Positive\"]\n",
    "#Initialize count array\n",
    "values =[0,0,0]\n",
    "\n",
    "#Categorize each review\n",
    "for review in reviews:\n",
    "    sentiment = TextBlob(review)\n",
    "    \n",
    "    #Custom formula to convert polarity \n",
    "    # 0 = (Negative) 1 = (Neutral) 2=(Positive)\n",
    "    polarity = round(( sentiment.polarity + 1 ) * 3 ) % 3\n",
    "    \n",
    "    #add the summary array\n",
    "    values[polarity] = values[polarity] + 1\n",
    "    \n",
    "print(\"Final summarized counts :\", values)\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "#Set colors by label\n",
    "colors=[\"Yellow\",\"Azure\",\"Blue\"]\n",
    "\n",
    "print(\"\\n Pie Representation \\n-------------------\")\n",
    "#Plot a pie chart\n",
    "plt.pie(values, labels=labels, colors=colors, \\\n",
    "        autopct='%1.1f%%', shadow=True, startangle=140)\n",
    "plt.axis('equal')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
