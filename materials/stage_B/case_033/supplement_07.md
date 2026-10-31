# Saved primary-source web extracts

Partial extracts; source URLs and original line gaps are retained where recorded.

challenge_demo_code/dataset/custom_transforms.py at master · EETChallenge/challenge_demo_code · GitHub (https://github.com/EETChallenge/challenge_demo_code/blob/master/dataset/custom_transforms.py)
L157:   * cite64†Code L158:   * cite66†Issues 0 L159:   * cite67†Pull requests 0 L160:   * cite68†Actions L161:   * cite69†Projects L162:   * cite70†Security and quality 0 L163:   * cite71†Insights L164: 
L165: Additional navigation options
L166: ## Files Expand file tree
L167: 
L168: master
L169: 
L170: ## Breadcrumbs
L171: 
L172:   1. cite72†challenge_demo_code L173:   2. /cite73†dataset L174: 
L175: /
L176: 
L177: # custom_transforms.py
L178: 
L179: Copy path
L180: 
L181: [Input: Go to file]
L182: 
L183: Blame More file actions
L184: 
L185: Blame More file actions
L186: 
L187: ## Latest commit
L188: 
L189: 
L190: 
L191: ## History
L192: 
L193: History
L194: 
L195: master
L196: 
L197: ## Breadcrumbs
L198: 
L199:   1. cite72†challenge_demo_code L200:   2. /cite73†dataset L201: 
L202: /
L203: 
L204: # custom_transforms.py
L205: 
L206: Copy path
L207: 
L208: Top
L209: ## File metadata and controls
L210: 
L211:   * Code
L212: 
L213:   * Blame
L214: 
L215: 265 lines (208 loc) · 8.96 KB
L216: 
L217: cite74†Raw L218: 
L219: Copy raw file
L220: 
L221: Download raw file
L222: 
L223: Open symbols panel
L224: 
L225: Edit and raw actions
L226: 
L227: 1
L228: 
L229: 2
L230: 
L231: 3
L232: 
L233: 4
L234: 
L235: 5
L236: 
L237: 6
L238: 
L239: 7
L240: 
L241: 8
L242: 
L243: 9
L244: 
L245: 10
L246: 
L247: 11
L248: 
L249: 12
L250: 
L251: 13
L252: 
L253: 14
L254: 
L255: 15
L256: 
L257: 16
L258: 
L259: 17
L260: 
L261: 18
L262: 
L263: 19
L264: 
L265: 20
L266: 
L267: 21
L268: 
L269: 22
L270: 
L271: 23
L272: 
L273: 24
L274: 
L275: 25
L276: 
L277: 26
L278: 
L279: 27
L280: 
L281: 28
L282: 
L283: 29
L284: 
L285: 30
L286: 
L287: 31
L288: 
L289: 32
L290: 
L291: 33
L292: 
L293: 34
L294: 
L295: 35
L296: 
L297: 36
L298: 
L299: 37
L300: 
L301: 38
L302: 
L303: 39
L304: 
L305: 40
L306: 
L307: 41
L308: 
L309: 42
L310: 
L311: 43
L312: 
L313: 44
L314: 
L315: 45
L316: 
L317: 46
L318: 
L319: 47
L320: 
L321: 48
L322: 
L323: 49
L324: 
L325: 50
L326: 
L327: 51
L328: 
L329: 52
L330: 
L331: 53
L332: 
L333: 54
L334: 
L335: 55
L336: 
L337: 56
L338: 
L339: 57
L340: 
L341: 58
L342: 
L343: 59
L344: 
L345: 60
L346: 
L347: 61
L348: 
L349: 62
L350: 
L351: 63
L352: 
L353: 64
L354: 
L355: 65
L356: 
L357: 66
L358: 
L359: 67
L360: 
L361: 68
L362: 
L363: 69
L364: 
L365: 70
L366: 
L367: 71
L368: 
L369: 72
L370: 
L371: 73
L372: 
L373: 74
L374: 
L375: 75
L376: 
L377: 76
L378: 
L379: 77
L380: 
L381: 78
L382: 
L383: 79
L384: 
L385: 80
L386: 
L387: 81
L388: 
L389: 82
L390: 
L391: 83
L392: 
L393: 84
L394: 
L395: 85
L396: 
L397: 86
L398: 
L399: 87
L400: 
L401: 88
L402: 89
L403: 
L404: 90
L405: 
L406: 91
L407: 
L408: 92
L409: 
L410: 93
L411: 
L412: 94
L413: 
L414: 95
L415: 
L416: 96
L417: 
L418: 97
L419: 
L420: 98
L421: 
L422: 99
L423: 
L424: 100
L425: 
L426: 101
L427: 
L428: 102
L429: 
L430: 103
L431: 
L432: 104
L433: 
L434: 105
L435: 
L436: 106
L437: 
L438: 107
L439: 
L440: 108
L441: 
L442: 109
L443: 
L444: 110
L445: 
L446: 111
L447: 
L448: 112
L449: 
L450: 113
L451: 
L452: 114
L453: 
L454: 115
L455: 
L456: 116
L457: 
L458: 117
L459: 
L460: 118
L461: 
L462: 119
L463: 
L464: 120
L465: 
L466: 121
L467: 
L468: 122
L469: 
L470: 123
L471: 
L472: 124
L473: 
L474: 125
L475: 
L476: 126
L477: 
L478: 127
L479: 
L480: 128
L481: 
L482: 129
L483: 
L484: 130
L485: 
L486: 131
L487: 
L488: 132
L489: 
L490: 133
L491: 
L492: 134
L493: 
L494: 135
L495: 
L496: 136
L497: 
L498: 137
L499: 
L500: 138
L501: 
L502: 139
L503: 
L504: 140
L505: 
L506: 141
L507: 
L508: 142
L509: 
L510: 143
L511: 
L512: 144
L513: 
L514: 145
L515: 
L516: 146
L517: 
L518: 147
L519: 
L520: 148
L521: 
L522: 149
L523: 
L524: 150
L525: 
L526: 151
L527: 
L528: 152
L529: 
L530: 153
L531: 
L532: 154
L533: 
L534: 155
L535: 
L536: 156
L537: 
L538: 157
L539: 
L540: 158
L541: 
L542: 159
L543: 
L544: 160
L545: 
L546: 161
L547: 
L548: 162
L549: 
L550: 163
L551: 
L552: 164
L553: 
L554: 165
L555: 
L556: 166
L557: 
L558: 167
L559: 
L560: 168
L561: 
L562: 169
L563: 
L564: 170
L565: 
L566: 171
L567: 
L568: 172
L569: 
L570: 173
L571: 
L572: 174
L573: 
L574: 175
L575: 
L576: 176
L577: 
L578: 177
L579: 
L580: 178
L581: 
L582: 179
L583: 
L584: 180
L585: 
L586: 181
L587: 
L588: 182
L589: 
L590: 183
L591: 
L592: 184
L593: 
L594: 185
L595: 
L596: 186
L597: 
L598: 187
L599: 
L600: 188
L601: 
L602: 189
L603: 
L604: 190
L605: 
L606: 191
L607: 
L608: 192
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
L712: 
L713: 245
L714: 
L715: 246
L716: 
L717: 247
L718: 
L719: 248
L720: 
L721: 249
L722: 
L723: 250
L724: 
L725: 251
L726: 
L727: 252
L728: 
L729: 253
L730: 
L731: 254
L732: 
L733: 255
L734: 
L735: 256
L736: 
L737: 257
L738: 
L739: 258
L740: 
L741: 259
L742: 
L743: 260
L744: 
L745: 261
L746: 
L747: 262
L748: 
L749: 263
L750: 
L751: 264
L752: 
L753: 265
L754: 
L755: import numpy as np
L756: 
L757: import torch
L758: 
L759: from tonic.slicers import (
L760: 
L761: slice_events_by_time,
L762: 
L763: )
L764: 
L765: from tonic.functional import to_voxel_grid_numpy
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
challenge_demo_code/configs/sliced_baseline.json at master · EETChallenge/challenge_demo_code · GitHub (https://github.com/EETChallenge/challenge_demo_code/blob/master/configs/sliced_baseline.json)
L82:     * PROGRAMS
L83:       * cite50†Security Lab†securitylab.github.com L84:       * cite51†Maintainer Community†maintainers.github.com L85:       * cite52†Accelerator L86:       * cite53†GitHub Stars†stars.github.com L87:       * cite54†Archive Program†archiveprogram.github.com L88: 
L89:     * REPOSITORIES
L90:       * cite55†Topics L91:       * cite56†Trending L92:       * cite57†Collections L93: 
L94:   * Enterprise
L95: 
L96:     * ENTERPRISE SOLUTIONS
L97:       * cite19†Enterprise platformAI-powered developer platform L98:     * AVAILABLE ADD-ONS
L99:       * cite10†GitHub Advanced SecurityEnterprise-grade security features L100:       * cite58†Copilot for BusinessEnterprise-grade AI features L101:       * cite59†Premium SupportEnterprise-grade 24/7 support L102: 
L103:   * cite60†Pricing L104: 
L105: Type `/` to search
L106: 
L107: cite1†Sign in L108: 
L109: cite61†Sign up Appearance settings
L110: You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert
L111: 
L112: cite62†EETChallenge / cite63†challenge_demo_code Public
L113: 
L114:   * cite64†Notifications You must be signed in to change notification settings
L115:   * cite64†Fork 0 L116:   * cite64†Star L117:   * cite63†Code L118:   * cite65†Issues 0 L119:   * cite66†Pull requests 0 L120:   * cite67†Actions L121:   * cite68†Projects L122:   * cite69†Security and quality 0 L123:   * cite70†Insights L124: 
L125: Additional navigation options
L126: ## Files Expand file tree
L127: 
L128: master
L129: 
L130: ## Breadcrumbs
L131: 
L132:   1. cite71†challenge_demo_code L133:   2. /cite72†configs L134: 
L135: /
L136: 
L137: # sliced_baseline.json
L138: 
L139: Copy path
L140: 
L141: [Input: Go to file]
L142: 
L143: Blame More file actions
L144: 
L145: Blame More file actions
L146: 
L147: ## Latest commit
L148: 
L149: 
L150: 
L151: ## History
L152: 
L153: History
L154: 
L155: master
L156: 
L157: ## Breadcrumbs
L158: 
L159:   1. cite71†challenge_demo_code L160:   2. /cite72†configs L161: 
L162: /
L163: 
L164: # sliced_baseline.json
L165: 
L166: Copy path
L167: 
L168: Top
L169: ## File metadata and controls
L170: 
L171:   * Code
L172: 
L173:   * Blame
L174: 
L175: 25 lines (25 loc) · 659 Bytes
L176: 
L177: cite73†Raw L178: 
L179: Copy raw file
L180: 
L181: Download raw file
L182: 
L183: Open symbols panel
L184: 
L185: Edit and raw actions
L186: 
L187: 1
L188: 
L189: 2
L190: 
L191: 3
L192: 
L193: 4
L194: 
L195: 5
L196: 
L197: 6
L198: 
L199: 7
L200: 
L201: 8
L202: 
L203: 9
L204: 
L205: 10
L206: 
L207: 11
L208: 
L209: 12
L210: 
L211: 13
L212: 
L213: 14
L214: 
L215: 15
L216: 
L217: 16
L218: 
L219: 17
L220: 
L221: 18
L222: 
L223: 19
L224: 
L225: 20
L226: 
L227: 21
L228: 
L229: 22
L230: 
L231: 23
L232: 
L233: 24
L234: 
L235: 25
L236: 
L237: {
L238: 
L239: "device": "cuda:0",
L240: 
L241: "mlflow_path": "./mlruns",
L242: 
L243: "experiment_name": "trial_experiment",
L244: 
L245: "data_dir": "./event_data",
L246: 
L247: "run_name": "trial_run",
L248: 
L249: "architecture": "CNN_GRU",
L250: 
L251: "lr": 0.001,
L252: 
L253: "num_epochs": 200,
L254: 
L255: "batch_size": 20,
L256: "spatial_factor": 0.125,
L257: 
L258: "temporal_subsample_factor": 0.2,
L259: 
L260: "val_interval": 2,
L261: 
L262: "save_k_best": 2,
L263: 
L264: "pixel_tolerances": [5,10,15],
L265: 
L266: "sensor_width": 640,
L267: 
L268: "sensor_height": 480,
L269: 
L270: "train_stride": 15,
L271: 
L272: "val_stride": 30,
L273: 
L274: "train_length": 30,
L275: 
L276: "val_length": 30,
L277: 
L278: "n_time_bins": 3,
L279: 
L280: "voxel_grid_ch_normaization": false,
L281: 
L282: "loss": "weighted_mse"
L283: 
L284: }
L285: 
L286: You can’t perform that action at this time.
GitHub - EETChallenge/challenge_demo_code · GitHub (https://github.com/EETChallenge/challenge_demo_code)
L287: After the raw event sequence is sliced into raw event sub-sequences, we can convert each of them into different event representations. The transformations are defined in the following code sniplet. SliceLongEventsToShort is a transformation that separate the raw event sub-sequences further into (10000us)/temp_subsample_factor time windows.
L288: EventSlicesToVoxelGrid is a transformation that convert each time window into the actual event representation, in this case, voxel grids with args.n_time_bins number of time bins.
L289: 
L290:     post_slicer_transform = transforms.Compose([
L291:         SliceLongEventsToShort(time_window=int(10000/temp_subsample_factor), overlap=0, include_incomplete=True),
L292:         EventSlicesToVoxelGrid(sensor_size=(int(640*factor), int(480*factor), 2), \
L293:                                 n_time_bins=args.n_time_bins, per_channel_normalize=args.voxel_grid_ch_normaization)
L294:     ])
L295: We then pass these transformations to the Tonic SlicedDataset class to post process the loaded raw events:
L296: 
L297:     train_data = SlicedDataset(train_data_orig, train_slicer, \
L298:       transform=post_slicer_transform, metadata_path=f"./metadata/3et_train_tl_{args.train_length}_ts{args.train_stride}_ch{args.n_time_bins}")
L299: The SlicedDataset has a convenient function to cache the indices of how the raw events are sliced, when argument metadata_path is provided not None. But be careful if you provided the same metadata_path for different slicing strategies, the SlicedDataset will ignore the slicing parameters and use the old indices, causing unexpected results.
L300: We can further cache the transformed voxel grid representation on the disk to further speed up data preprocessing. This is done by the DiskCachedDataset class. It will slow done the first time loading the data but for future epoch and future training, it will be much faster.
L301: 
L302:     train_data = DiskCachedDataset(train_data, \
L303:       cache_path=f'./cached_dataset/train_tl_{args.train_length}_ts{args.train_stride}_ch{args.n_time_bins}')
L304:     # at this point we can pass the dataset to the standard pytorch dataloader.
L305:     train_loader = DataLoader(train_data, batch_size=args.batch_size, shuffle=True, num_workers=int(os.cpu_count()-2), pin_memory=True)
L306: You can easily find a lot of cite111†data augmentation†tonic.readthedocs.io methods in the cite109†Tonic†tonic.readthedocs.io library and include them in the dataloader to further improve the performance of your model.
L307: #### Labeling
L308: 
L309: The ground truth is labeled at 100Hz and consists of two parts for each label (x, y, close) with
L310: 
L311:   * labeling of the pupil center coordinates (x,y).
L312: 
L313:   * a binary value 'close' indicating whether the eye blinks or not (0 for opening, 1 for closing).
L314: Labels (x,y,close) for the train split are provided at frequency of 100Hz. The user is free to decide at if they would like to downsample this frequency and whether to use the close label or not. In the training sample pipeline we provided, the labels are downsample to 20Hz and we do not use the close label by default. For the test set, we will evaluate the prediction at 20Hz only. If you would like to alter the data loading pipeline, please be aware this downsampling.
L315: #### Dataset splitting
L316: 
L317: We use 12 recordings for testing (test split) and the remaining recordings (train split) are for the user to train and validate their methods. The users are free to divide the training and validation sets from the training data.
L318: 
L319: * * *
L320: 
L321: ## Performance of baseline methods
L322: #### Baseline performance with standard event voxel grids
L323: 
L324: We conducted benchmarking of the dataset with several baseline methods. The baseline methods are trained with the standard event voxel grid representation. The results are shown in the following table. The inference latency is measured on a single RTX 3090 GPU with batch size = 1.
L325: 
L326: Method  | GPU  | Averaged Distance  | P10 Accuracy  | Inference Latency (bs=1)
L327: --- | --- | --- | --- | ---
L328: CNN_GRU  | RTX 3090 24 Gb  | 8.99  | 0.63  | -
L329: #### Monitoring and logging of training
L330: 
L331: We provide code sample together with cite112†mlflow†mlflow.org for monitoring training progress and tasks. It will log the essnetial informations under the folder 'mlruns'. To monitor the runs, simply run the following command in the terminal:
L332: 
L333:     mlflow ui --port 5000
L334: 
L335: Then open the browser and go to cite113†http://localhost:5000†localhost . You will see the following interface:
L336: 
L337: * * *
L338: ## Prepare test results and submission
L339: 
L340: We provide a sample script (test.py) to prepare your test results for submission. The script will generate a submission.csv file for submitting to the Kaggle challenge server.
L341: 
L342: Please be aware that if your data loading strategy is different from the standard strategy we provided, you need to modify the test set loader according to your method.
L343: 
L344:     `python .test.py --config [CONFIG_PATH] --checkpoint [CHECKPOINT_PATH] --output_path [OUTPUT_PATH]
L345:     `
L346: If you trained your model with mlflow, the checkpoint should be saved in mlruns folder. You can find the checkpoint path in the mlflow ui under arfitacts section.
L347: 
L348: * * *
L349: ## Evaluation of your submission
L350: 
L351: We request that you submit a `submission.csv` file, which should contain two columns 'x' and 'y'. Notice that the range of x is [0, 80] and y is [0, 60].
L352: #### scoring functions
L353: 
L354: There are two evaluation metrics for the challenge: p10 accuracy (used for leaderboard on Kaggle) and averaged euclidean distances (also taken into consideration for the report).
L355: 
L356: The p10 accuracy is defined as the percentage of the predictions that are within 10 pixels of the ground truths (in the downsampled 80x60 spatial space). The averaged euclidean distance is defined as the average euclidean distance between the predictions and the ground truths.
L357: #### inference speed will be taken into consideration
L358: 
L359: We do not measure the latency of your method in the score board. But in the final report, the inference speed (latency) is required and is a very important metric for evaluating the final report. That is said if your method requires huge amount of computation, it is probably not a good method for practical real-time eye tracking applications.
L360: 
L361: * * *
L362: 
L363: ## Contact
L364: 
L365:   * Zuowen Wang (zuowen@ini.uzh.ch)
L366:   * Qinyu Chen (q.chen@liacs.leidenuniv.nl)
