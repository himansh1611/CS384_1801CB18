{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import pandas as pd \n",
    "import os,time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = time.time()\n",
    "\n",
    "def spi(credits, grades):\n",
    "    gr= {\"AA\":10, \"AB\":9, \"BB\":8, \"BC\":7, \"CC\":6, \"CD\":5, \"DD\":4, \"F\":0, \"I\":0}\n",
    "    w_sum = 0\n",
    "    for x,y in zip(credits, grades):\n",
    "        w_sum += (x*gr[y])\n",
    "    return round((w_sum/sum(credits)),2)\n",
    "\n",
    "def cpi(credits,spi_li):\n",
    "    weighted_sum = 0\n",
    "    for x,y in zip(credits,spi_li):\n",
    "        weighted_sum += (x*y)\n",
    "    return round((weighted_sum/sum(credits)),2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "header1 = [\"sub_code\", \"total_credits\", \"sub_type\", \"credit_obtained\", \"sem\", \"roll\"]\n",
    "header2= [\"Subject\", \"Credits\", \"Type\", \"Grade\", \"Sem\"]\n",
    "columns = [\"sub_code\", \"total_credits\", \"sub_type\", \"credit_obtained\", \"sem\"]\n",
    "df = pd.read_csv(\"acad_res_stud_grades.csv\", usecols=header1)\n",
    "misc_df = pd.read_csv(\"acad_res_stud_grades.csv\")\n",
    "roll_nums = list(df[\"roll\"].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "if os.path.exists(\"./grades\"):\n",
    "    pass\n",
    "else:\n",
    "    os.makedirs(\"./grades\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13.041187047958374\n"
     ]
    }
   ],
   "source": [
    "basepath = \"./grades\"\n",
    "\n",
    "gra = {\"AA\":10, \"AB\":9, \"BB\":8, \"BC\":7, \"CC\":6, \"CD\":5, \"DD\":4, \"F\":0, \"I\":0}\n",
    "\n",
    "for roll_num in roll_nums:\n",
    "    \n",
    "    temp = df[df[\"roll\"] == roll_num]\n",
    "    temp.drop(\"roll\", axis=1)\n",
    "    if(set(list(temp[\"credit_obtained\"].unique())).issubset(list(gra.keys())) and list(sorted(temp[\"sem\"].unique())) == list(range(1,1+max(list(temp[\"sem\"].unique()))))):\n",
    "        \n",
    "        #individual file\n",
    "        filename = roll_num + \"_individual.csv\"\n",
    "        with open(os.path.join(basepath,filename), \"a+\") as file:\n",
    "            start = \"Roll: {}\".format(roll_num)\n",
    "            info = \"Semester Wise Details\"\n",
    "            start = [start,\"\", \"\", \"\", \"\"]\n",
    "            info = [info,\"\", \"\", \"\", \"\"]\n",
    "            start = pd.DataFrame(start).transpose()\n",
    "            info = pd.DataFrame(info).transpose()\n",
    "            start.to_csv(file, header=False, index=False)\n",
    "            info.to_csv(file, header=False, index=False)\n",
    "            temp.to_csv(file, index=False, columns=cols, header=headera)\n",
    "        \n",
    "        #overall file\n",
    "        filename = roll_num + \"_overall.csv\"\n",
    "        with open(os.path.join(basepath,filename), \"a+\") as file:\n",
    "            li = list(temp[\"sem\"].unique())\n",
    "            sem_li = list()\n",
    "            sem_credits_li = list()\n",
    "            sem_credits_cleared_li = list()\n",
    "            sem_spi_li = list()\n",
    "            total_credits_li = list()\n",
    "            sem_cpi_li = list()\n",
    "            for semester in li:\n",
    "                sem_res = temp[temp[\"sem\"] == semester]\n",
    "                sem_li.append(semester)\n",
    "                sem_credits_li.append(sem_res[\"total_credits\"].sum())\n",
    "                sem_credits_cleared_li.append(sem_credits_li)\n",
    "                sem_spi_li.append(spi(list(sem_res[\"total_credits\"]), list(sem_res[\"credit_obtained\"])))\n",
    "                total_credits_li.append(sum(sem_credits_li))\n",
    "                if (len(sem_cpi_li) == 0):\n",
    "                    sem_cpi_li.append(sem_spi_li[0])\n",
    "                else:\n",
    "                    sem_cpi_li.append(cpi(sem_credits_li, sem_spi_li))\n",
    "\n",
    "            dictionary = {\"Semester\": sem_li, \"Semester Credits\": sem_credits_li, \"Semester Credits Cleared\": sem_credits_li, \"SPI\": sem_spi_li, \"Total Credits\": total_credits_li, \"Total Credits Cleared\": total_credits_li, \"CPI\": sem_cpi_li}\n",
    "            results = pd.DataFrame.from_dict(dictionary)\n",
    "            start = \"Roll: {}\".format(roll_num)\n",
    "            start = [start,\"\", \"\", \"\", \"\", \"\", \"\"]\n",
    "            start = pd.DataFrame(start).transpose()\n",
    "            start.to_csv(file, header=False, index=False)\n",
    "            results.to_csv(file, index=False)\n",
    "    else:\n",
    "        #misc file\n",
    "        misc_data = misc_df[misc_df[\"roll\"] == roll_num]\n",
    "        if(os.path.exists(os.path.join(basepath,\"misc.csv\"))):\n",
    "            misc_data.to_csv(os.path.join(basepath,\"misc.csv\"), mode=\"a+\", index=False, header=False)\n",
    "        else:\n",
    "            misc_data.to_csv(os.path.join(basepath,\"misc.csv\"), mode=\"a+\", index=False)\n",
    "\n",
    "\n",
    "print(time.time() - start_time)"
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
