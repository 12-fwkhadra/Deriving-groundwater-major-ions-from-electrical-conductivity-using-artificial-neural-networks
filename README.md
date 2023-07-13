# Deriving groundwater major ions from electrical conductivity using artificial neural networks: GUI
This is the GUI interface for the algorithm that derives groundwater major ions from EC-20 value. The aim of building this GUI is to assis the flexibilty and reliability of the built algorithm so that anyone can run and test it more easily.
This GUI interface is built using MATLAB R2020a. Embedded, the GUI script runs MATLAB and Python scripts that of the designed ANN and Regression models.

## Overview

Inspired by the ease of acquiring Electrical Conductivity proxy, an AI-based algorithm is developed. It is capable of extracting a relationship between EC (as a predictor) and 7 major water constituents as predicted variables (Cl, Na, Mg, K, SO4, Ca and HCO3).
The algorithm is made up of two submodels: submodel 1 responsible for predicitng the major ions for salinized samples (EC>900 uS/cm) whereas the submodel 2 is responsible for predicting the major ions for fresh samples (EC<900 uS/cm>).

![proposed algorithm](https://github.com/12-fwkhadra/Deriving-groundwater-major-ions-from-electrical-conductivity-using-artificial-neural-networks/blob/15433380db90a0567aef043ed43ec1238cd87f00/proposed%20algorithm.jpg)

For further explanation for the algorithm and its consisting models check the following pdf: [GitHub Pages](https://github.com/12-fwkhadra/Deriving-groundwater-major-ions-from-electrical-conductivity-using-artificial-neural-networks/blob/ab297f776c751ba54d30cc18bb85d08feac67df9/Algorithm%20Methodology.pdf)

## Getting Started

Before running the gui, ensure the following requirements:

- Technical Requirements:
  1. install MATLAB R2020 version or higher.
  2. install Python and set its environment.
  3. install the following Python packages: pandas, numpy, pickle, sys, sklearn.
- Hydrochemical-input Requirements:  
   acquire EC_20 values. In case the EC values obtained are EC_25 or EC_18, apply the following conversions before proceeding:  
   EC_20= EC_25\*0.885  
   EC_20= EC_18\*1.046

After achieving the above requirements:

- download the src folder. This folder includes the following files:
  1. mainInterface.mlapp: MATLAB App Designer file. It's the interface's code.
  2. mainScript.mlx: MATLAB live-function script file. It has the function mainScript() that runs the whole algorithm. It is linked to the previous mlapp file to read the user's input.
  3. salinized_Na_Mg_K_ANN, salinized_SO4_ANN: MATLAB workspace including the ANNs as variables for further usages. These ANNs belong to submodel 1 for salinized samples.
  4. fresh_Na_SO4_ANN, fresh_K_ANN: MATLAB workspace including the ANNs as variables for further usages. These ANNs belong to submodel 2 for fresh samples.
  5. salinized_Cl_regression, fresh_Cl_SVR: Python files perdicting Chloride via regression-based and SVR formulas respectively.
  6. salinized_Ca_HCO3_analytical_solution, fresh_Ca_Mg_HCO3_analytical_solution: Python files applying the analytical solutions for both submodels elements.

* open the folder in MATLAB. Make sure MATLAB's current folder and directory is that of downloaded src folder.
* open and run "mainInterface.mlapp". 1. select the csv file that has the EC_20 values. Selecting different file type will raise an error. Selecting a file that contains other than EC_20 values will raise an error. 2. select the folder in which the results will be saved in. In this selected folder 2 csv files will be created: one representing the results of the salinized samples, second representing the results of the fresh samples.
  Once finishing the selections required, the mainScript will automatically start running.
* upon finishing, the interface will pop up a message. Open the folder you selected to find the results.

## Contact Us

Email us at f.khadra2003@gmail.com
