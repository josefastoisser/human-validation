# Original source context — Stage B only

Open after saving Stage A. These are original task-page and discussion texts extracted from saved archives. Their inclusion does not certify historical ambiguity, author authority, or the correctness of either local rule. No proposed validity judgments or benchmark model results are included.

Dates describe the saved record; a retrieval date is not a publication date. Missing dates/roles remain unknown. A current page does not establish what a participant saw earlier. The available archive need not be historically complete. Exact original text and archive locators are in [sources.json](sources.json).

## Source index

- [S001: data-description](#s001)
- [S002: Description](#s002)
- [S003: Evaluation Criteria](#s003)
- [S004: rules](#s004)
- [S005: abstract](#s005)
- [S006: cvpr-metafood-3d-food-reconstruction-challenge:thread:509899:opening](#s006)
- [S007: cvpr-metafood-3d-food-reconstruction-challenge:thread:509899:2861099](#s007)

<a id="s001"></a>
## S001

- **source_id:** cvpr-metafood-3d-food-reconstruction-challenge:page:0:data-description
- **page_name:** data-description
- **url:** https://www.kaggle.com/competitions/cvpr-metafood-3d-food-reconstruction-challenge/overview/data-description
- **retrieved_at:** 2026-10-20T16:00:21.421118+00:00
- **Archive locator:** `/task_documents/0/text`

Challenge update (05/25/2024):
Thank you to everyone who participated in the Physically Informed 3D Food Reconstruction competition. We are now entering Phase 2 of the competition, where we will select the top 5 teams to submit their 3D object models. These models will be evaluated based on chamfer distance. The final score will be calculated by averaging the rankings from Phase 1 and Phase 2. In the event of a tie, the Phase 1 score will determine the final ranking.

For the Phase 2 evaluation (for the top 5 teams), we were unable to find a fair and automatic way to align the pose between the submissions and the ground truth objects. Therefore, we are updating the evaluation procedure, and the winner announcement will be delayed to June 7th. The revised steps are as follows:

1. Upload Models: Upload all 20 of your 3D models (.obj files named with the object ID) to a location where we can download them.
2. Send Link: Send us the link to your models along with your team ID (or other ways to identify yourself) by May 27th, 11:59 PM AOE. Email: metafood.cvpr@gmail.com. If you encounter any issues, please post on the Kaggle discussion forum.
3. Model Verification: We will check your models against your final Phase 1 submission to ensure they are the same models used in Phase 1. We will also visually inspect the models to ensure no team is violating the rules by submitting primitive objects such as spheres.
4. Ground Truth Models: We will upload our ground truth 3D models, along with the script used to compute the final chamfer distance, on Kaggle by May 28th, 11:59 PM AOE.
5. Align Models: Align the models yourself and prepare a transform matrix for each object you submitted. Your final chamfer distance score will be computed using your submitted models and transform matrices.
6. Submit Transform Matrices: Send us your transform matrices by June 4th, 11:59 PM AOE.
We will announce the winner on June 7th.

Thank you for your understanding and cooperation.

DATASET UPDATE (04/23/2024): We added a script to extract depth information from the images. You can find the script in convert_depth folder. 
DATASET UPDATE (04/18/2024): Please use the data in the "MTF_Challenge-20240418T205428Z-001" directory. We fixed an issue where the masks for object 12 are incorrect. Note that you can still access the old data in the directory "MTF_Challenge".

The challenge features 20 selected food items, each meticulously scanned with a 3D scanner while corresponding videos were captured. These items are accompanied by a checkerboard and pattern mat during video capture, serving as physical references for scaling the output 3D models to ensure size accuracy—one of the key evaluation metrics. The difficulty level of the challenge varies with the number of 2D images available for reconstruction: simple levels are represented by approximately 200 images sampled from video, medium levels by about 30 images, and hard levels by a single monocular top-view image. Detailed information on these food items is provided below:

<!DOCTYPE html>

    
    
    Data stats
    
        table {
            border: 2px solid black;
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    

    
        
            Object Index
            Food Item
            Difficulty Level
            Number of Frames
        

    
    
        
            1
            Strawberry
            simple
            199
        

        
            2
            Cinnamon bun
            simple
            200
        

        
            3
            Pork rib
            simple
            200
        

        
            4
            Corn
            simple
            200
        

        
            5
            French toast
            simple
            200
        

        
            6
            Sandwich
            simple
            200
        

        
            7
            Burger
            simple
            200
        

        
            8
            Cake
            simple
            200
        

        
            9
            Blueberry muffin
            medium
            30
        

        
            10
            Banana
            medium
            30
        

        
            11
            Salmon
            medium
            30
        

        
            12
            Steak
            medium
            30
        

        
            13
            Burrito
            medium
            30
        

        
            14
            Hotdog
            medium
            30
        

        
            15
            Chicken nugget
            medium
            30
        

        
            16
            Everything bagel
            hard
            1
        

        
            17
            Croissant
            hard
            1
        

        
            18
            Shrimp
            hard
            1
        

        
            19
            Waffle
            hard
            1
        

        
            20
            Pizza
            hard
            1
        

    

Sample challenge data for “everything bagel”.
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F19611415%2Fb9fa4bb29d5cf4b50898ae5e968b2c8c%2FPicture1.png?generation=1711251426407329&alt=media)

    MTF_Challenge Dataset Structure

    
        
- **object index (1 - 20)**
            
                
- **Depth:** depth image for each frame

                
- **Mask:** segmentation mask for each frame

                
- **Original:** sampled original frames

            

        

        
- **source-files**
            
                
- **checkerboard.pdf**

                
- **mat.pdf**

                
- **data_meta.xls**

                
- **eval**
                
                    
- **challenge_volume_calculation.py** (evaluation script)

                    
- **environment.yml** (dependent libraries)

                    
- **volume_calculation_instructions.docx** (evaluation instruction)

                    
- **sample_solution.csv** (example submission file)


<a id="s002"></a>
## S002

- **source_id:** cvpr-metafood-3d-food-reconstruction-challenge:page:1:Description
- **page_name:** Description
- **url:** https://www.kaggle.com/competitions/cvpr-metafood-3d-food-reconstruction-challenge/overview/Description
- **retrieved_at:** 2026-10-20T16:00:21.421118+00:00
- **Archive locator:** `/task_documents/1/text`

Today, computer vision algorithms show near-perfect performance, better than human when there are clear, well curated and enough amount of data. However, there remains a substantial gap when it comes to applying state-of-the-art computer vision algorithms to food data, particularly when dealing with food in its natural, uncontrolled environment, often referred to as “data in the wild.” This gap stems from the inherent challenges in noisy, watermarked, and low-quality food data readily available on the internet. The MetaFood Workshop (MTF) invites the CVPR community to engage with the food domain-related challenges. These challenges provide not only a demanding, real testing environment for the development of robust computer vision algorithms, but also an exciting opportunity to develop new algorithms in the fields of food data analysis and food digitization.

The aim of this challenge is to highlight the importance of accurate 3D food reconstruction through a monocular camera, especially from a single image. This precise 3D modeling serves crucial purposes in food computing, such as keeping dietary records, necessitating an accurate representation of food portion sizes.


<a id="s003"></a>
## S003

- **source_id:** cvpr-metafood-3d-food-reconstruction-challenge:page:2:Evaluation Criteria
- **page_name:** Evaluation Criteria
- **url:** https://www.kaggle.com/competitions/cvpr-metafood-3d-food-reconstruction-challenge/overview/Evaluation Criteria
- **retrieved_at:** 2026-10-20T16:00:21.421118+00:00
- **Archive locator:** `/task_documents/2/text`

Challenge update (05/25/2024):
Thank you to everyone who participated in the Physically Informed 3D Food Reconstruction competition. We are now entering Phase 2 of the competition, where we will select the top 5 teams to submit their 3D object models. These models will be evaluated based on chamfer distance. The final score will be calculated by averaging the rankings from Phase 1 and Phase 2. In the event of a tie, the Phase 1 score will determine the final ranking.

For the Phase 2 evaluation (for the top 5 teams), we were unable to find a fair and automatic way to align the pose between the submissions and the ground truth objects. Therefore, we are updating the evaluation procedure, and the winner announcement will be delayed to June 7th. The revised steps are as follows:

1. Upload Models: Upload all 20 of your 3D models (.obj files named with the object ID) to a location where we can download them.
2. Send Link: Send us the link to your models along with your team ID (or other ways to identify yourself) by May 27th, 11:59 PM AOE. Email: metafood.cvpr@gmail.com. If you encounter any issues, please post on the Kaggle discussion forum.
3. Model Verification: We will check your models against your final Phase 1 submission to ensure they are the same models used in Phase 1. We will also visually inspect the models to ensure no team is violating the rules by submitting primitive objects such as spheres.
4. Ground Truth Models: We will upload our ground truth 3D models, along with the script used to compute the final chamfer distance, on Kaggle by May 28th, 11:59 PM AOE.
5. Align Models: Align the models yourself and prepare a transform matrix for each object you submitted. Your final chamfer distance score will be computed using your submitted models and transform matrices.
6. Submit Transform Matrices: Send us your transform matrices by June 4th, 11:59 PM AOE.
We will announce the winner on June 7th.

Thank you for your understanding and cooperation.

==============================================
Evaluation will consist of a two-phase process centered on the precision of the reconstructed 3D models in terms of their shape (3D structure) and portion size (volume). Results will be compared to the models of the same food items that are captured by a 3D scanner. 
In Phase-I, the Mean Absolute Percentage Error (MAPE) metric will be employed to assess the accuracy of the model's portion size. Only the volume accuracy of the models will be evaluated during this stage.
In Phase-II, the top-ranking teams from the phase-I will be asked to submit the complete 3D mesh files for each food item to validate their submission results of Phase-I. Then, the Chamfer distance metric will be used to evaluate the shape accuracy of these models.
The final winner will be determined by combining the scores from both phases for all 20 objects.  


## Submission File
For each id in the test set, you must reconstruct a 3D model from the provided images and report the volume of the model. The file should contain a header and have the following format:

    id,predicted
    2,0
    5,0
    6,0
    etc.


<a id="s004"></a>
## S004

- **source_id:** cvpr-metafood-3d-food-reconstruction-challenge:page:3:rules
- **page_name:** rules
- **url:** https://www.kaggle.com/competitions/cvpr-metafood-3d-food-reconstruction-challenge/overview/rules
- **retrieved_at:** 2026-10-20T16:00:21.421118+00:00
- **Archive locator:** `/task_documents/3/text`

Participants are required to submit 20 .obj mesh files corresponding to the 20 selected food items. These submissions will undergo evaluation based on the reconstruction's shape and size accuracy. It is essential for participants to review the following rules:

•	Submissions must adhere to the provided instructions. Submissions will be disqualified if they contain inappropriate content or fail to meet the submission rules.

•	Each registered participant/group can only submit the result once per day.

•	The contest is open to everyone. However, those directly involved in organizing and supporting the contest cannot enter.

•	Participants are allowed to use publicly available data and models, but they must properly attribute the source by including references in their submitted code.

•	During the final phase, the organizers will closely examine the code and 3D models submitted by the top-performing teams. Disqualification will occur for teams that do not present substantial original work, use similar code to others, or are caught cheating. Additionally, teams will be disqualified if their submitted 3D models do not accurately represent the object class’s shape. For instance, a team will face disqualification for submitting a sphere model for an object classified as a strawberry, whereas a submission featuring a model resembling a hemisphere with cone for the strawberry class will remain eligible.

•	Contestants are responsible for ensuring their submissions, including all files, data, and code, are legal and comply with regulations. The organizers are not liable for any legal issues that arise from the participants' submissions.

•	If contestants publish papers related to their competition results, they must credit the competition.

•	Contestants may use data and models available to the public, but must give credit by citing the sources in their code submissions.

•	The challenge data is not public yet, is not allowed to use for other purposes. 

Winner and Prize: The top-3 teams will be selected as winner. The winner will be invited for oral presentation at workshop and also write the technical report about the challenge. Refer to the workshop website for prize details: https://sites.google.com/view/cvpr-metafood-2024 

External sources: 
•	Participants are allowed to utilize external 3D object datasets for training purposes, such as OmniObject3D[1], NutritionVerse-3D[2], etc. The use of pre-trained models or any form of external data must be clearly disclosed in the submission.
•	Baseline 3D reconstruction methods include: 
        o	Medium/Simple: Use COLMAP for automatic reconstruction with the checkerboard available and apply Meshlab for cleaning and simplification to create a sparse 3D model, save it as an .obj file for the challenge submission.
        o	Hard: Apply existing methods such as One-2-3-4-5[3] to create multiple views from a single image, use them for 3D reconstruction, calibrate scale using a checkerboard pattern, and adjust the 3D model to real-world dimensions for accurate scene representation.


[1] Wu, Tong, et al. "Omniobject3d: Large-vocabulary 3d object dataset for realistic perception, reconstruction and generation." CVPR 2023.
[2] Tai, Chi-en Amy, et al. "Nutritionverse-3d: A 3d food model dataset for nutritional intake estimation." arXiv preprint arXiv:2304.05619, 2023
[3] Liu, Minghua, et al. "One-2-3-45: Any single image to 3d mesh in 45 seconds without per-shape optimization." Neurips, 2023.



<a id="s005"></a>
## S005

- **source_id:** cvpr-metafood-3d-food-reconstruction-challenge:page:4:abstract
- **page_name:** abstract
- **url:** https://www.kaggle.com/competitions/cvpr-metafood-3d-food-reconstruction-challenge/overview/abstract
- **retrieved_at:** 2026-10-20T16:00:21.421118+00:00
- **Archive locator:** `/task_documents/4/text`

3D Food Reconstruction is an innovative venture into the intersection of computer vision and culinary arts, with the goal of reconstructing three-dimensional models of food items from two-dimensional images. This challenge is designed to push the boundaries of 3D reconstruction technology by applying it to a dynamic and uncontrolled setting, such as capturing food images during eating occasions. Participants will tackle the challenge of creating precise and robust 3D models from single or multiple 2D views, using a visible physical reference (checkerboard) with the known size. The checkerboard serves as a reference object to ensure that the reconstructed 3D models have the same size as the real food items, which is crucial for accurate portion estimation. The objective is to reconstruct 3D models for 20 selected food items, provided at varying levels of difficulty: simple, medium, and hard. By reconstructing 3D models with the correct size, this technology can play a vital role in tracking nutritional intake and helping individuals maintain a healthy diet. This endeavor not only aims to enhance sharing food experiences in three dimensions but also has significant potential applications in the fields of nutrition and health monitoring. 


<a id="s006"></a>
## S006

- **source_id:** cvpr-metafood-3d-food-reconstruction-challenge:thread:509899:opening
- **url:** https://www.kaggle.com/competitions/cvpr-metafood-3d-food-reconstruction-challenge/discussion/509899
- **thread_id:** 509899
- **comment_id:** opening
- **author_name:** Andreea Dogaru
- **author_role:** unknown
- **created_at:** 2024-06-04T10:58:48.960Z
- **retrieved_at:** 2026-10-20T16:01:28.563614+00:00
- **Archive locator:** `/discussion/0/text`

Chamfer distance computation issue 

Hello,

While checking out the Chamfer evaluation code, I noticed that the distance is computed between the sets of vertices of the two meshes. However, the correct way of computing Chamfer between meshes is by sampling a fixed large number of points from the surface of each mesh (eg. 500k). This way, it accounts in a fair manner for different mesh resolutions and topologies.  

I suggest the loading function in the evaluation script to be modified as follows:

`def load_obj_as_pointcloud(file_path):
     = trimesh.(file_path)
     .(.sample())
`

Thank you!


<a id="s007"></a>
## S007

- **source_id:** cvpr-metafood-3d-food-reconstruction-challenge:thread:509899:2861099
- **url:** https://www.kaggle.com/competitions/cvpr-metafood-3d-food-reconstruction-challenge/discussion/509899#comment-2861099
- **thread_id:** 509899
- **comment_id:** 2861099
- **author_name:** metafood-cvpr
- **author_role:** unknown
- **created_at:** 2024-06-08T03:11:04.880Z
- **retrieved_at:** 2026-10-20T16:01:28.563614+00:00
- **Archive locator:** `/discussion/1/text`

Sampling adds randomness. That is the reason we don't resample.

