{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.56413411, 0.00853504, 0.88934185, 0.72377651],\n",
       "       [0.58288996, 0.90933422, 0.06746411, 0.2890998 ],\n",
       "       [0.13684485, 0.75629414, 0.53483564, 0.64206998],\n",
       "       [0.03629208, 0.95982606, 0.55795755, 0.59782197],\n",
       "       [0.34958169, 0.80342504, 0.44659039, 0.45268415]])"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n = np.random.rand(5,4)\n",
    "n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "list_rows = 'a b c d e'.split()\n",
    "list_cols = 'w x y z'.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>0.136845</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.642070</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>0.036292</td>\n",
       "      <td>0.959826</td>\n",
       "      <td>0.557958</td>\n",
       "      <td>0.597822</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>e</th>\n",
       "      <td>0.349582</td>\n",
       "      <td>0.803425</td>\n",
       "      <td>0.446590</td>\n",
       "      <td>0.452684</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          w         x         y         z\n",
       "a  0.564134  0.008535  0.889342  0.723777\n",
       "b  0.582890  0.909334  0.067464  0.289100\n",
       "c  0.136845  0.756294  0.534836  0.642070\n",
       "d  0.036292  0.959826  0.557958  0.597822\n",
       "e  0.349582  0.803425  0.446590  0.452684"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(n, list_rows, list_cols)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "w    0.564134\n",
       "x    0.008535\n",
       "y    0.889342\n",
       "z    0.723777\n",
       "Name: a, dtype: float64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc['a']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          w         x         y         z\n",
       "a  0.564134  0.008535  0.889342  0.723777\n",
       "b  0.582890  0.909334  0.067464  0.289100"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[['a','b']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>0.136845</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.64207</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          w         x         y        z\n",
       "c  0.136845  0.756294  0.534836  0.64207"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[2:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "df2 = df.loc[['a','b']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          w         x         y         z\n",
       "a  0.564134  0.008535  0.889342  0.723777\n",
       "b  0.582890  0.909334  0.067464  0.289100"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          w         x\n",
       "a  0.564134  0.008535\n",
       "b  0.582890  0.909334"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[['a','b'],['w','x']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          w         x\n",
       "a  0.564134  0.008535\n",
       "b  0.582890  0.909334"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[0:2,0:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "      <th>new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "      <td>0.572669</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "      <td>1.492224</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>0.136845</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.642070</td>\n",
       "      <td>0.893139</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>0.036292</td>\n",
       "      <td>0.959826</td>\n",
       "      <td>0.557958</td>\n",
       "      <td>0.597822</td>\n",
       "      <td>0.996118</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>e</th>\n",
       "      <td>0.349582</td>\n",
       "      <td>0.803425</td>\n",
       "      <td>0.446590</td>\n",
       "      <td>0.452684</td>\n",
       "      <td>1.153007</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          w         x         y         z       new\n",
       "a  0.564134  0.008535  0.889342  0.723777  0.572669\n",
       "b  0.582890  0.909334  0.067464  0.289100  1.492224\n",
       "c  0.136845  0.756294  0.534836  0.642070  0.893139\n",
       "d  0.036292  0.959826  0.557958  0.597822  0.996118\n",
       "e  0.349582  0.803425  0.446590  0.452684  1.153007"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['new'] = df['w']+df['x']\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>0.136845</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.642070</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>0.036292</td>\n",
       "      <td>0.959826</td>\n",
       "      <td>0.557958</td>\n",
       "      <td>0.597822</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>e</th>\n",
       "      <td>0.349582</td>\n",
       "      <td>0.803425</td>\n",
       "      <td>0.446590</td>\n",
       "      <td>0.452684</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          w         x         y         z\n",
       "a  0.564134  0.008535  0.889342  0.723777\n",
       "b  0.582890  0.909334  0.067464  0.289100\n",
       "c  0.136845  0.756294  0.534836  0.642070\n",
       "d  0.036292  0.959826  0.557958  0.597822\n",
       "e  0.349582  0.803425  0.446590  0.452684"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop('new', axis=1, inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "states = 'ab cd ef gh ij'.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "      <th>states</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "      <td>ab</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "      <td>cd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>0.136845</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.642070</td>\n",
       "      <td>ef</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>0.036292</td>\n",
       "      <td>0.959826</td>\n",
       "      <td>0.557958</td>\n",
       "      <td>0.597822</td>\n",
       "      <td>gh</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>e</th>\n",
       "      <td>0.349582</td>\n",
       "      <td>0.803425</td>\n",
       "      <td>0.446590</td>\n",
       "      <td>0.452684</td>\n",
       "      <td>ij</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          w         x         y         z states\n",
       "a  0.564134  0.008535  0.889342  0.723777     ab\n",
       "b  0.582890  0.909334  0.067464  0.289100     cd\n",
       "c  0.136845  0.756294  0.534836  0.642070     ef\n",
       "d  0.036292  0.959826  0.557958  0.597822     gh\n",
       "e  0.349582  0.803425  0.446590  0.452684     ij"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['states'] = states\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "      <th>states</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "      <td>ab</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>b</td>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "      <td>cd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>c</td>\n",
       "      <td>0.136845</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.642070</td>\n",
       "      <td>ef</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>d</td>\n",
       "      <td>0.036292</td>\n",
       "      <td>0.959826</td>\n",
       "      <td>0.557958</td>\n",
       "      <td>0.597822</td>\n",
       "      <td>gh</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>e</td>\n",
       "      <td>0.349582</td>\n",
       "      <td>0.803425</td>\n",
       "      <td>0.446590</td>\n",
       "      <td>0.452684</td>\n",
       "      <td>ij</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  index         w         x         y         z states\n",
       "0     a  0.564134  0.008535  0.889342  0.723777     ab\n",
       "1     b  0.582890  0.909334  0.067464  0.289100     cd\n",
       "2     c  0.136845  0.756294  0.534836  0.642070     ef\n",
       "3     d  0.036292  0.959826  0.557958  0.597822     gh\n",
       "4     e  0.349582  0.803425  0.446590  0.452684     ij"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>level_0</th>\n",
       "      <th>index</th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "      <th>states</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>a</td>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "      <td>ab</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>b</td>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "      <td>cd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>c</td>\n",
       "      <td>0.136845</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.642070</td>\n",
       "      <td>ef</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>d</td>\n",
       "      <td>0.036292</td>\n",
       "      <td>0.959826</td>\n",
       "      <td>0.557958</td>\n",
       "      <td>0.597822</td>\n",
       "      <td>gh</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>e</td>\n",
       "      <td>0.349582</td>\n",
       "      <td>0.803425</td>\n",
       "      <td>0.446590</td>\n",
       "      <td>0.452684</td>\n",
       "      <td>ij</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   level_0 index         w         x         y         z states\n",
       "0        0     a  0.564134  0.008535  0.889342  0.723777     ab\n",
       "1        1     b  0.582890  0.909334  0.067464  0.289100     cd\n",
       "2        2     c  0.136845  0.756294  0.534836  0.642070     ef\n",
       "3        3     d  0.036292  0.959826  0.557958  0.597822     gh\n",
       "4        4     e  0.349582  0.803425  0.446590  0.452684     ij"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.reset_index(inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>level_0</th>\n",
       "      <th>index</th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>states</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>ab</th>\n",
       "      <td>0</td>\n",
       "      <td>a</td>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cd</th>\n",
       "      <td>1</td>\n",
       "      <td>b</td>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ef</th>\n",
       "      <td>2</td>\n",
       "      <td>c</td>\n",
       "      <td>0.136845</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.642070</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>gh</th>\n",
       "      <td>3</td>\n",
       "      <td>d</td>\n",
       "      <td>0.036292</td>\n",
       "      <td>0.959826</td>\n",
       "      <td>0.557958</td>\n",
       "      <td>0.597822</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ij</th>\n",
       "      <td>4</td>\n",
       "      <td>e</td>\n",
       "      <td>0.349582</td>\n",
       "      <td>0.803425</td>\n",
       "      <td>0.446590</td>\n",
       "      <td>0.452684</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        level_0 index         w         x         y         z\n",
       "states                                                       \n",
       "ab            0     a  0.564134  0.008535  0.889342  0.723777\n",
       "cd            1     b  0.582890  0.909334  0.067464  0.289100\n",
       "ef            2     c  0.136845  0.756294  0.534836  0.642070\n",
       "gh            3     d  0.036292  0.959826  0.557958  0.597822\n",
       "ij            4     e  0.349582  0.803425  0.446590  0.452684"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.set_index('states', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([False, False, False, False,  True,  True,  True,  True,  True])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np1 = np.arange(1,10)\n",
    "np2 = np1>4\n",
    "np2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np1[np2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>level_0</th>\n",
       "      <th>index</th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>states</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>ab</th>\n",
       "      <td>0</td>\n",
       "      <td>a</td>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cd</th>\n",
       "      <td>1</td>\n",
       "      <td>b</td>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ef</th>\n",
       "      <td>2</td>\n",
       "      <td>c</td>\n",
       "      <td>0.136845</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.642070</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>gh</th>\n",
       "      <td>3</td>\n",
       "      <td>d</td>\n",
       "      <td>0.036292</td>\n",
       "      <td>0.959826</td>\n",
       "      <td>0.557958</td>\n",
       "      <td>0.597822</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ij</th>\n",
       "      <td>4</td>\n",
       "      <td>e</td>\n",
       "      <td>0.349582</td>\n",
       "      <td>0.803425</td>\n",
       "      <td>0.446590</td>\n",
       "      <td>0.452684</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        level_0 index         w         x         y         z\n",
       "states                                                       \n",
       "ab            0     a  0.564134  0.008535  0.889342  0.723777\n",
       "cd            1     b  0.582890  0.909334  0.067464  0.289100\n",
       "ef            2     c  0.136845  0.756294  0.534836  0.642070\n",
       "gh            3     d  0.036292  0.959826  0.557958  0.597822\n",
       "ij            4     e  0.349582  0.803425  0.446590  0.452684"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>level_0</th>\n",
       "      <th>index</th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>states</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>ab</th>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cd</th>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ef</th>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>gh</th>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ij</th>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        level_0  index      w      x      y      z\n",
       "states                                            \n",
       "ab        False   True   True  False   True   True\n",
       "cd         True   True   True   True  False  False\n",
       "ef         True   True  False   True   True   True\n",
       "gh         True   True  False   True   True   True\n",
       "ij         True   True  False   True  False  False"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df>.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop('index', axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "\"['level_0'] not found in axis\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-32-925733a081ea>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'level_0'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0minplace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mD:\\ANACONDA\\lib\\site-packages\\pandas\\core\\frame.py\u001b[0m in \u001b[0;36mdrop\u001b[1;34m(self, labels, axis, index, columns, level, inplace, errors)\u001b[0m\n\u001b[0;32m   3695\u001b[0m                                            \u001b[0mindex\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcolumns\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3696\u001b[0m                                            \u001b[0mlevel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlevel\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0minplace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0minplace\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 3697\u001b[1;33m                                            errors=errors)\n\u001b[0m\u001b[0;32m   3698\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3699\u001b[0m     @rewrite_axis_style_signature('mapper', [('copy', True),\n",
      "\u001b[1;32mD:\\ANACONDA\\lib\\site-packages\\pandas\\core\\generic.py\u001b[0m in \u001b[0;36mdrop\u001b[1;34m(self, labels, axis, index, columns, level, inplace, errors)\u001b[0m\n\u001b[0;32m   3109\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlabels\u001b[0m \u001b[1;32min\u001b[0m \u001b[0maxes\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3110\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mlabels\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 3111\u001b[1;33m                 \u001b[0mobj\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_drop_axis\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlevel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlevel\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   3112\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3113\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0minplace\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mD:\\ANACONDA\\lib\\site-packages\\pandas\\core\\generic.py\u001b[0m in \u001b[0;36m_drop_axis\u001b[1;34m(self, labels, axis, level, errors)\u001b[0m\n\u001b[0;32m   3141\u001b[0m                 \u001b[0mnew_axis\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlevel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlevel\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3142\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 3143\u001b[1;33m                 \u001b[0mnew_axis\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   3144\u001b[0m             \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreindex\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m**\u001b[0m\u001b[1;33m{\u001b[0m\u001b[0maxis_name\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnew_axis\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3145\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mD:\\ANACONDA\\lib\\site-packages\\pandas\\core\\indexes\\base.py\u001b[0m in \u001b[0;36mdrop\u001b[1;34m(self, labels, errors)\u001b[0m\n\u001b[0;32m   4402\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0merrors\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[1;34m'ignore'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4403\u001b[0m                 raise KeyError(\n\u001b[1;32m-> 4404\u001b[1;33m                     '{} not found in axis'.format(labels[mask]))\n\u001b[0m\u001b[0;32m   4405\u001b[0m             \u001b[0mindexer\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mindexer\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m~\u001b[0m\u001b[0mmask\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4406\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdelete\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mindexer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: \"['level_0'] not found in axis\""
     ]
    }
   ],
   "source": [
    "df.drop('level_0', axis=1, inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>states</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>ab</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cd</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ef</th>\n",
       "      <td>0.136845</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.642070</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>gh</th>\n",
       "      <td>0.036292</td>\n",
       "      <td>0.959826</td>\n",
       "      <td>0.557958</td>\n",
       "      <td>0.597822</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ij</th>\n",
       "      <td>0.349582</td>\n",
       "      <td>0.803425</td>\n",
       "      <td>0.446590</td>\n",
       "      <td>0.452684</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               w         x         y         z\n",
       "states                                        \n",
       "ab      0.564134  0.008535  0.889342  0.723777\n",
       "cd      0.582890  0.909334  0.067464  0.289100\n",
       "ef      0.136845  0.756294  0.534836  0.642070\n",
       "gh      0.036292  0.959826  0.557958  0.597822\n",
       "ij      0.349582  0.803425  0.446590  0.452684"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>states</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>ab</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cd</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ef</th>\n",
       "      <td>NaN</td>\n",
       "      <td>0.756294</td>\n",
       "      <td>0.534836</td>\n",
       "      <td>0.642070</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>gh</th>\n",
       "      <td>NaN</td>\n",
       "      <td>0.959826</td>\n",
       "      <td>0.557958</td>\n",
       "      <td>0.597822</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ij</th>\n",
       "      <td>NaN</td>\n",
       "      <td>0.803425</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               w         x         y         z\n",
       "states                                        \n",
       "ab      0.564134       NaN  0.889342  0.723777\n",
       "cd      0.582890  0.909334       NaN       NaN\n",
       "ef           NaN  0.756294  0.534836  0.642070\n",
       "gh           NaN  0.959826  0.557958  0.597822\n",
       "ij           NaN  0.803425       NaN       NaN"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df>.5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>states</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>ab</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cd</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ef</th>\n",
       "      <td>NaN</td>\n",
       "      <td>0.756294</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>gh</th>\n",
       "      <td>NaN</td>\n",
       "      <td>0.959826</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ij</th>\n",
       "      <td>NaN</td>\n",
       "      <td>0.803425</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               w         x\n",
       "states                    \n",
       "ab      0.564134       NaN\n",
       "cd      0.582890  0.909334\n",
       "ef           NaN  0.756294\n",
       "gh           NaN  0.959826\n",
       "ij           NaN  0.803425"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df>.5][['w','x']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "      <th>z</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>states</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>ab</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "      <td>0.889342</td>\n",
       "      <td>0.723777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cd</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "      <td>0.067464</td>\n",
       "      <td>0.289100</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               w         x         y         z\n",
       "states                                        \n",
       "ab      0.564134  0.008535  0.889342  0.723777\n",
       "cd      0.582890  0.909334  0.067464  0.289100"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['w']>0.5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>w</th>\n",
       "      <th>x</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>states</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>ab</th>\n",
       "      <td>0.564134</td>\n",
       "      <td>0.008535</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cd</th>\n",
       "      <td>0.582890</td>\n",
       "      <td>0.909334</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               w         x\n",
       "states                    \n",
       "ab      0.564134  0.008535\n",
       "cd      0.582890  0.909334"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['w']>0.5] [['w','x']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A    B  C\n",
       "0  1.0  5.0  1\n",
       "1  2.0  NaN  2\n",
       "2  NaN  NaN  3"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1 = pd.DataFrame({'A':[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C':[1,2,3]})\n",
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A    B  C\n",
       "0  1.0  5.0  1"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A    B  C\n",
       "0  1.0  5.0  1\n",
       "1  2.0  NaN  2\n",
       "2  NaN  NaN  3"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   C\n",
       "0  1\n",
       "1  2\n",
       "2  3"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.dropna(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1.0\n",
       "1    2.0\n",
       "2    1.5\n",
       "Name: A, dtype: float64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1['A'].fillna(df1['A'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.5</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A    B  C\n",
       "0  1.0  5.0  1\n",
       "1  2.0  5.0  2\n",
       "2  1.5  5.0  3"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.fillna(df1.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = { 'Company': ['GOOG','GOOG','MSFT','MSFT','FB','FB'], \n",
    "        'Person':['SAM','AKASH','ROHIT','VIRAT','MS','SACHIN'], \n",
    "        'Sales':[200,230,340,120,340,230]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Company</th>\n",
       "      <th>Person</th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>GOOG</td>\n",
       "      <td>SAM</td>\n",
       "      <td>200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>GOOG</td>\n",
       "      <td>AKASH</td>\n",
       "      <td>230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>ROHIT</td>\n",
       "      <td>340</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>VIRAT</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>FB</td>\n",
       "      <td>MS</td>\n",
       "      <td>340</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>FB</td>\n",
       "      <td>SACHIN</td>\n",
       "      <td>230</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Company  Person  Sales\n",
       "0    GOOG     SAM    200\n",
       "1    GOOG   AKASH    230\n",
       "2    MSFT   ROHIT    340\n",
       "3    MSFT   VIRAT    120\n",
       "4      FB      MS    340\n",
       "5      FB  SACHIN    230"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(data)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Company</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>FB</th>\n",
       "      <td>570</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>GOOG</th>\n",
       "      <td>430</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>MSFT</th>\n",
       "      <td>460</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Sales\n",
       "Company       \n",
       "FB         570\n",
       "GOOG       430\n",
       "MSFT       460"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Company').sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sales</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Company</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>FB</th>\n",
       "      <td>285</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>GOOG</th>\n",
       "      <td>215</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>MSFT</th>\n",
       "      <td>230</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Sales\n",
       "Company       \n",
       "FB         285\n",
       "GOOG       215\n",
       "MSFT       230"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Company').mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['GOOG', 'MSFT', 'FB'], dtype=object)"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Company'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Company'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "FB      2\n",
       "GOOG    2\n",
       "MSFT    2\n",
       "Name: Company, dtype: int64"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Company'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "def accNo(x):\n",
    "    return x*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Company</th>\n",
       "      <th>Person</th>\n",
       "      <th>Sales</th>\n",
       "      <th>DoubleSales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>GOOG</td>\n",
       "      <td>SAM</td>\n",
       "      <td>200</td>\n",
       "      <td>400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>GOOG</td>\n",
       "      <td>AKASH</td>\n",
       "      <td>230</td>\n",
       "      <td>460</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>ROHIT</td>\n",
       "      <td>340</td>\n",
       "      <td>680</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>MSFT</td>\n",
       "      <td>VIRAT</td>\n",
       "      <td>120</td>\n",
       "      <td>240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>FB</td>\n",
       "      <td>MS</td>\n",
       "      <td>340</td>\n",
       "      <td>680</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>FB</td>\n",
       "      <td>SACHIN</td>\n",
       "      <td>230</td>\n",
       "      <td>460</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Company  Person  Sales  DoubleSales\n",
       "0    GOOG     SAM    200          400\n",
       "1    GOOG   AKASH    230          460\n",
       "2    MSFT   ROHIT    340          680\n",
       "3    MSFT   VIRAT    120          240\n",
       "4      FB      MS    340          680\n",
       "5      FB  SACHIN    230          460"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['DoubleSales'] = df['Sales'].apply(accNo)\n",
    "df"
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
