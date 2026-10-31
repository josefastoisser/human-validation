# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Description](#s002)
- [S003: Evaluation](#s003)
- [S004: rules](#s004)
- [S005: abstract](#s005)
- [S006: foundational-rules](#s006)
- [S007: you-are-bot:thread:572987:opening](#s007)
- [S008: you-are-bot:thread:572987:3177410](#s008)
- [S009: you-are-bot:thread:572987:3183917](#s009)
- [S010: you-are-bot:thread:572987:3184230](#s010)
- [S011: you-are-bot:thread:572987:3182651](#s011)
- [S012: you-are-bot:thread:572987:3183919](#s012)
- [S013: you-are-bot:thread:693947:opening](#s013)
- [S014: you-are-bot:thread:693947:3447399](#s014)
- [S015: you-are-bot:thread:693947:3447398](#s015)

<a id="s001"></a>
## S001

- **source_id:** you-are-bot:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/you-are-bot/overview/data-description
- **retrieved_at:** 2026-10-17T06:31:12.908308+00:00
- **Archive locator:** `/task_documents/0/text`

В этом разделе описаны все доступные файлы и структура данных. Соревнование включает в себя 5 файлов, часть из которых содержит тренировочные данные и метки (train.json, ytrain.csv), а часть – тестовые (test.json, ytest.csv). Также приложен пример сабмита (sample_submission.csv). Ниже приведено краткое описание каждого файла.

**1. train.json**
   - Формат: JSON
   - Содержит тренировочные диалоги. Ключи верхнего уровня – это идентификаторы диалогов (dialog_id). Для каждого диалога хранится массив реплик (message), каждая из которых содержит:
     - text — текст сообщения
     - message — номер реплики
     - participant_index — индекс участника диалога (0 или 1)
   - Используется совместно с ytrain.csv, где указано, кто является ботом.

**2. ytrain.csv**
   - Формат: CSV
   - Содержит метки (is_bot) для каждого участника диалога в train.json.
   - Столбцы:
     - dialog_id — идентификатор диалога (совпадает с ключом в train.json)
     - participant_index — индекс участника (0 или 1)
     - is_bot — метка (0 = человек, 1 = бот)

**3. test.json**
   - Формат: JSON
   - Аналогична структуре train.json, но содержит тестовые диалоги без меток. Ключи верхнего уровня – это dialog_id. Каждому диалогу соответствует список реплик с text, message и participant_index.
   - Используется совместно с ytest.csv.

**4. ytest.csv**
   - Формат: CSV
   - Содержит идентификаторы и participant_index для тестовых записей, чтобы связать каждую запись test.json с полем ID, по которому нужно сделать предсказание.
   - Столбцы:
     - dialog_id — идентификатор диалога
     - participant_index — индекс участника
     - ID — комбинированное поле (dialog_id_participantIndex), которое используется в сабмите

**5. sample_submission.csv**
   - Формат: CSV
   - Пример правильного оформления файла сабмита, содержит столбцы:
     - ID — идентификатор в формате dialog_id_participantIndex
     - is_bot — пример вероятности (или скалярной оценки), что участник является ботом
   - Для итогового сабмита вам нужно заполнить колонку is_bot своими предсказаниями.

Обратите внимание, что для формата предсказаний в соревновании требуется вывести вероятность, а не бинарную метку (подробности – в разделе Evaluation).


<a id="s002"></a>
## S002

- **source_id:** you-are-bot:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/you-are-bot/overview/Description
- **retrieved_at:** 2026-10-17T06:31:12.908308+00:00
- **Archive locator:** `/task_documents/1/text`

	•	**Контекст.** Многие современные интернет-сервисы уже содержат чат-ботов. Во время короткого общения иногда трудно понять, с кем именно ты общаешься. Возможность автоматически это определять становится всё более важной — как для бизнеса, так и для обычных пользователей.
	•	**Сложность задачи.** Боты могут использовать разные языковые модели (например, OpenAI GPT, Deep Seek и.т.п.) и «притворяться» реальными людьми. Участникам соревнования предстоит встретиться с широким спектром стилей ответов — от элементарных эхо-ботов до продвинутых нейронных сетей.
	•	**Перспективы.** Разработка подобной модели классификации может помочь в будущем создавать более безопасные и прозрачные онлайн-пространства. 


<a id="s003"></a>
## S003

- **source_id:** you-are-bot:page:2:Evaluation
- **page_name:** Evaluation
- **url:** https://www.kaggle.com/competitions/you-are-bot/overview/Evaluation
- **retrieved_at:** 2026-10-17T06:31:12.908308+00:00
- **Archive locator:** `/task_documents/2/text`

Сабмишны оцениваются по функции потерь LogLoss — чем ниже значение, тем выше позиция в лидерборде.

Чтобы сформировать файл с предсказаниями, необходимо для каждого объекта из тестовой выборки (поле ID) подать вероятность (от 0 до 1), что данный участник диалога является ботом.

**Формат файла:** должен содержать заголовок и две колонки:  

    ID,is_bot
    36b3aae8-cbb8-493e-84c7-d28ed4c6fd2f_0,0.35798816568047337
    5b8dcc50-ce27-4ea9-8746-f3f7bf1ae6b9_1,0.6212305489275173
    83792cb8-6a3a-4c19-9086-64d747e133a3_0,0.1283000012570234
    …

Убедитесь, что у вас есть заголовок, и все строки соответствуют записям в тестовом наборе.


<a id="s004"></a>
## S004

- **source_id:** you-are-bot:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/you-are-bot/overview/rules
- **retrieved_at:** 2026-10-17T06:31:12.908308+00:00
- **Archive locator:** `/task_documents/3/text`

Правила классические:
- Don't cheat!
- Apply yourself!
- Have fun!


<a id="s005"></a>
## S005

- **source_id:** you-are-bot:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/you-are-bot/overview/abstract
- **retrieved_at:** 2026-10-17T06:31:12.908308+00:00
- **Archive locator:** `/task_documents/4/text`

**You Are Bot!**
Сможете ли вы отличить настоящего человека от чат-бота в диалоге?

На сайте [youare.bot](https://youare.bot) можно проверить свою «проницательность»: каждый пользователь общается с анонимным собеседником в течение нескольких минут и пытается определить, человек это или бот. В конце диалога пользователи делают пытаются угадать, с кем они говорили.

В этом соревновании мы публикуем датасет, собранный на платформе youare.bot, и предлагаем вам задачу бинарной классификации: определить, является ли автор сообщения человеком или ботом по текстам их диалога. В сервисе youare.bot создатели ботов стараются «замаскировать» свои творения под человека. Теперь настал ваш черёд разработать ML-модель, способную вычислить роботов!

**Описание задачи**

Вам даются примеры диалогов между двумя собеседниками и метка «bot»/«human» (1 или 0). Задача — построить модель, которая по тексту диалога с наибольшей точностью будет определять, является ли участник диалога ботом или нет.

Перезапуск этого соревнования здесь: https://kaggle.com/competitions/you-are-bot-2


<a id="s006"></a>
## S006

- **source_id:** you-are-bot:page:5:foundational-rules
- **page_name:** foundational-rules
- **url:** https://www.kaggle.com/competitions/you-are-bot/overview/foundational-rules
- **retrieved_at:** 2026-10-17T06:31:12.908308+00:00
- **Archive locator:** `/task_documents/5/text`

The following Kaggle Competition Foundational Rules (“ Foundational Rules ”) apply to every competition regardless of whether the Sponsor creates competition-specific rules. Any competition-specific rules provided by the Sponsor are in addition to these rules, and in the case of any conflict or inconsistency, these Foundational Rules control and nullify contrary competition-specific rules.
###GENERAL COMPETITION RULES - BINDING AGREEMENT
####1. ELIGIBILITY
a. To be eligible to enter the Competition, you must be:

1. a registered account holder at Kaggle.com; 

2. the older of 18 years old or the age of majority in your jurisdiction of residence (unless otherwise agreed to by Competition Sponsor and appropriate parental/guardian consents have been obtained by Competition Sponsor); 

3. not a resident of Crimea, so-called Donetsk People's Republic (DNR) or Luhansk People's Republic (LNR), Cuba, Iran, Syria, or North Korea; and

4. not a person or representative of an entity under U.S. export controls or sanctions (see: [https://www.treasury.gov/resourcecenter/sanctions/Programs/Pages/Programs.aspx][1]).

b. Competitions are open to residents of the United States and worldwide, except that if you are a resident of Crimea, so-called Donetsk People's Republic (DNR) or Luhansk People's Republic (LNR), Cuba, Iran, Syria, North Korea, or are subject to U.S. export controls or sanctions, you may not enter the Competition. Other local rules and regulations may apply to you, so please check your local laws to ensure that you are eligible to participate in skills-based competitions. The Competition Host reserves the right to forego or award alternative Prizes where needed to comply with local laws. If a winner is located in a country where prizes cannot be awarded, then they are not eligible to receive a prize.

c. If you are entering as a representative of a company, educational institution or other legal entity, or on behalf of your employer, these rules are binding on you, individually, and the entity you represent or where you are an employee. If you are acting within the scope of your employment, or as an agent of another party, you warrant that such party or your employer has full knowledge of your actions and has consented thereto, including your potential receipt of a Prize. You further warrant that your actions do not violate your employer's or entity's policies and procedures.

   

d. The Competition Sponsor reserves the right to verify eligibility and to adjudicate on any dispute at any time. If you provide any false information relating to the Competition concerning your identity, residency, mailing address, telephone number, email address, ownership of right, or information required for entering the Competition, you may be immediately disqualified from the Competition.

####2. SPONSOR AND HOSTING PLATFORM

a. The Competition is sponsored by Competition Sponsor named above. The Competition is hosted on behalf of Competition Sponsor by Kaggle Inc. ("Kaggle"). Kaggle is an independent contractor of Competition Sponsor, and is not a party to this or any agreement between you and Competition Sponsor. You understand that Kaggle has no responsibility with respect to selecting the potential Competition winner(s) or awarding any Prizes. Kaggle will perform certain administrative functions relating to hosting the Competition, and you agree to abide by the provisions relating to Kaggle under these Rules. As a Kaggle.com account holder and user of the Kaggle competition platform, remember you have accepted and are subject to the Kaggle Terms of Service at [www.kaggle.com/terms][2] in addition to these Rules.

####3. COMPETITION PERIOD
a. For the purposes of Prizes, the Competition will run from the Start Date and time to the Final Submission Deadline (such duration the “Competition Period”). The Competition Timeline is subject to change, and Competition Sponsor may introduce additional hurdle deadlines during the Competition Period. Any updated or additional deadlines will be publicized on the Competition Website. It is your responsibility to check the Competition Website regularly to stay informed of any deadline changes. YOU ARE RESPONSIBLE FOR DETERMINING THE CORRESPONDING TIME ZONE IN YOUR LOCATION.

####4. COMPETITION ENTRY
a. NO PURCHASE NECESSARY TO ENTER OR WIN. To enter the Competition, you must register on the Competition Website prior to the Entry Deadline, and follow the instructions for developing and entering your Submission through the Competition Website. Your Submissions must be made in the manner and format, and in compliance with all other requirements, stated on the Competition Website (the "Requirements"). Submissions must be received before any Submission deadlines stated on the Competition Website. Submissions not received by the stated deadlines will not be eligible to receive a Prize.

b. Submissions may not use or incorporate information from hand labeling or human prediction of the validation dataset or test data records.

c. If the Competition is a multi-stage competition with temporally separate training and/or test data, one or more valid Submissions may be required during each Competition stage in the manner described on the Competition Website in order for the Submissions to be Prize eligible.

d. Submissions are void if they are in whole or part illegible, incomplete, damaged, altered, counterfeit, obtained through fraud, or late. Competition Sponsor reserves the right to disqualify any entrant who does not follow these Rules, including making a Submission that does not meet the Requirements. 

####5. INDIVIDUALS AND TEAMS
a. Individual Account. You may make Submissions only under one, unique Kaggle.com account. You will be disqualified if you make Submissions through more than one Kaggle account, or attempt to falsify an account to act as your proxy. You may submit up to the maximum number of Submissions per day as specified on the Competition Website. 

b. Teams. If permitted under the Competition Website guidelines, multiple individuals may collaborate as a Team; however, you may join or form only one Team. Each Team member must be a single individual with a separate Kaggle account. You must register individually for the Competition before joining a Team. You must confirm your Team membership to make it official by responding to the Team notification message sent to your Kaggle account. Team membership may not exceed the Maximum Team Size stated on the Competition Website.

c. Team Merger. Teams may request to merge via the Competition Website. Team mergers may be allowed provided that: (i) the combined Team does not exceed the Maximum Team Size; (ii) the number of Submissions made by the merging Teams does not exceed the number of Submissions permissible for one Team at the date of the merger request; (iii) the merger is completed before the earlier of: any merger deadline or the Competition deadline; and (iv) the proposed combined Team otherwise meets all the requirements of these Rules. 

d. Private Sharing. No private sharing outside of Teams. Privately sharing code or data outside of Teams is not permitted. It's okay to share code if made available to all Participants on the forums.

####6. SUBMISSION CODE REQUIREMENTS
a. Private Code Sharing. Unless otherwise specifically permitted under the Competition Website or Competition Specific Rules above, during the Competition Period, you are not allowed to privately share source or executable code developed in connection with or based upon the Competition Data or other source or executable code relevant to the Competition (“Competition Code”). This prohibition includes sharing Competition Code between separate Teams, unless a Team merger occurs. Any such sharing of Competition Code is a breach of these Competition Rules and may result in disqualification.

b. Public Code Sharing. You are permitted to publicly share Competition Code, provided that such public sharing does not violate the intellectual property rights of any third party. If you do choose to share Competition Code or other such code, you are required to share it on Kaggle.com on the discussion forum or notebooks associated specifically with the Competition for the benefit of all competitors. By so sharing, you are deemed to have licensed the shared code under an Open Source Initiative-approved license (see [www.opensource.org][3]) that in no event limits commercial use of such Competition Code or model containing or depending on such Competition Code.

c. Use of Open Source. Unless otherwise stated in the Specific Competition Rules above, if open source code is used in the model to generate the Submission, then you must only use open source code licensed under an Open Source Initiative-approved license (see [www.opensource.org][4]) that in no event limits commercial use of such code or model containing or depending on such code.

####7. DETERMINING WINNERS
a. Each Submission will be scored and ranked by the evaluation metric stated on the Competition Website. During the Competition Period, the current ranking will be visible on the Competition Website's Public Leaderboard. The potential winner(s) are determined solely by the leaderboard ranking on the Private Leaderboard, subject to compliance with these Rules. The Public Leaderboard will be based on the public test set and the Private Leaderboard will be based on the private test set.

b. In the event of a tie, the Submission that was entered first to the Competition will be the winner. In the event a potential winner is disqualified for any reason, the Submission that received the next highest score rank will be chosen as the potential winner.

####8. NOTIFICATION OF WINNERS & DISQUALIFICATION
a. The potential winner(s) will be notified by email.

 
b. If a potential winner (i) does not respond to the notification attempt within one (1) week from the first notification attempt or (ii) notifies Kaggle within one week after the Final Submission Deadline that the potential winner does not want to be nominated as a winner or does not want to receive a Prize, then, in each case (i) and (ii) such potential winner will not receive any Prize, and an alternate potential winner will be selected from among all eligible entries received based on the Competition’s judging criteria.

c. In case (i) and (ii) above Kaggle may disqualify the Participant.  However, in case (ii) above, if requested by Kaggle, such potential winner may provide code and documentation to verify the Participant’s compliance with these Rules. If the potential winner provides code and documentation to the satisfaction of Kaggle, the Participant will not be disqualified pursuant to this paragraph.

d. Competition Sponsor reserves the right to disqualify any Participant from the Competition if the Competition Sponsor reasonably believes that the Participant has attempted to undermine the legitimate operation of the Competition by cheating, deception, or other unfair playing practices or abuses, threatens or harasses any other Participants, Competition Sponsor or Kaggle.

e. A disqualified Participant may be removed from the Competition leaderboard, at Kaggle's sole discretion. If a Participant is removed from the Competition Leaderboard, additional winning features associated with the Kaggle competition platform, for example Kaggle points or medals, may also not be awarded.

f. The final leaderboard list will be publicly displayed at Kaggle.com. Determinations of Competition Sponsor are final and binding.

####9. PRIZES
a. Prize(s) are as described on the Competition Website and are only available for winning during the time period described on the Competition Website. The odds of winning any Prize depends on the number of eligible Submissions received during the Competition Period and the skill of the Participants. 

b. All Prizes are subject to Competition Sponsor's review and verification of the Participant’s eligibility and compliance with these Rules, and the compliance of the winning Submissions with the Submissions Requirements. In the event that the Submission demonstrates non-compliance with these Competition Rules, Competition Sponsor may at its discretion take either of the following actions: (i) disqualify the Submission(s); or (ii) require the potential winner to remediate within one week after notice all issues identified in the Submission(s) (including, without limitation, the resolution of license conflicts, the fulfillment of all obligations required by software licenses, and the removal of any software that violates the software restrictions).

c. A potential winner may decline to be nominated as a Competition winner in accordance with Section 3.8.

d. Potential winners must return all required Prize acceptance documents within two (2) weeks following notification of such required documents, or such potential winner will be deemed to have forfeited the prize and another potential winner will be selected. Prize(s) will be awarded within approximately thirty (30) days after receipt by Competition Sponsor or Kaggle of the required Prize acceptance documents. Transfer or assignment of a Prize is not allowed. 

e. You are not eligible to receive any Prize if you do not meet the Eligibility requirements in Section 2.7 and Section 3.1 above.

f. If a Team wins a monetary Prize, the Prize money will be allocated in even shares between the eligible Team members, unless the Team unanimously opts for a different Prize split and notifies Kaggle before Prizes are issued.

####10. TAXES
a. ALL TAXES IMPOSED ON PRIZES ARE THE SOLE RESPONSIBILITY OF THE WINNERS. Payments to potential winners are subject to the express requirement that they submit all documentation requested by Competition Sponsor or Kaggle for compliance with applicable state, federal, local and foreign (including provincial) tax reporting and withholding requirements. Prizes will be net of any taxes that Competition Sponsor is required by law to withhold. If a potential winner fails to provide any required documentation or comply with applicable laws, the Prize may be forfeited and Competition Sponsor may select an alternative potential winner. Any winners who are U.S. residents will receive an IRS Form-1099 in the amount of their Prize.

####11. GENERAL CONDITIONS
a. All federal, state, provincial and local laws and regulations apply.

####12. PUBLICITY
a. You agree that Competition Sponsor, Kaggle and its affiliates may use your name and likeness for advertising and promotional purposes without additional compensation, unless prohibited by law.

####13. PRIVACY
a. You acknowledge and agree that Competition Sponsor and Kaggle may collect, store, share and otherwise use personally identifiable information provided by you during the Kaggle account registration process and the Competition, including but not limited to, name, mailing address, phone number, and email address (“Personal Information”). Kaggle acts as an independent controller with regard to its collection, storage, sharing, and other use of this Personal Information, and will use this Personal Information in accordance with its Privacy Policy <[www.kaggle.com/privacy][6]>, including for administering the Competition. As a Kaggle.com account holder, you have the right to request access to, review, rectification, portability or deletion of any personal data held by Kaggle about you by logging into your account and/or contacting Kaggle Support at <[www.kaggle.com/contact][7]>.

b. As part of Competition Sponsor performing this contract between you and the Competition Sponsor, Kaggle will transfer your Personal Information to Competition Sponsor, which acts as an independent controller with regard to this Personal Information. As a controller of such Personal Information, Competition Sponsor agrees to comply with all U.S. and foreign data protection obligations with regard to your Personal Information. Kaggle will transfer your Personal Information to Competition Sponsor in the country specified in the Competition Sponsor Address listed above, which may be a country outside the country of your residence. Such country may not have privacy laws and regulations similar to those of the country of your residence.

####14. WARRANTY, INDEMNITY AND RELEASE 
a. You warrant that your Submission is your own original work and, as such, you are the sole and exclusive owner and rights holder of the Submission, and you have the right to make the Submission and grant all required licenses.  You agree not to make any Submission that: (i) infringes any third party proprietary rights, intellectual property rights, industrial property rights, personal or moral rights or any other rights, including without limitation, copyright, trademark, patent, trade secret, privacy, publicity or confidentiality obligations, or defames any person; or (ii) otherwise violates any applicable U.S. or foreign state or federal law.

b. To the maximum extent permitted by law, you indemnify and agree to keep indemnified Competition Entities at all times from and against any liability, claims, demands, losses, damages, costs and expenses resulting from any of your acts, defaults or omissions and/or a breach of any warranty set forth herein. To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless the Competition Entities from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from: (a) your Submission or other material uploaded or otherwise provided by you that infringes any third party proprietary rights, intellectual property rights, industrial property rights, personal or moral rights or any other rights, including without limitation, copyright, trademark, patent, trade secret, privacy, publicity or confidentiality obligations, or defames any person; (b) any misrepresentation made by you in connection with the Competition; (c) any non-compliance by you with these Rules or any applicable U.S. or foreign state or federal law; (d) claims brought by persons or entities other than the parties to these Rules arising from or related to your involvement with the Competition; and (e) your acceptance, possession, misuse or use of any Prize, or your participation in the Competition and any Competition-related activity.

c. You hereby release Competition Entities from any liability associated with: (a) any malfunction or other problem with the Competition Website; (b) any error in the collection, processing, or retention of any Submission; or (c) any typographical or other error in the printing, offering or announcement of any Prize or winners.

####15. INTERNET
a. Competition Entities are not responsible for any malfunction of the Competition Website or any late, lost, damaged, misdirected, incomplete, illegible, undeliverable, or destroyed Submissions or entry materials due to system errors, failed, incomplete or garbled computer or other telecommunication transmission malfunctions, hardware or software failures of any kind, lost or unavailable network connections, typographical or system/human errors and failures, technical malfunction(s) of any telephone network or lines, cable connections, satellite transmissions, servers or providers, or computer equipment, traffic congestion on the Internet or at the Competition Website, or any combination thereof, which may limit a Participant’s ability to participate.

####16. RIGHT TO CANCEL, MODIFY OR DISQUALIFY
a. If for any reason the Competition is not capable of running as planned, including infection by computer virus, bugs, tampering, unauthorized intervention, fraud, technical failures, or any other causes which corrupt or affect the administration, security, fairness, integrity, or proper conduct of the Competition, Competition Sponsor reserves the right to cancel, terminate, modify or suspend the Competition. Competition Sponsor further reserves the right to disqualify any Participant who tampers with the submission process or any other part of the Competition or Competition Website.  Any attempt by a Participant to deliberately damage any website, including the Competition Website, or undermine the legitimate operation of the Competition is a violation of criminal and civil laws. Should such an attempt be made, Competition Sponsor and Kaggle each reserves the right to seek damages from any such Participant to the fullest extent of the applicable law.

####17. NOT AN OFFER OR CONTRACT OF EMPLOYMENT
a. Under no circumstances will the entry of a Submission, the awarding of a Prize, or anything in these Rules be construed as an offer or contract of employment with Competition Sponsor or any of the Competition Entities. You acknowledge that you have submitted your Submission voluntarily and not in confidence or in trust. You acknowledge that no confidential, fiduciary, agency, employment or other similar relationship is created between you and Competition Sponsor or any of the Competition Entities by your acceptance of these Rules or your entry of your Submission.

####18. DEFINITIONS
a. "Competition Data" are the data or datasets available from the Competition Website for the purpose of use in the Competition, including any prototype or executable code provided on the Competition Website. The Competition Data will contain private and public test sets. Which data belongs to which set will not be made available to Participants. 

b. An “Entry” is when a Participant has joined, signed up, or accepted the rules of a competition. Entry is required to make a Submission to a competition.

c. A “Final Submission” is the Submission selected by the user, or automatically selected by Kaggle in the event not selected by the user, that is/are used for final placement on the competition leaderboard.

d. A “Participant” or “Participant User” is an individual who participates in a competition by entering the competition and making a Submission.

e. The “Private Leaderboard” is a ranked display of Participants’ Submission scores against the private test set. The Private Leaderboard determines the final standing in the competition.

f. The “Public Leaderboard” is a ranked display of Participants’ Submission scores against a representative sample of the test data. This leaderboard is visible throughout the competition.

g. A “Sponsor” is responsible for hosting the competition, which includes but is not limited to providing the data for the competition, determining winners, and enforcing competition rules.

h. A “Submission” is anything provided by the Participant to the Sponsor to be evaluated for competition purposes and determine leaderboard position. A Submission may be made as a model, notebook, prediction file, or other format as determined by the Sponsor.

i. A “Team” is one or more Participants participating together in a Kaggle competition, by officially merging together as a Team within the competition platform.

  [1]: https://www.treasury.gov/resource-center/sanctions/Programs/Pages/Programs.aspx
  [2]: http://www.kaggle.com/terms
  [3]: http://www.opensource.org
  [4]: http://www.opensource.org
  [5]: https://www.kaggle.com/WinningModelDocumentationGuidelines
  [6]: http://www.kaggle.com/privacy
  [7]: http://www.kaggle.com/contact


<a id="s007"></a>
## S007

- **source_id:** you-are-bot:thread:572987:opening
- **url:** https://www.kaggle.com/competitions/you-are-bot/discussion/572987
- **thread_id:** 572987
- **comment_id:** opening
- **author_name:** Alexander Guschin
- **author_role:** unknown
- **created_at:** 2025-04-12T17:42:32.128Z
- **retrieved_at:** 2026-10-17T21:55:22.669350+00:00
- **Archive locator:** `/discussion/0/text`

Добро пожаловать в соревнование!

Всем привет! Добро пожаловать в соревнование)

Если у вас есть какие-то вопросы, задавайте их здесь, будем рады на них ответить:)


<a id="s008"></a>
## S008

- **source_id:** you-are-bot:thread:572987:3177410
- **url:** https://www.kaggle.com/competitions/you-are-bot/discussion/572987#comment-3177410
- **thread_id:** 572987
- **comment_id:** 3177410
- **author_name:** Mikhail
- **author_role:** unknown
- **created_at:** 2025-04-12T17:53:44.253Z
- **retrieved_at:** 2026-10-17T21:55:22.669350+00:00
- **Archive locator:** `/discussion/1/text`

Всем привет!

Я разработчик youare.bot - задавайте вопросы, если что-то непонятно!

По данным, по форматам, по обозначениям - всё расскажу и покажу)


<a id="s009"></a>
## S009

- **source_id:** you-are-bot:thread:572987:3183917
- **url:** https://www.kaggle.com/competitions/you-are-bot/discussion/572987#comment-3183917
- **thread_id:** 572987
- **comment_id:** 3183917
- **author_name:** Daniil Zaytsev
- **author_role:** unknown
- **created_at:** 2025-04-21T12:44:14.147Z
- **retrieved_at:** 2026-10-17T21:55:22.669350+00:00
- **Archive locator:** `/discussion/2/text`

Добрый день. Подскажите, почему в Leaderborad у более высокого места меньший скор ROC AUC?


<a id="s010"></a>
## S010

- **source_id:** you-are-bot:thread:572987:3184230
- **url:** https://www.kaggle.com/competitions/you-are-bot/discussion/572987#comment-3184230
- **thread_id:** 572987
- **comment_id:** 3184230
- **parent_comment_id:** 3183917
- **author_name:** Alexander Guschin
- **author_role:** unknown
- **created_at:** 2025-04-21T19:44:58.010Z
- **retrieved_at:** 2026-10-17T21:55:22.669350+00:00
- **Archive locator:** `/discussion/3/text`

Добрый день! На лидерборде вы видите не ROC AUC, а Logloss. Поправил это в описании задачи. Спасибо)


<a id="s011"></a>
## S011

- **source_id:** you-are-bot:thread:572987:3182651
- **url:** https://www.kaggle.com/competitions/you-are-bot/discussion/572987#comment-3182651
- **thread_id:** 572987
- **comment_id:** 3182651
- **author_name:** Pavel Grigorev
- **author_role:** unknown
- **created_at:** 2025-04-19T17:06:38.700Z
- **retrieved_at:** 2026-10-17T21:55:22.669350+00:00
- **Archive locator:** `/discussion/4/text`

Есть ли лимиты на сабмиты? количество, частота, дэдлайн?


<a id="s012"></a>
## S012

- **source_id:** you-are-bot:thread:572987:3183919
- **url:** https://www.kaggle.com/competitions/you-are-bot/discussion/572987#comment-3183919
- **thread_id:** 572987
- **comment_id:** 3183919
- **parent_comment_id:** 3182651
- **author_name:** Daniil Zaytsev
- **author_role:** unknown
- **created_at:** 2025-04-21T12:47:07.090Z
- **retrieved_at:** 2026-10-17T21:55:22.669350+00:00
- **Archive locator:** `/discussion/5/text`

При сабмите написано, что максимум 5 решений в день


<a id="s013"></a>
## S013

- **source_id:** you-are-bot:thread:693947:opening
- **url:** https://www.kaggle.com/competitions/you-are-bot/discussion/693947
- **thread_id:** 693947
- **comment_id:** opening
- **author_name:** Lobzinastya
- **author_role:** unknown
- **created_at:** 2026-04-22T19:45:48.561Z
- **retrieved_at:** 2026-10-17T21:55:25.437463+00:00
- **Archive locator:** `/discussion/6/text`

DLS Bot Detection - победное решение

Попробую описать, что в итоге сработало и принесло победу в соревновании

Изначально пыталась делать одну модель (catboost на фичах + tf-idf), но дальше всё постепенно превратилось в многоуровневый ансамбль. Решение получилось довольно "грязным" (с точки зрения сложной и маловоспроизводимой архитектуры), но давало стабильный прирост.

**Основная идея**: Не оказалось одного сильного сигнала. Лучше всего работала комбинация разного:

- структура диалога

- perplexity

- tf-idf

- отдельные модели на первых репликах

- stacking

- диалог как последовательность

Важно было не терять порядок реплик. Собирала диалог через [SEP], а для первого участника добавляла [EMPTY], чтобы первая реплика тоже учитывалась нормально. Это дало прирост (модель начала лучше понимать, кто как отвечает)

Отдельные модели на репликах: один из самых сильных сигналов - это первая реплика (и для того кто начинает диалог, и как ответ на первую реплику собеседника)
Я отдельно обучала модели на:

- первой реплике

- второй реплике

- и в целом на репликах
И потом добавляла их вероятности как признаки.

Perplexity: Считала разные варианты:

- обычная

- sliding

- contextual
и все это для GPT-2 и phi. И это тоже реально хорошо работало 

Агрегация: Так как диалоги разной длины, считала признаки по отдельным репликам (в том числе на основе эмбеддингов текста), а затем агрегировала их через статистики (mean, std, min, max, skew и т.д.). Это оказалось лучше, чем пытаться обучать последовательные модели. Также отдельно считала, насколько реплика похожа на предыдущую и на весь контекст диалога (через косинусное сходство эмбеддингов) - это тоже давало полезный сигнал.

TF-IDF: Простой TF-IDF (особенно char n-grams) дал очень заметный буст.
Пробовала более сложные вещи, а итоге tf-idf всё равно выигрывал.

Ансамбль: 
Дальше всё собиралось так:

- несколько базовых моделей (catboost, tf-idf, nb-svm, модели на репликах)

- их предсказания добавлялись как фичи

- на них обучались ещё модели (с частичным прокидыванием начальных признаков)

- потом финальная logistic regression
И в конце: усреднение нескольких лучших сабмитов.

Что не зашло:

- нейросети (lstm, трансформеры - пыталась познать многомерную геометрию переходов между эмбеддингами реплик, но неудачно скорее всего из-за маленького количества данных)

**Итог**: 
Решение получилось не очень красивым, но рабочим

- много разных сигналов

- вероятности как признаки

- постепенный stacking

P.S. Не уверена, как обычно оформляют writeups, поэтому постаралась кратко описать идеи и процесс. Финального воспроизводимого кода в одном месте нет - решение собиралось итеративно из бесконечных экспериментов и промежуточных результатов


<a id="s014"></a>
## S014

- **source_id:** you-are-bot:thread:693947:3447399
- **url:** https://www.kaggle.com/competitions/you-are-bot/discussion/693947#comment-3447399
- **thread_id:** 693947
- **comment_id:** 3447399
- **author_name:** Alexander Guschin
- **author_role:** unknown
- **created_at:** 2026-04-23T04:27:29.253Z
- **retrieved_at:** 2026-10-17T21:55:25.437463+00:00
- **Archive locator:** `/discussion/7/text`

Мы перезапустили соревнование, возможно ты захочешь поделиться ссылкой на это решение в новом запуске (или засабмитить свое решение туда:) [https://kaggle.com/competitions/you-are-bot-2](https://kaggle.com/competitions/you-are-bot-2)


<a id="s015"></a>
## S015

- **source_id:** you-are-bot:thread:693947:3447398
- **url:** https://www.kaggle.com/competitions/you-are-bot/discussion/693947#comment-3447398
- **thread_id:** 693947
- **comment_id:** 3447398
- **author_name:** Alexander Guschin
- **author_role:** unknown
- **created_at:** 2026-04-23T04:25:39.093Z
- **retrieved_at:** 2026-10-17T21:55:25.437463+00:00
- **Archive locator:** `/discussion/8/text`

Очень круто! Спасибо)

