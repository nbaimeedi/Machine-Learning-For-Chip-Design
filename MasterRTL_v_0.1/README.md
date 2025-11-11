# MasterRTL: A Pre-Synthesis PPA Estimation Framework for Any RTL Design

Wenji Fang, Yao Lu, Shang Liu, Qijun Zhang, Ceyu Xu, Lisa Wu Wills, Hongce Zhang, Zhiyao Xie. In Proceedings of IEEE/ACM International Conference on Computer Aided Design (ICCAD), 2023. [[paper]](https://ieeexplore.ieee.org/abstract/document/10323951)


## Collected Benchmarks
All the RTL designs used in our work are collected from open-source projects (from Openroad-flow-scripts).
https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts.git

Training DataSet:

Riscv, Aes, Black Parrot, Spi, Uart and TinyRocket.

Test Dataset:

Gcd, Microwatt.



## Code Structure

### 1. Process RTL files (foler: "ys_script")

```
   $ cd ys_script
   $ yosys run_{design}_sog.ys
   $ python3 clean_vlg.py
   
   ## Input: example/verilog/{design}/*.v (original Verilog files)
   ## Output: example/verilog/{design}/{design}_sog.v (SOG Verilog)
```

* Convert the original RTL files into standard Verilog format
  * Exmploy [Yosys](https://github.com/YosysHQ/yosys) for flattening (i.e., word-level AST) or bit-blasting (i.e., bit-level SOG).
  * Clean the generated Verilog file ("clean_vlg.py").

### 2. Verilog to Graph (folder: "vlg2ir")

```
   $ cd vlg2ir
   $ python3 auto_run.py
   
   ## Input: example/verilog/{design}/{design}_sog.v
   ## Output: example/sog/*.pkl
```

* Parse the Verilog code and convert it to graph representation
  * Build upon the open-source Verilog parser [Pyverilog](https://github.com/PyHDI/Pyverilog), converting the Verilog code into the abstract syntax tree (AST).
  * Construct graph representation by traversing the AST from the Verilog parser (Details in "DG.py", "logicGraph.py", and "AST_analyzer.py").
  * Analyze the graph for feature extraction ("graph_stat.py").

### 3. Circuit Preprocessing (folder: "preproc")

```
   ## Timing
   $ cd preproc/timing
   $ python3 delay_propagation.py
   
   Note - No circuit preprocessing for Power and Area 

* Preprocess the circuit graph data, including:
  * Process the graph into a directed acyclic graph (DAG) by removing the loop of the registers ("timing/delay_propagation.py").
  * Conduct delay propagation for timing estimation ("timing/delay_propagate.py").

```

### 4. Feature Extraction (folder: "feature_extract")

```
   ## Timing
   $ cd feature_extract/timing
   $ python3 feature_extra_graph_STA.py
	  ## Please note that this feature extraction step needs the trained path-level model ('rfr' in the code) to infer the path delay. You may train the path model first referring to the method in the paper. 
   
   ## Area:
   $ cd feature_extract/area
   $ python3 feature_extra_graph_stat.py

   ## Power
   Currently, we use only features related to area prediction.
```

* Perform feature extractions for timing, power, and area, the example of extracted features are saved in "./example/feature"
  * Timing: analytical node delay feature, propagated path delay feature, graph-level feature, etc.
  * Area: analytical area feature, graph-level feature, etc.

### 5. ML model Training (folder: "ML_model/train")

```
   ## Change the ppa_tpe in "train.py" (Area/TNS/WNS/Power)
   $ python3 train.py
```
* Trained model is saved in "ML_model/saved_model"

### 6. ML model inference (folder: "ML_model/infer")

```
   ## Change the ppa_tpe in "infer.py" (Area/TNS/WNS/Power)
   $ python3 infer.py
```

### Note

Label data is generated using Synopsys Design Compiler in the original paper. We used open-sourced tools like Yosys, ABC and OpenSTA for synthesis, area, power and timing extraction. The process can be found in /example/label/README.md

## Citation

```
@inproceedings{fang2023masterrtl,
  title={MasterRTL: A Pre-Synthesis PPA Estimation Framework for Any RTL Design},
  author={Fang, Wenji and Lu, Yao and Liu, Shang and Zhang, Qijun and Xu, Ceyu and Wills, Lisa Wu and Zhang, Hongce and Xie, Zhiyao},
  booktitle={Proceedings of 2023 IEEE/ACM International Conference on Computer-Aided Design (ICCAD)},
  pages={1--9},
  year={2023},
  organization={IEEE}
}
```

