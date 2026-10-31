# Saved primary-source web extracts

Partial extracts; source URLs and original line gaps are retained where recorded.

 (https://raw.githubusercontent.com/EETChallenge/challenge_demo_code/master/dataset/ThreeET_plus.py)
L0: import os
L1: from typing import Any, Callable, Optional, Tuple
L2: import h5py
L3: import numpy as np
L4: 
L5: from tonic.dataset import Dataset
L6: 
L7: class ThreeETplus_Eyetracking(Dataset):
L8:     """3ET DVS eye tracking `3ET <https://github.com/qinche106/cb-convlstm-eyetracking>`_
L9:     ::
L10: 
L11:         @article{chen20233et,
L12:             title={3ET: Efficient Event-based Eye Tracking using a Change-Based ConvLSTM Network},
L13:             author={Chen, Qinyu and Wang, Zuowen and Liu, Shih-Chii and Gao, Chang},
L14:             journal={arXiv preprint arXiv:2308.11771},
L15:             year={2023}
L16:         }
L17: 
L18:         authors: Qinyu Chen^{1,2}, Zuowen Wang^{1}
L19:         affiliations: 1. Institute of Neuroinformatics, University of Zurich and ETH Zurich, Switzerland
L20:                       2. Univeristy of Leiden, Netherlands
L21: 
L22:     Parameters:
L23:         save_to (string): Location to save files to on disk.
L24:         transform (callable, optional): A callable of transforms to apply to the data.
L25:         split (string, optional): The dataset split to use, ``train`` or ``val``.
L26:         target_transform (callable, optional): A callable of transforms to apply to the targets/labels.
L27:         transforms (callable, optional): A callable of transforms that is applied to both data and
L28:                                          labels at the same time.
L29: 
L30:     Returns:
L31:          A dataset object that can be indexed or iterated over.
L32:          One sample returns a tuple of (events, targets).
L33:     """
L34:     sensor_size = (640, 480, 2)
L35:     dtype = np.dtype([("t", int), ("x", int), ("y", int), ("p", int)])
L36:     ordering = dtype.names
L37: 
L38:     def __init__(
L39:         self,
L40:         save_to: str,
L41:         split: str = "train",
L42:         transform: Optional[Callable] = None,
L43:         target_transform: Optional[Callable] = None,
L44:         transforms: Optional[Callable] = None,
L45:     ):
L46:         super().__init__(
L47:             save_to,
L48:             transform=transform,
L49:             target_transform=target_transform,
L50:             transforms=transforms,
L51:         )
L52: 
L53:         data_dir = save_to
L54:         data_list_dir = './dataset'
L55:         # Load filenames from the provided lists
L56:         if split == "train":
L57:             filenames = self.load_filenames(os.path.join(data_list_dir, "train_files.txt"))
L58:         elif split == "val":
L59:             filenames = self.load_filenames(os.path.join(data_list_dir, "val_files.txt"))
L60:         elif split == "test":
L61:             filenames = self.load_filenames(os.path.join(data_list_dir, "test_files.txt"))
L62:         else:
L63:             raise ValueError("Invalid split name")
L64: 
L65:         # Get the data file paths and target file paths
L66:         if split == "train" or split == "val":
L67:             self.data = [os.path.join(data_dir, "train", f, f + ".h5") for f in filenames]
L68:             self.targets = [os.path.join(data_dir, "train", f, "label.txt") for f in filenames]
L69:         elif split == "test":
L70:             self.data = [os.path.join(data_dir, "test", f, f + ".h5") for f in filenames]
L71:             # for test set, we load the placeholder labels with all zeros
L72:             self.targets = [os.path.join(data_dir, "test", f, "label_zeros.txt") for f in filenames]
L73: 
L74:     def __getitem__(self, index: int) -> Tuple[Any, Any]:
L75:         """
L76:         Returns:
L77:             (events, target) where target is index of the target class.
L78:         """
L79:         # get events from .h5 file
L80:         with h5py.File(self.data[index], "r") as f:
L81:             # original events.dtype is dtype([('t', '<u8'), ('x', '<u8'), ('y', '<u8'), ('p', '<u8')])
L82:             # t is in us
L83:             events = f["events"][:].astype(self.dtype)
L84:             events['p'] = events['p']*2 -1  # convert polarity to -1 and 1
L85: 
L86:         # load the sparse labels
L87:         with open(self.targets[index], "r") as f:
L88:             # target is at the frequency of 100 Hz. It will be downsampled to 20 Hz in the target transformation
L89:             target = np.array(
L90:                 [list(map(float, line.strip('()\n').split(', '))) for line in f.readlines()], np.float32)
L91: 
L92:         if self.transform is not None:
L93:             events = self.transform(events)
L94:         if self.target_transform is not None:
L95:             target = self.target_transform(target)
L96:         if self.transforms is not None:
L97:             events, target = self.transforms(events, target)
L98:         return events, target
L99: 
L100:     def __len__(self):
L101:         return len(self.data)
L102: 
L103:     def _check_exists(self):
L104:         return self._is_file_present()
L105: 
L106:     def load_filenames(self, path):
L107:         with open(path, "r") as f:
L108:             return [line.strip() for line in f.readlines()]
L0: Failed to fetch https://raw.githubusercontent.com/EETChallenge/challenge_demo_code/master/dataset/custom_transforms.py: Cache miss
 (https://github.com/EETChallenge/challenge_demo_code/raw/refs/heads/master/calculate_metrics.ipynb)
L0: {
L1:  "cells": [
L2:   {
L3:    "cell_type": "code",
L4:    "execution_count": null,
L5:    "metadata": {},
L6:    "outputs": [],
L7:    "source": [
L8:     "import torch\n",
L9:     "import pandas as pd\n",
L10:     "import numpy as np\n",
L11:     "import torch\n",
L12:     "import os"
L13:    ]
L14:   },
L15:   {
L16:    "cell_type": "code",
L17:    "execution_count": null,
L18:    "metadata": {},
L19:    "outputs": [],
L20:    "source": [
L21:     "def p_acc(target, prediction, pixel_tolerances=[1,3,5,10]):\n",
L22:     "    \"\"\"\n",
L23:     "    Calculate the accuracy of prediction\n",
L24:     "    :param target: (N, seq_len, 2) tensor, seq_len could be 1\n",
L25:     "    :param prediction: (N, seq_len, 2) tensor\n",
L26:     "    :return: a dictionary of p-total correct and batch size of this batch\n",
L27:     "    \"\"\"\n",
L28:     "    # flatten the N and seqlen dimension of target and prediction\n",
L29:     "    target = target.reshape(-1, 2)\n",
L30:     "    prediction = prediction.reshape(-1, 2)\n",
L31:     "\n",
L32:     "    dis = target - prediction\n",
L33:     "    dist = torch.norm(dis, dim=-1)\n",
L34:     "\n",
L35:     "    total_correct = {}\n",
L36:     "    for p_tolerance in pixel_tolerances:\n",
L37:     "        total_correct[f'p{p_tolerance}'] = torch.sum(dist < p_tolerance)\n",
L38:     "\n",
L39:     "    bs_times_seqlen = target.shape[0]\n",
L40:     "    return total_correct, bs_times_seqlen"
L41:    ]
L42:   },
L43:   {
L44:    "cell_type": "code",
L45:    "execution_count": null,
L46:    "metadata": {},
L47:    "outputs": [],
L48:    "source": [
L49:     "def px_euclidean_dist(target, prediction):\n",
L50:     "    \"\"\"\n",
L51:     "    Calculate the total pixel euclidean distance between target and prediction\n",
L52:     "    in a batch over the sequence length\n",
L53:     "    :param target: (N, seqlen, 2) tensor\n",
L54:     "    :param prediction: (N, seqlen, 2) tensor\n",
L55:     "    :return: total pixel euclidean distance and sample numbers\n",
L56:     "    \"\"\"\n",
L57:     "    # flatten the N and seqlen dimension of target and prediction\n",
L58:     "    target = target.reshape(-1, 2)[:, :2]\n",
L59:     "    prediction = prediction.reshape(-1, 2)\n",
L60:     "\n",
L61:     "    dis = target - prediction\n",
L62:     "    dist = torch.norm(dis, dim=-1)\n",
L63:     "    total_px_euclidean_dist = torch.sum(dist)\n",
L64:     "    sample_numbers = target.shape[0]\n",
L65:     "    return total_px_euclidean_dist, sample_numbers"
L66:    ]
L67:   },
L68:   {
L69:    "cell_type": "code",
L70:    "execution_count": null,
L71:    "metadata": {},
L72:    "outputs": [],
L73:    "source": [
L74:     "def px_manhaten_dist(target, prediction):\n",
L75:     "    \"\"\"\n",
L76:     "    Calculate the total pixel manhaten distance between target and prediction\n",
L77:     "    in a batch over the sequence length\n",
L78:     "    :param target: (N, seqlen, 2) tensor\n",
L79:     "    :param prediction: (N, seqlen, 2) tensor\n",
L80:     "    :return: total pixel manhaten distance and sample numbers\n",
L81:     "    \"\"\"\n",
L82:     "    # flatten the N and seqlen dimension of target and prediction\n",
L83:     "    target = target.reshape(-1, 2)[:, :2]\n",
L84:     "    prediction = prediction.reshape(-1, 2)\n",
L85:     "    dis = target - prediction\n",
L86:     "    dist = torch.sum(torch.abs(dis), dim=-1)\n",
L87:     "    total_px_manhaten_dist = torch.sum(dist)\n",
L88:     "    sample_numbers = target.shape[0]\n",
L89:     "    return total_px_manhaten_dist, sample_numbers"
L90:    ]
L91:   },
L92:   {
L93:    "cell_type": "code",
L94:    "execution_count": null,
L95:    "metadata": {},
L96:    "outputs": [],
L97:    "source": [
L98:     "def calculate_metrics(gt_df, predictions_df):\n",
L99:     "    # Convert the dataframes into PyTorch tensors\n",
L100:     "    gt_tensor = torch.tensor(gt_df[['x', 'y']].values, dtype=torch.float32)\n",
L101:     "    predictions_tensor = torch.tensor(predictions_df[['x', 'y']].values, dtype=torch.float32)\n",
L102:     "\n",
L103:     "    # Calculate pixel tolerated accuracy\n",
L104:     "    total_correct, sample_size = p_acc(gt_tensor, predictions_tensor, pixel_tolerances=[1,3,5,10,15])\n",
L105:     "    # enumerate the tolerances and print the accuracy\n",
L106:     "    print(\"p_acc:\", end=\" \")\n",
L107:     "    for p_tolerance, correct in total_correct.items():\n",
L108:     "        print(f'{p_tolerance}={correct.item() / sample_size:.2%}', end=\", \")\n",
L109:     "    print()\n",
L110:     "    # calculate the px_euclidean_dist\n",
L111:     "    total_px_euclidean_dist, sample_size = px_euclidean_dist(gt_tensor, predictions_tensor)\n",
L112:     "    print(f'px_euclidean_dist: {total_px_euclidean_dist.item() / sample_size:.2f}')\n",
L113:     "\n",
L114:     "    # calculate the px_manhaten_dist\n",
L115:     "    total_px_manhaten_dist, sample_size = px_manhaten_dist(gt_tensor, predictions_tensor)\n",
L116:     "    print(f'px_manhaten_dist: {total_px_manhaten_dist.item() / sample_size:.2f}')\n"
L117:    ]
L118:   },
L119:   {
L120:    "cell_type": "code",
L121:    "execution_count": null,
L122:    "metadata": {},
L123:    "outputs": [],
L124:    "source": [
L125:     "gt_df = pd.read_csv('./gt_orig_merged.csv')\n",
L126:     "\n",
L127:     "# iterate over csv files in a directory\n",
L128:     "folder = './your_submissions/'\n",
L129:     "files = os.listdir(folder)\n",
L130:     "# remove the files that contains null\n",
L131:     "files = [file for file in files if 'null' not in file]\n",
L132:     "# sort files by the Priv_ score\n",
L133:     "sort_files = sorted(files, key=lambda x: float(x.split('_')[-1].split('.')[0]), reverse=True)\n",
L134:     "for filename in sort_files:\n",
L135:     "    if filename.endswith(\".csv\"):\n",
L136:     "        print(filename)\n",
L137:     "        predictions_df = pd.read_csv(os.path.join(folder, filename))\n",
L138:     "\n",
L139:     "        calculate_metrics(gt_df, predictions_df)\n",
L140:     "    else:\n",
L141:     "        continue"
L142:    ]
L143:   }
L144:  ],
L145:  "metadata": {
L146:   "kernelspec": {
L147:    "display_name": "event_eyetracking",
L148:    "language": "python",
L149:    "name": "python3"
L150:   },
L151:   "language_info": {
L152:    "codemirror_mode": {
L153:     "name": "ipython",
L154:     "version": 3
L155:    },
L156:    "file_extension": ".py",
L157:    "mimetype": "text/x-python",
challenge_demo_code/train.py at master · EETChallenge/challenge_demo_code · GitHub (https://github.com/EETChallenge/challenge_demo_code/blob/master/train.py)
L0: cite0†Skip to content L1: ## Navigation Menu
L2: 
L3: cite1†Sign in Appearance settings
L4: 
L5:   * Platform
L6: 
L7:     * AI CODE CREATION
L8:       * cite2†GitHub CopilotWrite better code with AI L9:       * cite3†GitHub Copilot appDirect agents from issue to merge L10:       * cite4†MCP RegistryIntegrate external tools L11: 
L12:     * DEVELOPER WORKFLOWS
L13:       * cite5†ActionsAutomate any workflow L14:       * cite6†CodespacesInstant dev environments L15:       * cite7†IssuesPlan and track work L16:       * cite8†Code ReviewManage code changes L17:       * cite9†Code QualityEnforce quality at merge L18:     * APPLICATION SECURITY
L19:       * cite10†GitHub Advanced SecurityFind and fix vulnerabilities L20:       * cite11†Code securitySecure your code as you build L21:       * cite12†Secret protectionStop leaks before they start L22: 
L23:     * EXPLORE
L24:       * cite13†Why GitHub L25:       * cite14†Documentation†docs.github.com L26:       * cite15†Blog†github.blog L27:       * cite16†Changelog†github.blog L28:       * cite17†Marketplace L29: 
L30: cite18†View all features L31: 
L32:   * Solutions
L33:     * BY COMPANY SIZE
L34:       * cite19†Enterprises L35:       * cite20†Small and medium teams L36:       * cite21†Startups L37:       * cite22†Nonprofits L38: 
L39:     * BY USE CASE
L40:       * cite23†App Modernization L41:       * cite24†DevSecOps L42:       * cite25†DevOps L43:       * cite26†CI/CD L44:       * cite27†View all use cases L45: 
L46:     * BY INDUSTRY
L47:       * cite28†Healthcare L48:       * cite29†Financial services L49:       * cite30†Manufacturing L50:       * cite31†Government L51:       * cite32†View all industries L52: 
L53: cite33†View all solutions L54: 
L55:   * Resources
L56:     * EXPLORE BY TOPIC
L57:       * cite34†AI L58:       * cite35†Software Development L59:       * cite36†DevOps L60:       * cite37†Security L61:       * cite38†View all topics L62: 
L63:     * EXPLORE BY TYPE
L64:       * cite39†Customer stories L65:       * cite40†Events & webinars L66:       * cite41†Ebooks & reports L67:       * cite42†Business insights L68:       * cite43†GitHub Skills†skills.github.com L69:     * SUPPORT & SERVICES
L70:       * cite14†Documentation†docs.github.com L71:       * cite44†Customer support†support.github.com L72:       * cite45†Community forum L73:       * cite46†Trust center L74:       * cite47†Partners L75: 
L76: cite48†View all resources L77: 
L78:   * Open Source
L79: 
L80:     * COMMUNITY
L81:       * cite49†GitHub SponsorsFund open source developers L82:     * PROGRAMS
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
L132:   1. cite71†challenge_demo_code L133: 
L134: /
L135: 
L136: # train.py
L137: 
L138: Copy path
L139: 
L140: [Input: Go to file]
L141: 
L142: Blame More file actions
L143: 
L144: Blame More file actions
L145: 
L146: ## Latest commit
L147: 
L148: 
L149: 
L150: ## History
L151: 
L152: History
L153: 
L154: master
L155: 
L156: ## Breadcrumbs
L157: 
L158:   1. cite71†challenge_demo_code L159: 
L160: /
L161: 
L162: # train.py
L163: 
L164: Copy path
L165: 
L166: Top
L167: ## File metadata and controls
L168: 
L169:   * Code
L170: 
L171:   * Blame
L172: 
L173: 211 lines (170 loc) · 10.7 KB
L174: 
L175: cite72†Raw L176: 
L177: Copy raw file
L178: 
L179: Download raw file
L180: 
L181: Open symbols panel
L182: 
L183: Edit and raw actions
L184: 
L185: 1
L186: 
L187: 2
L188: 
L189: 3
L190: 
L191: 4
L192: 
L193: 5
L194: 
L195: 6
L196: 
L197: 7
L198: 
L199: 8
L200: 
L201: 9
L202: 
L203: 10
L204: 
L205: 11
L206: 
L207: 12
L208: 
L209: 13
L210: 
L211: 14
L212: 
L213: 15
L214: 
L215: 16
L216: 
L217: 17
L218: 
L219: 18
L220: 
L221: 19
L222: 
L223: 20
L224: 
L225: 21
L226: 
L227: 22
L228: 
L229: 23
L230: 
L231: 24
L232: 
L233: 25
L234: 
L235: 26
L236: 
L237: 27
L238: 
L239: 28
L240: 
L241: 29
L242: 
L243: 30
L244: 
L245: 31
L246: 
L247: 32
L248: 
L249: 33
L250: 
L251: 34
L252: 
L253: 35
L254: 
L255: 36
L256: 
L257: 37
L258: 
L259: 38
L260: 
L261: 39
L262: 
L263: 40
L264: 
L265: 41
L266: 
L267: 42
L268: 
L269: 43
L270: 
L271: 44
L272: 
L273: 45
L274: 
L275: 46
L276: 
L277: 47
L278: 
L279: 48
L280: 
L281: 49
L282: 
L283: 50
L284: 
L285: 51
L286: 
L287: 52
L288: 
L289: 53
L290: 
L291: 54
L292: 
L293: 55
L294: 
L295: 56
L296: 
L297: 57
L298: 
L299: 58
L300: 
L301: 59
L302: 
L303: 60
L304: 
L305: 61
L306: 
L307: 62
L308: 
L309: 63
L310: 
L311: 64
L312: 
L313: 65
L314: 
L315: 66
L316: 
L317: 67
L318: 
L319: 68
L320: 
L321: 69
L322: 
L323: 70
L324: 
L325: 71
L326: 
L327: 72
L328: 
L329: 73
L330: 
L331: 74
L332: 
L333: 75
L334: 
L335: 76
L336: 
L337: 77
L338: 
L339: 78
L340: 
L341: 79
L342: 
L343: 80
L344: 
L345: 81
L346: 
L347: 82
L348: 
L349: 83
L350: 
L351: 84
L352: 
L353: 85
L354: 
L355: 86
L356: 
L357: 87
L358: 
L359: 88
L360: 89
L361: 
L362: 90
L363: 
L364: 91
L365: 
L366: 92
L367: 
L368: 93
L369: 
L370: 94
L371: 
L372: 95
L373: 
L374: 96
L375: 
L376: 97
L377: 
L378: 98
L379: 
L380: 99
L381: 
L382: 100
L383: 
L384: 101
L385: 
L386: 102
L387: 
L388: 103
L389: 
L390: 104
L391: 
L392: 105
L393: 
L394: 106
L395: 
L396: 107
L397: 
L398: 108
L399: 
L400: 109
L401: 
L402: 110
L403: 
L404: 111
L405: 
L406: 112
L407: 
L408: 113
L409: 
L410: 114
L411: 
L412: 115
L413: 
L414: 116
L415: 
L416: 117
L417: 
L418: 118
L419: 
L420: 119
L421: 
L422: 120
L423: 
L424: 121
L425: 
L426: 122
L427: 
L428: 123
L429: 
L430: 124
L431: 
L432: 125
L433: 
L434: 126
L435: 
L436: 127
L437: 
L438: 128
L439: 
L440: 129
L441: 
L442: 130
L443: 
L444: 131
L445: 
L446: 132
L447: 
L448: 133
L449: 
L450: 134
L451: 
L452: 135
L453: 
L454: 136
L455: 
L456: 137
L457: 
L458: 138
L459: 
L460: 139
L461: 
L462: 140
L463: 
L464: 141
L465: 
L466: 142
L467: 
L468: 143
L469: 
L470: 144
L471: 
L472: 145
L473: 
L474: 146
L475: 
L476: 147
L477: 
L478: 148
L479: 
L480: 149
L481: 
L482: 150
L483: 
L484: 151
L485: 
L486: 152
L487: 
L488: 153
L489: 
L490: 154
L491: 
L492: 155
L493: 
L494: 156
L495: 
L496: 157
L497: 
L498: 158
L499: 
L500: 159
L501: 
L502: 160
L503: 
L504: 161
L505: 
L506: 162
L507: 
L508: 163
L509: 
L510: 164
L511: 
L512: 165
L513: 
L514: 166
L515: 
L516: 167
L517: 
L518: 168
L519: 
L520: 169
L521: 
L522: 170
L523: 
L524: 171
L525: 
L526: 172
L527: 
L528: 173
L529: 
L530: 174
L531: 
L532: 175
L533: 
L534: 176
L535: 
L536: 177
L537: 
L538: 178
L539: 
L540: 179
L541: 
L542: 180
L543: 
L544: 181
L545: 
L546: 182
L547: 
L548: 183
L549: 
L550: 184
L551: 
L552: 185
L553: 
L554: 186
L555: 
L556: 187
L557: 
L558: 188
L559: 
L560: 189
L561: 
L562: 190
L563: 
L564: 191
L565: 
L566: 192
L567: 193
L568: 
L569: 194
L570: 
L571: 195
L572: 
L573: 196
L574: 
L575: 197
L576: 
L577: 198
L578: 
L579: 199
L580: 
L581: 200
L582: 
L583: 201
L584: 
L585: 202
L586: 
L587: 203
L588: 
L589: 204
L590: 
L591: 205
L592: 
L593: 206
L594: 
L595: 207
L596: 
L597: 208
L598: 
L599: 209
L600: 
L601: 210
L602: 
L603: 211
L604: 
L605: """
L606: 
L607: This script implements a PyTorch deep learning training pipeline for an eye tracking application.
L608: 
L609: It includes a main function to pass in arguments, train and validation functions, and uses MLflow as the logging library.
L610: 
L611: The script also supports fine-grained deep learning hyperparameter tuning using argparse and JSON configuration files.
L612: 
L613: All hyperparameters are logged with MLflow.
L614: Contributors: Zuowen Wang, Chang Gao
L615: 
L616: Affiliation: Insitute of Neuroinformatics, University of Zurich and ETH Zurich, TU Delft
L617: 
L618: Email: wangzu@ethz.ch, gaochangw@outlook.com
L619: 
L620: """
L621: 
L622: import argparse, json, os, mlflow
L623: 
L624: import torch
L625: 
L626: import torch.nn as nn
L627: 
L628: import torch.optim as optim
L629: 
L630: from torch.utils.data import DataLoader
L631: 
L632: from model.BaselineEyeTrackingModel import CNN_GRU
L633: 
L634: from utils.training_utils import train_epoch, validate_epoch, top_k_checkpoints
L635: 
L636: from utils.metrics import weighted_MSELoss
L637: from dataset import ThreeETplus_Eyetracking, ScaleLabel, NormalizeLabel, \
L638: 
L639: TemporalSubsample, NormalizeLabel, SliceLongEventsToShort, \
L640: 
L641: EventSlicesToVoxelGrid, SliceByTimeEventsTargets
L642: 
L643: import tonic.transforms as transforms
L644: 
L645: from tonic import SlicedDataset, DiskCachedDataset
L646: 
L647: from tqdm import tqdm
L648: 
