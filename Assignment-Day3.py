{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Insert the number to check whether it is prime or not   5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Given number is a prime number\n"
     ]
    }
   ],
   "source": [
    "'''Program to check whether the given number is prime or not'''\n",
    "n = int(input(\"Insert the number to check whether it is prime or not  \"))\n",
    "if n > 1:\n",
    "   for d in range(2,n):\n",
    "       if (n % d) == 0:\n",
    "           print(\"Given number is not a prime number \")\n",
    "           break\n",
    "   else:\n",
    "       print(\"Given number is a prime number\")\n",
    "       \n",
    "else:\n",
    "   print(\"Given number is not a prime number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the number  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "sum upto 1 numbers is 1\n",
      "\n",
      "sum upto 2 numbers is 3\n",
      "\n",
      "sum upto 3 numbers is 6\n",
      "\n",
      "sum upto 4 numbers is 10\n",
      "\n",
      "sum upto 5 numbers is 15\n",
      "\n",
      "Required sum of 5 numbers is 15 .\n"
     ]
    }
   ],
   "source": [
    "'''Program to get sum of n numbers'''\n",
    "\n",
    "i=1\n",
    "sum1 = 0\n",
    "n = int(input(\"Enter the number \"))\n",
    "while n>=i>=1 : \n",
    "    sum1 = sum1 + i\n",
    "    print (\"\\nsum upto %d numbers is %d\" %(i,sum1)  )\n",
    "    i+=1\n",
    "    \n",
    "print(\"\\nRequired sum of %d numbers is %d .\"%(n,sum1))"
   ]
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
