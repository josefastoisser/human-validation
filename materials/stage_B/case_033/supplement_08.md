# Saved primary-source web extracts

Partial extracts; source URLs and original line gaps are retained where recorded.

challenge_demo_code/dataset/custom_transforms.py at master · EETChallenge/challenge_demo_code · GitHub (https://github.com/EETChallenge/challenge_demo_code/blob/master/dataset/custom_transforms.py)
L609: 193
L610: 
L611: 194
L612: 
L613: 195
L614: 
L615: 196
L616: 
L617: 197
L618: 
L619: 198
L620: 
L621: 199
L622: 
L623: 200
L624: 
L625: 201
L626: 
L627: 202
L628: 
L629: 203
L630: 
L631: 204
L632: 
L633: 205
L634: 
L635: 206
L636: 
L637: 207
L638: 
L639: 208
L640: 
L641: 209
L642: 
L643: 210
L644: 
L645: 211
L646: 
L647: 212
L648: 
L649: 213
L650: 
L651: 214
L652: 
L653: 215
L654: 
L655: 216
L656: 
L657: 217
L658: 
L659: 218
L660: 
L661: 219
L662: 
L663: 220
L664: 
L665: 221
L666: 
L667: 222
L668: 
L669: 223
L670: 
L671: 224
L672: 
L673: 225
L674: 
L675: 226
L676: 
L677: 227
L678: 
L679: 228
L680: 
L681: 229
L682: 
L683: 230
L684: 
L685: 231
L686: 
L687: 232
L688: 
L689: 233
L690: 
L691: 234
L692: 
L693: 235
L694: 
L695: 236
L696: 
L697: 237
L698: 
L699: 238
L700: 
L701: 239
L702: 
L703: 240
L704: 
L705: 241
L706: 
L707: 242
L708: 
L709: 243
L710: 
L711: 244
L766: from typing import Any, List, Tuple
L767: 
L768: class SliceByTimeEventsTargets:
L769: 
L770: """
L771: 
L772: Modified from tonic.slicers.SliceByTimeEventsTargets in the Tonic Library
L773: 
L774: Slices an event array along fixed time window and overlap size. The number of bins depends
L775: 
L776: on the length of the recording. Targets are copied.
L777: 
L778: > <overlap>
L779: 
L780: >| window1 |
L781: 
L782: > | window2 |
L783: 
L784: Parameters:
L785: 
L786: time_window (int): time for window length (same unit as event timestamps)
L787: 
L788: overlap (int): overlap (same unit as event timestamps)
L789: include_incomplete (bool): include the last incomplete slice that has shorter time
L790: 
L791: """
L792: 
L793: def __init__(self,time_window, overlap=0.0, seq_length=30, seq_stride=15, include_incomplete=False) -> None:
L794: 
L795: self.time_window= time_window
L796: 
L797: self.overlap= overlap
L798: 
L799: self.seq_length=seq_length
L800: 
L801: self.seq_stride=seq_stride
L802: 
L803: self.include_incomplete=include_incomplete
L804: 
L805: def slice(self, data: np.ndarray, targets: int) -> List[np.ndarray]:
L806: 
L807: metadata = self.get_slice_metadata(data, targets)
L808: return self.slice_with_metadata(data, targets, metadata)
L809: 
L810: def get_slice_metadata(
L811: 
L812: self, data: np.ndarray, targets: int
L813: 
L814: ) -> List[Tuple[int, int]]:
L815: 
L816: t = data["t"]
L817: 
L818: stride = self.time_window - self.overlap
L819: 
L820: assert stride > 0
L821: 
L822: if self.include_incomplete:
L823: 
L824: n_slices = int(np.ceil(((t[-1] - t[0]) - self.time_window) / stride) + 1)
L825: 
L826: else:
L827: 
L828: n_slices = int(np.floor(((t[-1] - t[0]) - self.time_window) / stride) + 1)
L829: 
L830: n_slices = max(n_slices, 1) # for strides larger than recording time
L831: window_start_times = np.arange(n_slices) * stride + t[0]
L832: 
L833: window_end_times = window_start_times + self.time_window
L834: 
L835: indices_start = np.searchsorted(t, window_start_times)[:n_slices]
L836: 
L837: indices_end = np.searchsorted(t, window_end_times)[:n_slices]
L838: 
L839: if not self.include_incomplete:
L840: # get the strided indices for loading labels
L841: 
L842: label_indices_start = np.arange(0, targets.shape[0]-self.seq_length, self.seq_stride)
L843: 
L844: label_indices_end = label_indices_start + self.seq_length
L845: 
L846: else:
L847: 
L848: label_indices_start = np.arange(0, targets.shape[0], self.seq_stride)
L849: 
L850: label_indices_end = label_indices_start + self.seq_length
L851: # the last label indices end should be the last label
L852: 
L853: label_indices_end[-1] = targets.shape[0]
L854: 
L855: assert targets.shape[0] >= label_indices_end[-1]
L856: 
L857: return list(zip(zip(indices_start, indices_end), zip(label_indices_start, label_indices_end)))
L858: 
L859: @staticmethod
L860: 
L861: def slice_with_metadata(
L862: 
L863: data: np.ndarray, targets: int, metadata: List[Tuple[Tuple[int, int], Tuple[int, int]]]
L864: 
L865: ):
L866: 
L867: return_data = []
L868: 
L869: return_target = []
L870: 
L871: for tuple1, tuple2 in metadata:
L872: 
L873: return_data.append(data[tuple1[0]:tuple1[1]])
L874: return_target.append(targets[tuple2[0]:tuple2[1]])
L875: 
L876: return return_data, return_target
L877: 
L878: class SliceLongEventsToShort:
L879: 
L880: def __init__(self, time_window, overlap, include_incomplete):
L881: 
L882: """
L883: 
L884: Initialize the transformation.
L885: 
L886: Args:
L887: 
L888: - time_window (int): The length of each sub-sequence.
L889: 
L890: """
L891: 
L892: self.time_window = time_window
L893: 
L894: self.overlap = overlap
L895: 
L896: self.include_incomplete = include_incomplete
L897: 
L898: def __call__(self, events):
L899: 
L900: return slice_events_by_time(events, self.time_window, self.overlap, self.include_incomplete)
L901: class EventSlicesToVoxelGrid:
L902: 
L903: def __init__(self, sensor_size, n_time_bins, per_channel_normalize):
L904: 
L905: """
L906: 
L907: Initialize the transformation.
L908: 
L909: Args:
L910: 
L911: - sensor_size (tuple): The size of the sensor.
L912: 
L913: - n_time_bins (int): The number of time bins.
L914: 
L915: """
L916: 
L917: self.sensor_size = sensor_size
L918: 
L919: self.n_time_bins = n_time_bins
L920: 
L921: self.per_channel_normalize = per_channel_normalize
L922: 
L923: def __call__(self, event_slices):
L924: 
L925: """
L926: 
L927: Apply the transformation to the given event slices.
L928: 
L929: Args:
L930: 
L931: - event_slices (Tensor): The input event slices.
L932: Returns:
L933: 
L934: - Tensor: A batched tensor of voxel grids.
L935: 
L936: """
L937: 
L938: voxel_grids = []
L939: 
L940: for event_slice in event_slices:
L941: 
L942: voxel_grid = to_voxel_grid_numpy(event_slice, self.sensor_size, self.n_time_bins)
L943: 
L944: voxel_grid = voxel_grid.squeeze(-3)
L945: 
L946: if self.per_channel_normalize:
L947: # Calculate mean and standard deviation only at non-zero values
L948: 
L949: non_zero_entries = (voxel_grid != 0)
L950: 
L951: for c in range(voxel_grid.shape[0]):
L952: 
L953: mean_c = voxel_grid[c][non_zero_entries[c]].mean()
L954: 
L955: std_c = voxel_grid[c][non_zero_entries[c]].std()
L956: 
L957: voxel_grid[c][non_zero_entries[c]] = (voxel_grid[c][non_zero_entries[c]] - mean_c) / (std_c + 1e-10)
L958: 
L959: voxel_grids.append(voxel_grid)
L960: 
L961: return np.array(voxel_grids).astype(np.float32)
L962: 
L963: class SplitSequence:
L964: 
L965: def __init__(self, sub_seq_length, stride):
L966: 
L967: """
L968: Initialize the transformation.
L969: 
L970: Args:
L971: 
L972: - sub_seq_length (int): The length of each sub-sequence.
L973: 
L974: - stride (int): The stride between sub-sequences.
L975: 
L976: """
L977: 
L978: self.sub_seq_length = sub_seq_length
L979: 
L980: self.stride = stride
L981: 
L982: def __call__(self, sequence, labels):
L983: 
L984: """
L985: 
L986: Apply the transformation to the given sequence and labels.
L987: 
L988: Args:
L989: 
L990: - sequence (Tensor): The input sequence of frames.
L991: 
L992: - labels (Tensor): The corresponding labels.
L993: 
L994: Returns:
L995: 
L996: - Tensor: A batched tensor of sub-sequences.
L997: - Tensor: A batched tensor of corresponding labels.
L998: 
L999: """
L1000: 
L1001: sub_sequences = []
L1002: 
L1003: sub_labels = []
L1004: 
L1005: for i in range(0, len(sequence) - self.sub_seq_length + 1, self.stride):
L1006: 
L1007: sub_seq = sequence[i:i + self.sub_seq_length]
L1008: 
L1009: sub_seq_labels = labels[i:i + self.sub_seq_length]
L1010: 
L1011: sub_sequences.append(sub_seq)
L1012: 
L1013: sub_labels.append(sub_seq_labels)
L1014: 
L1015: return np.stack(sub_sequences), np.stack(sub_labels)
L1016: 
L1017: class SplitLabels:
L1018: 
L1019: def __init__(self, sub_seq_length, stride):
L1020: 
L1021: """
L1022: 
L1023: Initialize the transformation.
L1024: 
L1025: Args:
L1026: - sub_seq_length (int): The length of each sub-sequence.
L1027: 
L1028: - stride (int): The stride between sub-sequences.
L1029: 
L1030: """
L1031: 
L1032: self.sub_seq_length = sub_seq_length
L1033: 
L1034: self.stride = stride
L1035: # print(f"stride is {self.stride}")
L1036: 
L1037: def __call__(self, labels):
L1038: 
L1039: """
L1040: 
L1041: Apply the transformation to the given sequence and labels.
L1042: 
L1043: Args:
L1044: 
L1045: - labels (Tensor): The corresponding labels.
L1046: 
L1047: Returns:
L1048: 
L1049: - Tensor: A batched tensor of corresponding labels.
L1050: 
L1051: """
L1052: 
L1053: sub_labels = []
L1054: 
L1055: for i in range(0, len(labels) - self.sub_seq_length + 1, self.stride):
L1056: 
L1057: sub_seq_labels = labels[i:i + self.sub_seq_length]
L1058: 
L1059: sub_labels.append(sub_seq_labels)
L1060: 
L1061: return np.stack(sub_labels)
L1062: 
L1063: class ScaleLabel:
L1064: def __init__(self, scaling_factor):
L1065: 
L1066: """
L1067: 
L1068: Initialize the transformation.
L1069: 
L1070: Args:
L1071: 
L1072: - scaling_factor (float): How much the spatial scaling was done on input
L1073: 
L1074: """
L1075: 
L1076: self.scaling_factor = scaling_factor
L1077: 
L1078: def __call__(self, labels):
L1079: 
L1080: """
L1081: 
L1082: Apply the transformation to the given sequence and labels.
L1083: 
L1084: Args:
L1085: 
L1086: - labels (Tensor): The corresponding labels.
L1087: 
L1088: Returns:
L1089: 
L1090: - Tensor: A batched tensor of corresponding labels.
L1091: 
L1092: """
L1093: 
L1094: labels[:,:2] = labels[:,:2] * self.scaling_factor
L1095: 
L1096: return labels
L1097: 
L1098: class TemporalSubsample:
L1099: def __init__(self, temporal_subsample_factor):
L1100: 
L1101: self.temp_subsample_factor = temporal_subsample_factor
L1102: 
L1103: def __call__(self, labels):
L1104: 
L1105: """
L1106: 
L1107: temorally subsample the labels
L1108: 
L1109: """
L1110: 
L1111: interval = int(1/self.temp_subsample_factor)
L1112: 
L1113: return labels[::interval]
L1114: 
L1115: class NormalizeLabel:
L1116: 
L1117: def __init__(self, pseudo_width, pseudo_height):
L1118: 
L1119: """
L1120: 
L1121: Initialize the transformation.
L1122: 
L1123: Args:
L1124: 
L1125: - scaling_factor (float): How much the spatial scaling was done on input
L1126: 
L1127: """
L1128: 
L1129: self.pseudo_width = pseudo_width
L1130: self.pseudo_height = pseudo_height
L1131: 
L1132: def __call__(self, labels):
L1133: 
L1134: """
L1135: 
L1136: Apply normalization on label, with pseudo width and height
L1137: 
L1138: Args:
L1139: 
L1140: - labels (Tensor): The corresponding labels.
L1141: 
L1142: Returns:
L1143: 
L1144: - Tensor: A batched tensor of corresponding labels.
L1145: 
L1146: """
L1147: 
L1148: labels[:, 0] = labels[:, 0] / self.pseudo_width
L1149: 
L1150: labels[:, 1] = labels[:, 1] / self.pseudo_height
L1151: 
L1152: return labels
L1153: 
L1154: You can’t perform that action at this time.
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
 (https://github.com/EETChallenge/challenge_demo_code/raw/refs/heads/master/test.py)
L0: """
L1: Author: Zuowen Wang
L2: Affiliation: Insitute of Neuroinformatics, University of Zurich and ETH Zurich
L3: Email: wangzu@ethz.ch
L4: """
L5: 
L6: import argparse, json, os, mlflow, csv
L7: import torch
L8: import torch.nn as nn
L9: import torch.optim as optim
L10: from torch.utils.data import DataLoader
L11: from model.BaselineEyeTrackingModel import CNN_GRU
L12: from dataset import ThreeETplus_Eyetracking, ScaleLabel, NormalizeLabel, \
L13:     TemporalSubsample, NormalizeLabel, SliceLongEventsToShort, \
L14:     EventSlicesToVoxelGrid, SliceByTimeEventsTargets
L15: import tonic.transforms as transforms
L16: from tonic import SlicedDataset, DiskCachedDataset
L17: 
L18: 
L19: def main(args):
L20:     # Load hyperparameters from JSON configuration file
L21:     if args.config_file:
L22:         with open(os.path.join('./configs', args.config_file), 'r') as f:
L23:             config = json.load(f)
L24:         # Overwrite hyperparameters with command-line arguments
L25:         for key, value in vars(args).items():
L26:             if value is not None:
L27:                 config[key] = value
L28:         args = argparse.Namespace(**config)
L29:     else:
L30:         raise ValueError("Please provide a JSON configuration file.")
L31: 
L32:     # also dump the args to a JSON file in MLflow artifact
L33:     with open(os.path.join(mlflow.get_artifact_uri(), "args.json"), 'w') as f:
L34:         json.dump(vars(args), f)
L35: 
L36:     # Define your model, optimizer, and criterion
L37:     model = eval(args.architecture)(args).to(args.device)
L38:     # test data loader always cuts the event stream with the labeling frequency
L39:     factor = args.spatial_factor
L40:     temp_subsample_factor = args.temporal_subsample_factor
L41: 
L42:     label_transform = transforms.Compose([
L43:         ScaleLabel(factor),
L44:         TemporalSubsample(temp_subsample_factor),
L45:         NormalizeLabel(pseudo_width=640*factor, pseudo_height=480*factor)
L46:     ])
L47: 
L48:     test_data_orig = ThreeETplus_Eyetracking(save_to=args.data_dir, split="test", \
L49:                     transform=transforms.Downsample(spatial_factor=factor),
L50:                     target_transform=label_transform)
L51: 
L52:     slicing_time_window = args.test_length*int(10000/temp_subsample_factor) #microseconds
L53: 
L54:     test_slicer=SliceByTimeEventsTargets(slicing_time_window, overlap=0, \
L55:                     seq_length=args.test_length, seq_stride=args.test_stride, include_incomplete=True)
L56: 
L57:     post_slicer_transform = transforms.Compose([
L58:         SliceLongEventsToShort(time_window=int(10000/temp_subsample_factor), overlap=0, include_incomplete=True),
L59:         EventSlicesToVoxelGrid(sensor_size=(int(640*factor), int(480*factor), 2), \
L60:                                 n_time_bins=args.n_time_bins, per_channel_normalize=args.voxel_grid_ch_normaization)
L61:     ])
L62: 
L63:     test_data = SlicedDataset(test_data_orig, test_slicer, transform=post_slicer_transform)
L64: 
L65:     # Uncomment the following lines to use the cached dataset
L66:     # Use with caution! Don't forget to update the cache path if you change the dataset or the slicing parameters
L67: 
L68:     # test_data = SlicedDataset(test_data_orig, test_slicer, transform=post_slicer_transform, \
L69:     #     metadata_path=f"./metadata/3et_test_l{args.test_length}s{args.test_stride}_ch{args.n_time_bins}")
L70: 
L71:     # cache the dataset to disk to speed up training. The first epoch will be slow, but the following epochs will be fast.
L72:     # test_data = DiskCachedDataset(test_data, \
L73:     #                               cache_path=f'./cached_dataset/test_l{args.test_length}s{args.test_stride}_ch{args.n_time_bins}')
L74: 
L75:     assert args.batch_size == 1
L76:     # otherwise the collate function will through an error.
L77:     # This is only used in combination of include_incomplete=True during testing
L78:     test_loader = DataLoader(test_data, batch_size=args.batch_size, shuffle=False, \
L79:                             num_workers=int(os.cpu_count()-2))
L80: 
L81:     # load weights from a checkpoint
L82:     if args.checkpoint:
L83:         model.load_state_dict(torch.load(args.checkpoint))
L84:     else:
L85:         raise ValueError("Please provide a checkpoint file.")
L86: 
L87:     # evaluate on the validation set and save the predictions into a csv file.
L88:     with open(args.output_path, 'w', newline='') as csvfile:
L89:         csv_writer = csv.writer(csvfile, delimiter=',')
L90:         # add column names 'row_id', 'x', 'y'
L91:         csv_writer.writerow(['row_id', 'x', 'y'])
L92:         row_id = 0
L93:         for batch_idx, (data, target_placeholder) in enumerate(test_loader):
L94:             data = data.to(args.device)
L95:             output = model(data)
L96: 
L97:             # Important!
L98:             # cast the output back to the downsampled sensor space (80x60)
L99:             output = output * torch.tensor((640*factor, 480*factor)).to(args.device)
L100: 
L101:             for sample in range(target_placeholder.shape[0]):
L102:                 for frame_id in range(target_placeholder.shape[1]):
L103:                     row_to_write = output[sample][frame_id].tolist()
L104:                     # prepend the row_id
L105:                     row_to_write.insert(0, row_id)
L106:                     csv_writer.writerow(row_to_write)
L107:                     row_id += 1
L108: 
L109: 
L110: if __name__ == "__main__":
L111:     import argparse
L112:     parser = argparse.ArgumentParser()
L113: 
L114:     # a config file
L115:     parser.add_argument("--config_file", type=str, default='test_config', \
L116:                         help="path to JSON configuration file")
L117:     # load weights from a checkpoint
L118:     parser.add_argument("--checkpoint", type=str, help="path to checkpoint")
L119:     parser.add_argument("--output_path", type=str, default='./submission.csv')
L120: 
L121:     args = parser.parse_args()
L122: 
L123:     main(args)
