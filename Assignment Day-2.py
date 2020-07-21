{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello       \n",
      "Everyone\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello \\\n",
    "      \\nEveryone\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Here I am trying to practice th things I learned today.'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"Here I am trying to practice th things I learned today.\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I want some \tSPACE\n"
     ]
    }
   ],
   "source": [
    "print(\"I want some \\tSPACE\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I want to print this on next line: \n",
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"I want to print this on next line: \\nHello World\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The car by Maruti which is Swift Vxi costs around  8\n"
     ]
    }
   ],
   "source": [
    "make=\"Maruti\"\n",
    "Model=\"Swift Vxi\"\n",
    "Price=8 \n",
    "\n",
    "print(\"The car by\", make, \"which is\",Model,\"costs around \",Price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The car by Maruti which is Swift Vxi costs around 8.25 Lakhs\n"
     ]
    }
   ],
   "source": [
    "make=\"Maruti\"\n",
    "Model=\"Swift Vxi\"\n",
    "Price=8.25 \n",
    "\n",
    "print(\"The car by %s which is %s costs around %0.2f Lakhs\" %(make,Model,Price))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square of a is 100\n",
      "Sum of a and b is 25\n",
      "'a' divided by 'b' is 0.60\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=15\n",
    "c=20\n",
    "Sq=a**2\n",
    "\n",
    "print(\"Square of a is %d\" %Sq)\n",
    "a+=b\n",
    "print (\"Sum of a and b is %d\" %a)\n",
    "b/=a\n",
    "print(\"'a' divided by 'b' is %0.2f\" %b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=10\n",
    "b=15\n",
    "c=20\n",
    "\n",
    "a<=b & c>b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str1 = \"My name is XYZ\" \n",
    "\"b\" in str1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10>8<9"
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
