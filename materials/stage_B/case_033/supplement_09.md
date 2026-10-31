# Saved primary-source web extracts

Partial extracts; source URLs and original line gaps are retained where recorded.

Event-Based Eye Tracking. AIS 2024 Challenge Survey (https://arxiv.org/html/2404.11770v1)
L0: ##### Report GitHub Issue
L1: 
L2: [Button: ×]
L3: 
L4: Title: [Input: Enter title]
L5: 
L6: Content selection saved. Describe the issue below:
L7: 
L8: Description:
L9: 
L10: [Button: Submit without GitHub] [Button: Submit in GitHub]
L11: 
L12: cite0†Back to arXiv L13: 
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Event-based Eye Tracking Challenge L18:     1. cite8†2.1 Introduction of the 3ET+ dataset L19:     2. cite9†2.2 Task description L20:     3. cite10†2.3 Provided pipeline for loading data and training L21:     4. cite11†2.4 Challenge phases L22:   4. cite12†3 Challenge Results L23:     1. cite13†3.1 Architectures and main ideas L24:     2. cite14†3.2 Participants L25:     3. cite15†3.3 Inclusiveness and fairness L26:     4. cite16†3.4 Conclusions L27:       1. cite17†Related Challenges L28:   5. cite18†4 Challenge Methods and Teams L29:     1. cite19†4.1 Team: USTCEventGroup L30:       1. cite20†Description. L31:       2. cite21†Implementation Details. L32:       3. cite22†Results. L33:     2. cite23†4.2 Team: FreeEvs L34:       1. cite24†Description. L35:       2. cite25†Implementation Details. L36:       3. cite26†Results. L37:     3. cite27†4.3 Team: bigBrains L38:       1. cite28†Description. L39:       2. cite29†Implementation Details. L40:       3. cite30†Results. L41:     4. cite31†4.4 Team: Go Sparse L42:       1. cite32†Description. L43:       2. cite33†Implementation Details. L44:       3. cite34†Results. L45:     5. cite35†4.5 Team: MeMo L46:       1. cite36†Description. L47:       2. cite37†Implementation Details. L48:       3. cite38†Results. L49:     6. cite39†4.6 Team: ERVT L50:       1. cite40†Description. L51:       2. cite41†Implementation Details. L52:     7. cite42†4.7 Team: EFFICIENT L53:       1. cite43†Description. L54:       2. cite44†Implementation Details. L55:       3. cite45†Results. L56:     8. cite46†4.8 Team: GTechVision L57:       1. cite47†Description. L58:       2. cite48†Implementation Details. L59:       3. cite49†Results. L60:   6. cite50†References L61: cite51†License: CC BY-NC-ND 4.0†info.arxiv.org L62: 
L63: arXiv:2404.11770v1 [cs.CV] 17 Apr 2024
L64: # Event-Based Eye Tracking. AIS 2024 Challenge Survey
L65: Zuowen Wang^{*}    Chang Gao^{*}    Zongwei Wu^{*}    Marcos V.
L66: Conde^{*}    Radu Timofte^{*}    Shih-Chii Liu^{*}    Qinyu Chen^{* ⋄}    Zheng-jun Zha    Wei Zhai    Han Han    Bohao Liao    Yuliang Wu    Zengyu Wan    Zhong Wang    Yang Cao    Ganchao Tan    Jinze Chen    Yan Ru Pei    Sasskia Brüers    Sébastien Crouzet    Douglas McLelland    Oliver Coenen    Baoheng Zhang    Yizhao Gao    Jingyuan Li    Hayden Kwok-Hay So    Philippe Bich    Chiara Boretti    Luciano Prono    Mircea Lică    David Dinucu-Jianu    Cătălin Grîu    Xiaopeng Lin    Hongwei Ren    Bojun Cheng    Xinan Zhang    Valentin Vial    Anthony Yezzi    James Tsai
L67: ###### Abstract
L68: This survey reviews the AIS 2024 Event-Based Eye Tracking (EET) Challenge. The task of the challenge focuses on processing eye movement recorded with event cameras and predicting the pupil center of the eye. The challenge emphasizes efficient eye tracking with event cameras to achieve good task accuracy and efficiency trade-off. During the challenge period, 38 participants registered for the Kaggle competition, and 8 teams submitted a challenge factsheet.
L69: The novel and diverse methods from the submitted factsheets are reviewed and analyzed in this survey to advance future event-based eye tracking research.
L70: ^{†}^{†}footnotetext: ^{∗} Zuowen Wang, Chang Gao, Zongwei Wu, Marcos V. Conde, Radu Timofte, Shih-Chii Liu and Qinyu Chen are the challenge organizers, while the other authors participated in the challenge.
L71: ^{⋄} Qinyu Chen (q.chen@liacs.leidenuniv.nl) is the corresponding author.
L72: Challenge website: cite52†https://eetchallenge.github.io/EET.github.io/†eetchallenge.github.io . Demonstration code repository: cite53†https://github.com/EETChallenge/challenge_demo_code†github.com . Challenge Kaggle website: cite54†https://www.kaggle.com/competitions/event-based-eye-tracking-ais2024†www.kaggle.com . AIS 2024 host website: cite55†https://ai4streaming-workshop.github.io/†ai4streaming-workshop.github.io .
L73: ## 1 Introduction
L74: The fast development of augmented reality (AR) and virtual reality (VR) technologies in industry, has significantly magnified the importance of precise and efficient eye-tracking systems [cite56†15 , cite57†16 ].
L75: Furthermore, eye-tracking and related tasks, including gaze detection, pupil shape detection, etc, have tremendous potential in the field of wearable healthcare technology, offering novel approaches for diagnosing and monitoring conditions such as Parkinson’s and Alzheimer’s diseases through the analysis of eye movement patterns [cite58†31 , cite59†14 , cite60†25 ].
L76: Energy consumption and computation resources are often constrained when implementing software and algorithms on mobile platforms. Moreover, the high sensory sampling rate for eye-tracking tasks also poses challenges from the sensor side. For mobile applications, ideally, the eye tracking system should be lightweight enough to fit in the headset while providing a high sampling rate.
L77: Event cameras, or Dynamic Vision Sensors (DVS) [cite61†28 , cite62†27 , cite63†17 , cite64†43 ], provide a unique type of sensory modality for potential eye-tracking applications on mobile devices. Unlike traditional cameras that capture the entire scene synchronously at a fixed frequency, event cameras asynchronously record log intensity changes in brightness that exceed a threshold.
L78: This different sensing mechanism results in an inherently sparse spatiotemporal stream of output events, which, if appropriately exploited with the underlying algorithm [cite65†40 , cite66†29 , cite67†36 , cite68†37 , cite69†44 , cite70†45 , cite71†42 ] and computing platform [cite72†4 , cite73†7 , cite74†6 , cite75†18 ], can significantly reduce the computation and energy demands of the hardware platform. The high temporal resolution of the DVS events can also be useful for the eye-tracking task.
L79: This challenge aims to invite participants to explore algorithms for the event-based eye tracking task on a recorded eye tracking DVS dataset. By focusing on efficient algorithms capable of extracting meaningful information from sparse event streams, this challenge aims to pursue advancements in eye tracking technologies that are both energy-efficient and suitable for real-time applications in AR/VR technologies and wearable healthcare devices.
L80: ## 2 Event-based Eye Tracking Challenge
L81: ### 2.1 Introduction of the 3ET+ dataset
L82: The 3ET+ dataset [cite76†41 ] is an event-based eye-tracking dataset that contains real events recorded with a DVXplorer Mini [cite77†3 ] event camera. There are 13 subjects in total, each having 2-6 recording sessions. The subjects are required to perform 5 classes of activities: random, saccades, read text, smooth pursuit and blinks. The total data volume is 9.2 GB.
L83: The ground truth is labeled at 100Hz and consists of two parts for each label: (1) a binary value indicating whether there was an eye blink or not; (2) human-labeled pupil center coordinates.
L84: ### 2.2 Task description
L85: 
L86:   * •
L87: 
L88: Input: Raw event stream $(x_{i},y_{i},t_{i},p_{i})$ of recorded eye movement.
L89: 
L90:   * •
L91: 
L92: Task: Predict the pupil center spatial coordinate $(x,y)$ at required timestamps (same frequency as the ground truth) in the input space.
L93: 
L94:   * •
L95: Metric: The metric used in this work was also used in the work [cite78†8 ]. The primary metric used on the Kaggle leaderboard was the p-accuracy. If the Euclidean distance between the spatial coordinates of the predicted label and the ground truth label is within p pixels, then we classify it as a successful prediction. On the Kaggle leaderboard, we set the tolerance as 10 pixels. We also provide p = {5, 3, 1} in the demonstration code pipeline for evaluating the model under a stricter tolerance value.
L96: After the Kaggle competition ended, we also provided a script for the participants to evaluate their results against the test set ground truth with mean Euclidean distance ($\ell_{2}$) and mean Manhattan distance ($\ell_{1}$).
L97: ### 2.3 Provided pipeline for loading data and training
L98: A handy data loading and training pipeline was provided to the challenge participants. The data loading module (data loader) is compatible with the Tonic library [cite79†26 ]. The module enables the participants to explore various event feature representations. The data loader can also cache the generated feature representation on the main memory or on disk during the first training epoch. For the following epochs, it can automatically load these pre-made data thus speeding up the training process.
L99: For the training pipeline, the challenge participants can easily place in their deep learning architecture and configure the hyperparameters. A machine learning monitoring library, namely the MLFlow library [cite80†2 ], was provided in the challenge pipeline code for the participants to monitor various metrics and to record the hyperparameters, as well as the checkpoints.
L100: ### 2.4 Challenge phases
L101: 
L102: The challenge is mainly divided into three phases: (1) before 5. Feb. 2024, preparation of challenge dataset, code pipeline, website, and Kaggle setup. (2) 5. Feb. 2024, the Kaggle competition begins, and teams are allowed to register and download the dataset. (3) 16. March. 2024, the submission system closed and the private score was released. The top-performing teams are then invited to submit their factsheets and every team was encouraged to submit a workshop challenge paper.
L103: ## 3 Challenge Results
L104: The evaluation results of the final submissions from participating teams are listed in Tab. cite81†1 . The primary evaluation metric used in the Kaggle competition [cite82†1 ] ranking is the p10 accuracy described in Sec. cite9†2.2 . The challenge ranking is based on the private test split (p10 private (primary)), and only teams who submit their factsheets will participate in the final ranking.
L105: We also evaluate p10, p5, p3 and p1 accuracy and mean Euclidean distance ($\ell_{2}$) and mean Manhattan distance ($\ell_{1}$) based on the final submissions of the teams on the entire test split. Notably, all teams achieved very high p10 accuracy on the task.
L106: Team  | Rank  | p10 private (primary)  | p10  | p5  | p3  | p1  | $\ell_{2}$  | $\ell_{1}$
L107: --- | --- | --- | --- | --- | --- | --- | --- | ---
L108: USTCEventGroup  | 1  | 99.58  | 99.42  | 97.05  | 90.73  | 33.75  | 1.67  | 2.11
L109: FreeEvs  | 2  | 99.27  | 99.26  | 96.31  | 83.83  | 23.91  | 2.03  | 2.56
L110: bigBrains  | 3  | 99.16  | 99.00  | 97.79  | 94.58  | 45.50  | 1.44  | 1.82
L111: Go Sparse  | 4  | 98.74  | 99.00  | 77.20  | 47.97  | 7.32  | 3.51  | 4.63
L112: MeMo  | 4  | 98.74  | 99.05  | 89.36  | 50.87  | 6.53  | 3.2  | 4.04
L113: ERVT  | 6  | 97.60  | 98.21  | 94.94  | 87.26  | 28.80  | 1.98  | 2.48
L114: EFFICIENT  | 6  | 97.60  | 97.95  | 80.67  | 49.08  | 7.79  | 3.51  | 4.43
L115: GTechVision  | 8  | 91.86  | 92.26  | 61.08  | 31.70  | 4.16  | 4.94  | 6.18
L116: Table 1: Final results from the top performing teams on Kaggle leaderboard. p10 private (primary) was evaluated on the private test set and all the rest metrics were evaluated on the entire test set.
L117: ### 3.1 Architectures and main ideas
L118: 
L119: The participating teams proposed many different methods. This shows that there is no yet conclusive best approach for processing event data specifically for the eye tracking task. We summarize and discuss the major findings from the submitted methods.
L120: Stateful models and spatial-temporal processing. Most teams selected architectures with state as their backbones, including gated recurrent units (GRU) [cite83†11 ], recurrent visual transformer [cite84†19 ] with convolutional long short-term memory [cite85†38 ] (ConvLSTM), bidirectional LSTM (biLSTM) and the newly emerged state-space model variant Mamba [cite86†20 ].
L121: Stateful models are chosen due to the need to integrate event history and preserve the eye tracking states when very few events are generated, i.e., static or very slow eye movement. The other class of choices for handling the property of event data is using certain spatiotemporal techniques, including having a memory channel in the event representation preprocessing or temporal processing blocks in the convolution architecture.
L122: Computation and parameter efficiency. This challenge emphasizes efficiency and task performance as equally important. Most teams have considered computation and parameter efficiency in their method designs. One team (Sec. cite27†4.3 ) designed a temporal causal layer that could be implemented with a buffer for online inference. The team Go Sparse (Sec. cite31†4.4 ) implemented their method, which implements sparse convolution [cite87†9 , cite88†10 ], on an FPGA board, achieving sub-millisecond inference latency.
L123: Most teams provided inference latency, model parameters and FLOPs needed for inference as part of their result.
L124: Event representations and spatial feature extraction. Converting raw event data into representations that can be processed by synchronous deep learning architectures is an important first step for any event-based tasks. In this challenge, the participants selected different ways to implement this step. Two teams aggregate sequential event frames using binary map representation to compress the input data sent to the model.
L125: The team MeMo (Sec. cite35†4.5 ) proposes using a memory channel to preserve historical event information better. Different from other teams, the team EFFICIENT (Sec. cite42†4.7 ) uses point-based network [cite89†34 , cite90†32 , cite91†33 ] to process the raw event data as spatiotemporal event cloud. They also propose to use techniques that subsample the event cloud to reduce the computation.
L126: Other novel components. Apart from backbone design, hardware consideration, and event representation, the teams also propose other innovations during the challenge. This includes implementation of an affine transformation on event data (Sec. cite27†4.3 ), sequence splitting and reordering data augmentation (Sec. cite35†4.5 ) and different regularization techniques (Sec. cite23†4.2 , Sec. cite27†4.3 ).
L127: ### 3.2 Participants
L128: 
L129: There were, in total, 38 user accounts registered and participated in the Kaggle competition [cite82†1 ] of the challenge, and 8 teams with private p10 accuracy over 90% submitted factsheets describing their methods. The institutions of the team members for the submitted factsheets are located in regions including Asia, Europe and North America.
L130: ### 3.3 Inclusiveness and fairness
L131: Several measures were implemented to maintain the inclusiveness and fairness of the challenge. First and most importantly, the dataset and task are preprocessed and configured to keep the hardware requirement for training models possibly low. Second, an out-of-box usable training and testing pipeline was provided so that even teams with little event-based data experience could easily start experimenting. Thirdly, code submission is required for the factsheets submission to ensure reproducible results.
L132: ### 3.4 Conclusions
L133: 
L134: We summarize the insights obtained during the challenge and from the challenge results as follows:
L135: 
L136:   1. 1.
L137: 
L138: The field of event-based visual processing, more specifically event-based eye tracking, is a newly emerged field. Unlike many other computer vision fields where transformer-based methods dominate, there is a large variety in event data processing. There is plenty of room for achieving a better trade-off for task performance and model efficiency.
L139: 
L140:   2. 2.
L141: Hardware consideration is always essential for researchers developing algorithms for event cameras due to its compatibility with mobile platforms. Algorithm-hardware co-design is an important research direction in this field.
L142: 
L143:   3. 3.
L144: 
L145: This challenge and existing works proved the feasibility of using an event camera for the eye-tracking task. Prototyping and more realistic settings are needed to step towards more mature event-based eye tracking systems.
L146: #### Related Challenges
L147: 
L148: This challenge is one of the AIS 2024 Workshop associated challenges on: Event-based Eye-Tracking [cite76†41 ], Video Quality Assessment of user-generated content [cite92†13 ], Real-time compressed image super-resolution [cite93†12 ], Mobile Video SR, and Depth Upscaling.
L149: ## Acknowledgements
L150: 
L151: Zongwei Wu, Marcos V. Conde, and Radu Timofte are with University of Würzburg, CAIDAS, Computer Vision Lab.
L152: 
L153: Zuowen Wang and Shih-Chii Liu are at the Institute of Neuroinformatics, University of Zurich and ETH Zurich (INI). Qinyu Chen was at INI at the start of the challenge and is currently at the Leiden Institute of Advanced Computer Science (LIACS), Leiden University.
L154: 
L155: Chang Gao is at Delft University of Technology.
L156: This project was partially (e.g., dataset collection) funded by the Swiss National Science Foundation and Innosuisse BRIDGE - Proof of Concept Project (40B1-0_213731).
L157: 
L158: The dataset collection was partially supported by the 2023 Telluride Neuromorphic Cognition Engineering Workshop.
L159: 
L160: This work was partially supported by the European Union’s Horizon 2020 research and innovation programme under grant agreement No 899287.
L161: This work was partially supported by the Humboldt Foundation. We thank the AIS 2024 sponsors: Meta Reality Labs, Meta, Netflix, Sony Interactive Entertainment (FTG), and the University of Würzburg (Computer Vision Lab).
L162: ## 4 Challenge Methods and Teams
L163: 
L164: In the following sections we describe the best challenge solutions. Note that the method descriptions were provided by each team as their contribution to this survey.
L165: 
L166: ### 4.1 Team: USTCEventGroup
L167: 
L168: Zheng-jun Zha, Wei Zhai, Han Han,
L169: Bohao Liao, Yuliang Wu
L170: 
L171: University of Science and Technology of China
L172: 
L173: Contact: zhazj@ustc.edu.cn
L174: #### Description.
L175: 
L176: The USTCEventGroup proposed the MambaPupil method as shown in cite94†Fig. 1 . This lightweight and time-efficient network comprises two main parts: the Spatial Feature Extractor and the Dual-Recurrent Module for position prediction. In the Spatial Feature Extractor there are a series of convolutional blocks, which are designed as follows:
L177: 
L178:  | $\displaystyle x_{t}=Pool(ReLU(BatchNorm(Conv(B_{e})))),$  |  | (1)
L179: Larger convolutional kernels (7 or 5) are employed, and extracted features are fed into the Dual Recurrent Module after an adaptative global pooling layer and a SpatialDropout layer. The Dual Recurrent Module consists of a bi-directional GRU module and an LTV-SSM module, recently known as a Mamba block.
L180: This bi-directional structure is beneficial to capturing contextual information compared to a uni-directional one, and the additional Linear-time-variant State-Space Model (LTV-SSM) module models the behavior patterns of eye movements selectively to cast more attention into the valid phase. The LTV-SSM module can be described by the formula:
L181:  | $\displaystyle\Delta,B,C$  | $\displaystyle=Linear(x),$  |  | (2)
L182:  | $\displaystyle\Delta A$  | $\displaystyle=exp(\Delta*A),$  |  | (3)
L183:  | $\displaystyle\Delta B$  | $\displaystyle=\Delta*B.$  |  | (4)
L184:  | $\displaystyle\Delta x$  | $\displaystyle=\Delta A*x+\Delta B*u,$  |  | (5)
L185:  | $\displaystyle y$  | $\displaystyle=Cx+Du,$  |  | (6)
L186: Furthermore, to reduce computational complexity and avoid uncorrelated events negatively affecting the model, The USTCEventGroup utilizes binary map representation of events and encodes the order of events in the sequence. The binary map representation, usually referred to as bina-rep, is aggregated from multiple sequential event frames. These frames are firstly binarized and stacked by bits forming a bina-rep.
L187: Additionally, several data enhancement methods are introduced, including Event-Cutout, which applies spatial random masking to the event image and extends it across the entire sequence in the data augmentation stage to enhance the generalization ability. As for the loss criterion, RMSE loss is applied:
L188:  | $\displaystyle Loss=\sqrt{\frac{1}{L}\sum_{i=1}^{L}(Pred_{i}-Label_{i})^{2}},$  |  | (7)
L189: #### Implementation Details.
L190: 
L191: All the experiments were implemented using PyTorch, and Cosine Annealing Warm Restart was utilized as a learning-rate scheduler, beginning at an initial rate of 0.002. The training and evaluation are performed entirely on the 3ET++ dataset, and the time cost for 1000 epochs with a batchsize of 32 is about 1.5 hours on a single RTX 2080Ti GPU.
L192: 
L193: cite95†Image: Refer to caption Figure 1: MambaPupil network by Team USTCEventGroup.
L194: #### Results.
L195: 
L196: We scored best on the leaderboard, performed far exceeded the baseline with a p10 accuracy above 0.995. Our visualization shows the elegant tracking process even in difficult scenario. Visualization results and code is available in cite96†https://github.com/hh-xiaohu/Event-based-Eye-Tracking-Challenge-Solution†github.com .
L197: 
L198: The results are obtained from the validation set:
L199:  | p_5  | p_10  | p_15  | p_error
L200: MambaPupil  | 0.9192  | 0.9846  | 0.9926  | 2.1799
L201: Table 2: Validation results of MambaPupil.
L202: ### 4.2 Team: FreeEvs
L203: 
L204: Zengyu Wan, Zhong Wang, Yang Cao,
L205: Ganchao Tan, Jinze Chen
L206: 
L207: University of Science and Technology of China
L208: 
L209: Contact: wanzengy@mail.ustc.edu.cn
L210: #### Description.
L211: The FreeEvs Team proposed the lightweight and efficient model, Consistent Eye Tracking Model (CETM), as shown in cite97†2 . The whole framework consists of the following components: 1. Event representation; 2. Representation enhancement; 3. Tracking predictor; 4. Motion consistency loss. Given the event stream, the CETM will first convert it into the binary map representation [cite98†5 ], which is compact and informative.
L212: The binary map first generates a spatially binarized event clip based on the event frames aggregated and accumulated over a period of time, after which it encodes each frame in the clip using a temporal binarization mask. And then, the spatio-temporally binarized encoded clip is accumulated at corresponding locations to form the final Bina-rep $B_{e}$.
L213: This approach brings two benefits: 1) it reduces storage and computational costs, improving the training and inference speed of the network.; 2) it reduces the impact of noise and redundant information on prediction results to some extent. Next, the Bina-rep will be enhanced for effective training. The adopted data enhancement techniques contain spatial shift, spatial flip, temporal shift, and temporal flip.
L214: The spatial operations improve the model localization ability with more spatial variation samples, and the temporal operations endow the model’s consistent tracking ability with more temporal variation samples. Next, the tracking predictor is utilized to localize the pupil efficiently. The predictor consists of the stacked convolution blocks, the global pooling layer, the gated recurrent unit (GRU), and the final full connection layer (FC) to predict the result.
L215: Among them, the team used 3 convolution blocks, each composed of the 2D convolution, batch normalization, ReLU activation function, and average pooling layer, to extract the corresponding pupil space information. And then, the spatial information will be transported into the GRU module in time order to extract the temporal contextual clues. The spatial-temporal clues are finally transformed into the prediction by the FC layer.
Event-based Eye Tracking - AIS2024 CVPR Workshop | Kaggle (https://www.kaggle.com/competitions/event-based-eye-tracking-ais2024/discussion/484138)
Event-based Eye Tracking - CVPR 2024 Challenge (https://eetchallenge.github.io/EET.github.io/)
L0: # Event-based Eye Tracking
L1: AI for Streaming CVPR 2024 Challenge
L2: 
L3: cite0†Zuowen Wang†scholar.google.fr ^{1}, cite1†Chang Gao†scholar.google.fr ^{2}, cite2†Zongwei Wu†scholar.google.fr ^{3}, cite3†Shih-Chii Liu†scholar.google.fr ^{1}, cite4†Qinyu Chen†scholar.google.fr ^{1,4},
L4: 
L5: ^{1}Sensors Group, Institute of Neuroinformatics, UZH/ETH Zurich, ^{2}EMI Lab,TU Delft, ^{3}Computer Vision Lab, University of Wurzburg, ^{4}LIACS, Leiden University
L6: Presentation at CVPR cite5†AI for Streaming Workshop†ai4streaming-workshop.github.io L7: cite6†Kaggle†www.kaggle.com cite7†Github†github.com cite8†Data†www.kaggle.com cite9†Challenge Report†arxiv.org L8: 
L9: cite10†Image: Event-based eye-tracking video game demo L10: 
L11: Let's play some video games with event-based eye-tracking!
L12: 
L13: This video was filmed at the 2023 Telluride Neuromorphic Cognition Engineering Workshop, CO, US, by Qinyu Chen and Chang Gao.
L14: ## About the Challenge
L15: Developing an event-based eye-tracking system presents significant opportunities in diverse fields, notably in consumer electronics and neuroscience. Human eyes exhibit rapid movements, occasionally surpassing speeds of 300°/s. This necessitates using cite11†event cameras†www.youtube.com capable of high-speed sampling and tracking.
L16: In consumer electronics, particularly in augmented and virtual reality (AR/VR) applications, the primary benefits of event-based systems extend beyond their high speed. Their highly sparse input data streams can be exploited to reduce power consumption. This is a pivotal advantage in creating lighter, more efficient wearable headsets that offer prolonged usage and enhanced user comfort.
L17: This is instrumental in augmenting the immersive experience in AR/VR and expanding the capabilities of portable technology. In neuroscience and cognitive studies, such technology is crucial for deciphering the complexities of eye movement. It facilitates a deeper comprehension of visual attention processes and aids in diagnosing and understanding neurological disorders.
L18: This challenge aims to develop an **event-based eye-tracking system for precise tracking of rapid eye movements** to produce lighter and more comfortable devices for a better user experience. Simultaneously, it promises to provide novel insights into neuroscience and cognitive research, deepening our understanding of these domains.
L19: The challenge will held with the cite5†1st edition of AI for Streaming†ai4streaming-workshop.github.io workshop, in conjunction with CVPR 2024.
L20: ## News
L21: 
L22: [16/03/2024] Challenge Ends! Thanks for your interest in our challenge!
L23: 
L24: [02/05/2024] Challenge Starts!
L25: 
L26: [01/29/2024] Release Website
L27: ## Contact
L28: 
L29: If you have technical questions on the challenge, please contact us at:
L30: - Zuowen Wang (zuowen [at] ini [dot] uzh [dot] ch)
L31: - Qinyu Chen (q.chen [at] liacs [dot] leidenuniv [dot] nl)
L32: Winners will be invited, after being reviewed, to present during the associated CVPR workshop.
L33: Other top-ranked teams may be invited to a tentative report for documenting the challenge.
L34: For more details, please contact cite5†workshop†ai4streaming-workshop.github.io organizers.
L35: ## Program Committee Members (TBU):
L36: Zuowen Wang, UZH/ETH Zurich
L37: Chang Gao, TU Delft
L38: Zongwei Wu, University of Wurzburg
L39: Shih-Chii Liu, UZH/ETH Zurich
L40: Qinyu Chen, UZH/ETH Zurich & Leiden University
L41: Zhuyun Zhou, University of Burgundy
L42: Remi Boutteau, University of Rouen Normandy
L43: Dominique Ginhac, University of Burgundy
L44: Fan Yang-Song, University of Burgundy
L45: Guillaume Caron, CNRS-AIST JRL, IRL 3218 & UPJV
L46: Menghan Hu, East China Normal University
L47: Guohao Lan, TU Delft
L48: Xucong Zhang, TU Delft
L49: Zhuo Zou, Fudan University
L50: Congyi Sun, Nanjing University
L51: Shilin Fu, Dalian University of Technology
L52: Zixiao Li, UZH/ETH Zurich
L53: Joachim Ott, UZH/ETH Zurich
L54: ## BibTeX
L55: 
L56:     `
L57:           @inproceedings{chen20233et,
L58:           title={3et: Efficient event-based eye tracking using a change-based convlstm network},
L59:           author={Chen, Qinyu and Wang, Zuowen and Liu, Shih-Chii and Gao, Chang},
L60:           booktitle={2023 IEEE Biomedical Circuits and Systems Conference (BioCAS)},
L61:           pages={1--5},
L62:           year={2023},
L63:           organization={IEEE}
L64:         }
L65: 
L66:           @inproceedings{wang2024ais_event,
L67:           title={{E}vent-{B}ased {E}ye {T}racking. {AIS} 2024 {C}hallenge {S}urvey},
L68:           author={Zuowen Wang and Chang Gao and Zongwei Wu and Marcos V. Conde and Radu Timofte and Shih-Chii Liu and Qinyu Chen and others},
L69:           booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops},
L70:           year={2024}
L71:         }
L72:         `
L73: This website template is borrowed from cite12†Nerfies†github.com .
