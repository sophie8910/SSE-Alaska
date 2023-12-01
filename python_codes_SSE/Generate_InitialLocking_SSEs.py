{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ed481f77-a7f6-4820-a57c-d23a4b80b600",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import all the python packages here\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6a5dfc23-a86e-4d5a-b9fe-d9041070943c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[-0.33, -0.54, -0.54, -0.45, 0.13, -0.23, -0.58, -0.58, -0.52, -0.56, -0.54, -0.43], array([15, 16, 17, 18, 14, 15, 16, 17, 18, 16, 17, 18]), array([4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6])]\n"
     ]
    }
   ],
   "source": [
    "# read the file that include longitude, latitude, phi, node X, node Z, sub-segment X, sub-segment Z\n",
    "# when we use the columns, index starts from 0\n",
    "NodePhifile = 'Diff1avg242_phi_srd_llpSSE12.gmt'\n",
    "#sse1p1philon = np.loadtxt(NodePhifile, usecols=0, dtype = 'float')\n",
    "#sse1p1philat = np.loadtxt(NodePhifile, usecols=1, dtype = 'float')\n",
    "sse1p1phiphi = np.loadtxt(NodePhifile, usecols=2, dtype = 'float')\n",
    "sse1p1phiNodeX = np.loadtxt(NodePhifile, usecols=3, dtype = 'int')\n",
    "sse1p1phiNodeZ = np.loadtxt(NodePhifile, usecols=4, dtype = 'int')\n",
    "\n",
    "# import text file that includes distinct values of node X, node Z processing based on file NodePhifile\n",
    "distinctfile = 'Diff1avg242_phi_srd_llpSSE12_nodeindices.gmt'\n",
    "disNodeX = np.loadtxt(distinctfile, usecols=3, dtype = 'int')\n",
    "disNodeZ = np.loadtxt(distinctfile, usecols=4, dtype = 'int')\n",
    "\n",
    "# t marks the index for each individual set of nodes\n",
    "\n",
    "avgphis = []\n",
    "for nx, nz in zip(disNodeX, disNodeZ):\n",
    "    # avgphi marks the average value of all the phis corressponding to the same disNodeX, disNodeZ\n",
    "    avgphi = 0\n",
    "    # n marks the number of phis calculated in total\n",
    "    n = 0\n",
    "    for i, j in zip(range(len(sse1p1phiNodeX)), range(len(sse1p1phiNodeZ))):\n",
    "        if sse1p1phiNodeX[i] == nx and sse1p1phiNodeZ[j] == nz:\n",
    "            #print(sse1p1phiphi[i])\n",
    "            avgphi += sse1p1phiphi[i]\n",
    "            n += 1\n",
    "    avgphis.append(round(avgphi/n, 2))\n",
    "\n",
    "newphienodes = [avgphis, disNodeX, disNodeZ]\n",
    "#print(avgphis, disNodeX, disNodeZ)\n",
    "print(newphienodes)\n",
    "    \n",
    "# Then we use the calculated avgphis for corresponding disNodeX, disNodeZ to write into a new text file\n",
    "\n",
    "newNodephifile = 'Diff1avg242_phi_srd_llpSSE12_newphis.gmt'\n",
    "np.savetxt(newNodephifile, newphienodes)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9f701d7-2887-4c5a-a8ba-946225c1a582",
   "metadata": {},
   "outputs": [],
   "source": [
    "# plot calculated GPS velocity after TDEFNODE forward modeling\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3584d590-b969-41f1-9882-bf39139bf681",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
